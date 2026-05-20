---
id: MDCS-TICKET-001
title: Setup repository structure and local library validator.
epic: epic-dumb-copilot
status: ready
risk: low
allowed_areas:
  - tools/
  - procedures/
  - references/
must_not_touch:
  - .git/
requirements:
  - Create the folder structure: `tools/`, `procedures/`, `references/`.
  - Implement/rewrite a local Python validator script `tools/validate_mdcs_library.py`. (Note: This is a reopened/superseding requirement to replace the temporary or older 4-key contract validator).
  - The validator must require and parse the full Aegis procedural-skill contract on every closet prompt under `procedures/*/SKILL.md`:
    * YAML frontmatter must contain all 10 canonical keys: `trigger`, `non_trigger`, `failure_modes_addressed`, `attention_signals`, `procedure`, `scope_boundary`, `composition_points`, `reference_pointers`, `verification`, `output_contract`.
    * Closet size budget: at most 200 lines total.
    * `reference_pointers` must be a list of structured mappings, each containing keys: `ref`, `section`, and `open_when`.
    * An empty list `[]` is valid.
    * The validator must reject any `reference_pointers` entry that is a bare string instead of a structured mapping.
    * The validator must verify that `ref` resolves to `references/<ref>/` and `section` resolves to `references/<ref>/sections/<section>.md`.
  - The validator must require and parse the Aegis reference index contract on every index under `references/*/README.md`:
    * Index size budget: at most 120 lines total.
    * Must contain a markdown Sections table with columns: `id | topic | open when` (note the exact space in "open when").
    * Every `id` in the Sections table must resolve to a file under `references/<ref>/sections/<id>.md`.
  - The validator must require and parse the Aegis section drawer contract on every drawer under `references/*/sections/*.md`:
    * Drawer size budget: at most 150 lines total.
    * Each drawer must begin with a one-line `relevant-when:` header (e.g., `relevant-when: <description>`), which is a key-style line rather than a markdown heading.
  - The validator must use `PyYAML` to parse nested structures (require PyYAML in `tools/requirements.txt`).
non_goals:
  - Do not implement the actual schema compressor or data anonymizer code in this ticket.
  - Do not build roles or operating-discipline layers. MDCS is adapted to support only the procedural and reference layers.
acceptance_criteria:
  - Running `python tools/validate_mdcs_library.py` executes successfully on a valid repository.
  - The validator successfully rejects a `SKILL.md` missing any of the 10 keys, or exceeding 200 lines, or containing string-based `reference_pointers`.
  - The validator successfully rejects a `README.md` index exceeding 120 lines or lacking the `id | topic | open when` columns.
  - The validator successfully rejects a section drawer exceeding 150 lines or missing the one-line `relevant-when:` header.
verification_commands:
  - python tools/validate_mdcs_library.py
depends_on: []
---

# Body

## Goal

Re-author the folder layout and local validation script to enforce the canonical Aegis Closet/Drawer contract.

## Context

The previous validator implemented a subset of Aegis rules. To ensure our Copilot prompts stay robust, we are adopting the complete Aegis structure: 10-key frontmatter for procedures, structured reference pointers, table column names matching the core template, and key-style `relevant-when:` headers for drawers.

## Procedure

1. Reopen and replace the old validator in `tools/validate_mdcs_library.py`.
2. Configure `tools/requirements.txt` to require `PyYAML`.
3. Implement YAML parsing using PyYAML to support nested lists and mappings in `reference_pointers`.
4. Validate size limits (closet: 200 lines, index: 120 lines, drawer: 150 lines).
5. Assert pointer integrity (resolve `ref` and `section` keys to actual files).
6. Verify drawer-specific constraints (`relevant-when:` first line).
7. Create temporary malformed files to verify each error condition is correctly reported, then delete them.
