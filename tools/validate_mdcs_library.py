#!/usr/bin/env python3
import os
import sys
import yaml

def parse_frontmatter(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return None, f"Failed to read file: {e}"
        
    lines = content.splitlines()
    if not lines or lines[0].strip() != '---':
        return None, "File does not start with YAML frontmatter delimiter '---'"
        
    end_idx = -1
    for idx in range(1, len(lines)):
        if lines[idx].strip() == '---':
            end_idx = idx
            break
            
    if end_idx == -1:
        return None, "YAML frontmatter is not closed with '---'"
        
    yaml_text = '\n'.join(lines[1:end_idx])
    try:
        data = yaml.safe_load(yaml_text)
        if not isinstance(data, dict):
            return None, "Frontmatter is not a key-value dictionary"
        return data, None
    except Exception as e:
        return None, f"YAML parse error: {e}"

def parse_sections_table(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return None, f"Failed to read README: {e}"
        
    lines = content.splitlines()
    header_idx = -1
    
    for idx, line in enumerate(lines):
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 3:
            if parts[0] == '':
                parts = parts[1:]
            if parts and parts[-1] == '':
                parts = parts[:-1]
                
            # Must check columns exactly: id | topic | open when
            if len(parts) >= 3 and parts[0].lower() == 'id' and parts[1].lower() == 'topic' and parts[2].lower() == 'open when':
                header_idx = idx
                break
                
    if header_idx == -1:
        return None, "Missing Sections table with columns: id, topic, open when"
        
    if header_idx + 1 >= len(lines):
        return None, "Table has a header but no divider or rows"
        
    # Check divider
    divider_line = lines[header_idx + 1].strip()
    divider_parts = [p.strip() for p in divider_line.split('|')]
    if divider_parts[0] == '':
        divider_parts = divider_parts[1:]
    if divider_parts and divider_parts[-1] == '':
        divider_parts = divider_parts[:-1]
        
    is_divider = len(divider_parts) >= 3 and all(all(c in '-: ' for c in part) and len(part) > 0 for part in divider_parts)
    start_row = header_idx + 2 if is_divider else header_idx + 1
    
    section_ids = []
    for i in range(start_row, len(lines)):
        line = lines[i].strip()
        if not line or '|' not in line:
            break
        parts = [p.strip() for p in line.split('|')]
        if parts[0] == '':
            parts = parts[1:]
        if parts and parts[-1] == '':
            parts = parts[:-1]
            
        if len(parts) >= 1:
            sec_id = parts[0].strip().strip('`*_"\'')
            if sec_id:
                section_ids.append(sec_id)
                
    return section_ids, None

def get_line_count(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return len(f.readlines())
    except Exception:
        return 0

def check_starts_with_relevant_when(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                stripped = line.strip()
                if not stripped:
                    continue
                # Enforce that it starts with 'relevant-when:'
                return stripped.startswith('relevant-when:')
    except Exception:
        return False
    return False

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, '..'))
    
    errors = []
    
    # 1. Procedures (procedures/*/SKILL.md)
    procedures_dir = os.path.join(repo_root, 'procedures')
    if os.path.exists(procedures_dir) and os.path.isdir(procedures_dir):
        for sub in os.listdir(procedures_dir):
            sub_path = os.path.join(procedures_dir, sub)
            if os.path.isdir(sub_path):
                skill_file = os.path.join(sub_path, 'SKILL.md')
                if os.path.exists(skill_file):
                    # Check line count
                    lines_count = get_line_count(skill_file)
                    if lines_count >= 200:
                        errors.append(f"{skill_file}: File size ({lines_count} lines) must be strictly under 200 lines.")
                    
                    # Parse frontmatter
                    data, err = parse_frontmatter(skill_file)
                    if err:
                        errors.append(f"{skill_file}: Frontmatter validation error: {err}")
                    else:
                        # Check canonical 10 keys
                        canonical_keys = [
                            'trigger', 'non_trigger', 'failure_modes_addressed', 
                            'attention_signals', 'procedure', 'scope_boundary', 
                            'composition_points', 'reference_pointers', 'verification', 
                            'output_contract'
                        ]
                        for key in canonical_keys:
                            if key not in data:
                                errors.append(f"{skill_file}: Frontmatter is missing required key '{key}'")
                        
                        # Validate reference_pointers
                        ref_pointers = data.get('reference_pointers', [])
                        if not isinstance(ref_pointers, list):
                            errors.append(f"{skill_file}: Frontmatter key 'reference_pointers' must be a list.")
                        else:
                            for idx, ptr in enumerate(ref_pointers):
                                if isinstance(ptr, str):
                                    errors.append(f"{skill_file}: reference_pointers entry at index {idx} must be a structured mapping, not a bare string: '{ptr}'")
                                    continue
                                elif not isinstance(ptr, dict):
                                    errors.append(f"{skill_file}: reference_pointers entry at index {idx} must be a structured mapping, got '{type(ptr).__name__}'")
                                    continue
                                
                                # Check keys
                                mapping_keys = ['ref', 'section', 'open_when']
                                for mk in mapping_keys:
                                    if mk not in ptr:
                                        errors.append(f"{skill_file}: reference_pointers entry at index {idx} is missing key '{mk}'")
                                
                                ref_val = ptr.get('ref')
                                sec_val = ptr.get('section')
                                
                                if not isinstance(ref_val, str) or not ref_val:
                                    errors.append(f"{skill_file}: reference_pointers entry at index {idx} has invalid 'ref' (must be a non-empty string)")
                                    continue
                                    
                                if not isinstance(sec_val, str) or not sec_val:
                                    errors.append(f"{skill_file}: reference_pointers entry at index {idx} has invalid 'section' (must be a non-empty string)")
                                    continue
                                
                                # Verify resolution
                                ref_dir = os.path.abspath(os.path.join(repo_root, 'references', ref_val))
                                if not os.path.exists(ref_dir) or not os.path.isdir(ref_dir):
                                    errors.append(f"{skill_file}: reference_pointers entry ref '{ref_val}' does not resolve to an existing directory at '{ref_dir}'")
                                else:
                                    sec_file = os.path.abspath(os.path.join(ref_dir, 'sections', f"{sec_val}.md"))
                                    if not os.path.exists(sec_file) or not os.path.isfile(sec_file):
                                        errors.append(f"{skill_file}: reference_pointers entry section '{sec_val}' does not resolve to an existing drawer file at '{sec_file}'")
                                        
    # 2. References (references/*/README.md)
    references_dir = os.path.join(repo_root, 'references')
    if os.path.exists(references_dir) and os.path.isdir(references_dir):
        for sub in os.listdir(references_dir):
            sub_path = os.path.join(references_dir, sub)
            if os.path.isdir(sub_path):
                readme_file = os.path.join(sub_path, 'README.md')
                if os.path.exists(readme_file):
                    # Check line count
                    lines_count = get_line_count(readme_file)
                    if lines_count >= 120:
                        errors.append(f"{readme_file}: File size ({lines_count} lines) must be strictly under 120 lines.")
                    
                    # Parse Sections table
                    section_ids, err = parse_sections_table(readme_file)
                    if err:
                        errors.append(f"{readme_file}: Markdown table error: {err}")
                    else:
                        # Verify every id maps to an existing drawer file
                        for sec_id in section_ids:
                            drawer_path = os.path.join(sub_path, 'sections', f"{sec_id}.md")
                            if not os.path.exists(drawer_path):
                                errors.append(f"{readme_file}: Section ID '{sec_id}' in Sections table does not resolve to an existing drawer file at '{drawer_path}'.")
                                
                # 3. Section Drawers (references/*/sections/*.md)
                sections_dir = os.path.join(sub_path, 'sections')
                if os.path.exists(sections_dir) and os.path.isdir(sections_dir):
                    for file_name in os.listdir(sections_dir):
                        if file_name.endswith('.md'):
                            drawer_file = os.path.join(sections_dir, file_name)
                            
                            # Check line count
                            lines_count = get_line_count(drawer_file)
                            if lines_count >= 150:
                                errors.append(f"{drawer_file}: File size ({lines_count} lines) must be strictly under 150 lines.")
                                
                            # Check starts with relevant-when:
                            if not check_starts_with_relevant_when(drawer_file):
                                errors.append(f"{drawer_file}: Must start with a 'relevant-when:' header key-style line.")
                                
    if errors:
        print("Validation FAILED with the following errors:", file=sys.stderr)
        for err in errors:
            print(f" - {err}", file=sys.stderr)
        sys.exit(1)
    else:
        print("Validation PASSED successfully.")
        sys.exit(0)

if __name__ == '__main__':
    main()
