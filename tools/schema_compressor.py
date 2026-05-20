#!/usr/bin/env python3
import os
import sys
import re
import argparse
import oracledb

def split_columns(column_defs_str):
    parts = []
    current = []
    depth = 0
    for char in column_defs_str:
        if char == '(':
            depth += 1
        elif char == ')':
            depth -= 1
        elif char == ',' and depth == 0:
            parts.append(''.join(current).strip())
            current = []
            continue
        current.append(char)
    if current:
        parts.append(''.join(current).strip())
    return [p for p in parts if p]

def shorten_type(type_str):
    t = type_str.upper().replace(" ", "")
    
    # Map VARCHAR2(N) / VARCHAR(N) -> VARCHAR(N)
    m = re.match(r'^(?:VARCHAR2|VARCHAR)\((\d+)\)$', t)
    if m:
        return f"VARCHAR({m.group(1)})"
        
    # Map NUMBER(N,0) -> NUM
    m_num0 = re.match(r'^NUMBER\((\d+),0\)$', t)
    if m_num0:
        return "NUM"
        
    # Map other NUMBER cases
    if t == 'NUMBER' or re.match(r'^NUMBER\(\d+\)$', t) or re.match(r'^NUMBER\(\d+,0\)$', t):
        return "NUM"
        
    # Keep DATE
    if t == 'DATE':
        return "DATE"
        
    # Fallback replacements
    if t.startswith('VARCHAR2'):
        return t.replace('VARCHAR2', 'VARCHAR')
    if t.startswith('NUMBER'):
        return 'NUM'
        
    return t

def build_oracle_type(dtype, dlen, dprec, dscale):
    dtype = dtype.upper()
    if dtype in ('VARCHAR2', 'VARCHAR', 'CHAR'):
        return f"{dtype}({dlen})"
    elif dtype == 'NUMBER':
        if dprec is not None and dprec != 'None' and str(dprec).strip() != '':
            scale = dscale if (dscale is not None and dscale != 'None') else 0
            return f"NUMBER({dprec},{scale})"
        return "NUMBER"
    return dtype

def parse_ddl_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        sql = f.read()
        
    # Remove comments
    sql = re.sub(r'--.*$', '', sql, flags=re.MULTILINE)
    sql = re.sub(r'/\*.*?\*/', '', sql, flags=re.DOTALL)
    
    # Split by semicolon
    statements = sql.split(';')
    
    schema = {}
    
    # 1. Parse CREATE TABLE statements
    for stmt in statements:
        stmt = stmt.strip()
        if not stmt:
            continue
            
        create_match = re.match(r'^CREATE\s+TABLE\s+(\w+)\s*\((.*)\)', stmt, re.IGNORECASE | re.DOTALL)
        if create_match:
            table_name = create_match.group(1).upper()
            body = create_match.group(2).strip()
            
            schema[table_name] = {
                'columns': [],
                'pks': set(),
                'fks': {}
            }
            
            items = split_columns(body)
            for item in items:
                item = item.strip()
                if not item:
                    continue
                
                # Check table-level PK constraint
                pk_table_match = re.match(r'^(?:CONSTRAINT\s+\w+\s+)?PRIMARY\s+KEY\s*\(([^)]+)\)', item, re.IGNORECASE)
                if pk_table_match:
                    cols = [c.strip().upper() for c in pk_table_match.group(1).split(',')]
                    schema[table_name]['pks'].update(cols)
                    continue
                    
                # Check table-level FK constraint
                fk_table_match = re.match(
                    r'^(?:CONSTRAINT\s+\w+\s+)?FOREIGN\s+KEY\s*\(([^)]+)\)\s*REFERENCES\s+(\w+)\s*\(([^)]+)\)', 
                    item, 
                    re.IGNORECASE
                )
                if fk_table_match:
                    local_cols = [c.strip().upper() for c in fk_table_match.group(1).split(',')]
                    ref_table = fk_table_match.group(2).upper()
                    ref_cols = [c.strip().upper() for c in fk_table_match.group(3).split(',')]
                    for lc, rc in zip(local_cols, ref_cols):
                        schema[table_name]['fks'][lc] = (ref_table, rc)
                    continue
                    
                # Inline PK and FK extraction
                is_pk = False
                if re.search(r'\bPRIMARY\s+KEY\b', item, re.IGNORECASE):
                    is_pk = True
                    item = re.sub(r'\bPRIMARY\s+KEY\b', '', item, flags=re.IGNORECASE).strip()
                    
                ref_match = re.search(r'\bREFERENCES\s+(\w+)\s*\(([^)]+)\)', item, re.IGNORECASE)
                inline_fk = None
                if ref_match:
                    ref_table = ref_match.group(1).upper()
                    ref_col = ref_match.group(2).strip().upper()
                    inline_fk = (ref_table, ref_col)
                    item = re.sub(r'\bREFERENCES\s+\w+\s*\([^)]+\)', '', item, flags=re.IGNORECASE).strip()
                    
                # Parse column name and type
                col_match = re.match(r'^(\w+)\s+([a-zA-Z0-9_]+\s*(?:\([^)]+\))?)', item)
                if col_match:
                    col_name = col_match.group(1).upper()
                    col_type = col_match.group(2).replace(" ", "")
                    
                    schema[table_name]['columns'].append((col_name, col_type))
                    if is_pk:
                        schema[table_name]['pks'].add(col_name)
                    if inline_fk:
                        schema[table_name]['fks'][col_name] = inline_fk
                        
    # 2. Parse ALTER TABLE statements
    for stmt in statements:
        stmt = stmt.strip()
        if not stmt:
            continue
            
        # Alter table PK
        alt_pk_match = re.match(
            r'^ALTER\s+TABLE\s+(\w+)\s+ADD\s+(?:CONSTRAINT\s+\w+\s+)?PRIMARY\s+KEY\s*\(([^)]+)\)', 
            stmt, 
            re.IGNORECASE
        )
        if alt_pk_match:
            table_name = alt_pk_match.group(1).upper()
            cols = [c.strip().upper() for c in alt_pk_match.group(2).split(',')]
            if table_name in schema:
                schema[table_name]['pks'].update(cols)
            continue
            
        # Alter table FK
        alt_fk_match = re.match(
            r'^ALTER\s+TABLE\s+(\w+)\s+ADD\s+(?:CONSTRAINT\s+\w+\s+)?FOREIGN\s+KEY\s*\(([^)]+)\)\s*REFERENCES\s+(\w+)\s*\(([^)]+)\)', 
            stmt, 
            re.IGNORECASE
        )
        if alt_fk_match:
            table_name = alt_fk_match.group(1).upper()
            local_cols = [c.strip().upper() for c in alt_fk_match.group(2).split(',')]
            ref_table = alt_fk_match.group(3).upper()
            ref_cols = [c.strip().upper() for c in alt_fk_match.group(4).split(',')]
            if table_name in schema:
                for lc, rc in zip(local_cols, ref_cols):
                    schema[table_name]['fks'][lc] = (ref_table, rc)
            continue
            
    return schema

def parse_connection_string(conn_str):
    match = re.match(r'^([^/]+)/([^@]+)@([^:/]+)(?::(\d+))?(?:/(.+)|:(.+))?$', conn_str)
    if not match:
        raise ValueError("Invalid connection string format. Use user/password@host:port/service_name")
    user = match.group(1)
    password = match.group(2)
    host = match.group(3)
    port = int(match.group(4)) if match.group(4) else 1521
    service_name = match.group(5)
    sid = match.group(6)
    
    if service_name:
        dsn = f"{host}:{port}/{service_name}"
    elif sid:
        dsn = f"{host}:{port}:{sid}"
    else:
        dsn = f"{host}:{port}"
        
    return user, password, dsn

def parse_database(conn_str):
    user, password, dsn = parse_connection_string(conn_str)
    schema = {}
    
    connection = oracledb.connect(user=user, password=password, dsn=dsn)
    try:
        cursor = connection.cursor()
        
        # 1. Fetch tables and columns
        cursor.execute("""
            SELECT table_name, column_name, data_type, data_length, data_precision, data_scale
            FROM user_tab_columns
            ORDER BY table_name, column_id
        """)
        for row in cursor.fetchall():
            table_name = row[0].upper()
            col_name = row[1].upper()
            dtype = str(row[2])
            dlen = row[3]
            dprec = row[4]
            dscale = row[5]
            
            col_type = build_oracle_type(dtype, dlen, dprec, dscale)
            
            if table_name not in schema:
                schema[table_name] = {
                    'columns': [],
                    'pks': set(),
                    'fks': {}
                }
            schema[table_name]['columns'].append((col_name, col_type))
            
        # 2. Fetch primary keys
        cursor.execute("""
            SELECT c.table_name, cc.column_name
            FROM user_constraints c
            JOIN user_cons_columns cc ON c.constraint_name = cc.constraint_name
            WHERE c.constraint_type = 'P'
        """)
        for row in cursor.fetchall():
            table_name = row[0].upper()
            col_name = row[1].upper()
            if table_name in schema:
                schema[table_name]['pks'].add(col_name)
                
        # 3. Fetch foreign keys
        cursor.execute("""
            SELECT 
                fk.table_name AS fk_table,
                fk_cols.column_name AS fk_column,
                pk.table_name AS pk_table,
                pk_cols.column_name AS pk_column
            FROM user_constraints fk
            JOIN user_cons_columns fk_cols ON fk.constraint_name = fk_cols.constraint_name
            JOIN user_constraints pk ON fk.r_constraint_name = pk.constraint_name
            JOIN user_cons_columns pk_cols ON pk.constraint_name = pk_cols.constraint_name 
                AND fk_cols.position = pk_cols.position
            WHERE fk.constraint_type = 'R'
        """)
        for row in cursor.fetchall():
            fk_table = row[0].upper()
            fk_col = row[1].upper()
            pk_table = row[2].upper()
            pk_col = row[3].upper()
            
            if fk_table in schema:
                schema[fk_table]['fks'][fk_col] = (pk_table, pk_col)
                
    finally:
        connection.close()
        
    return schema

def compress_schema(schema):
    output_lines = []
    for table_name in sorted(schema.keys()):
        table_info = schema[table_name]
        col_strings = []
        pks = table_info.get('pks', set())
        fks = table_info.get('fks', {})
        
        for col_name, col_type in table_info['columns']:
            col_name_upper = col_name.upper()
            short_type = shorten_type(col_type)
            col_str = f"{col_name_upper} {short_type}"
            
            constraints = []
            if col_name_upper in pks:
                constraints.append("PK")
            if col_name_upper in fks:
                ref_table, ref_col = fks[col_name_upper]
                constraints.append(f"FK -> {ref_table.upper()}.{ref_col.upper()}")
                
            if constraints:
                col_str += " " + " ".join(constraints)
                
            col_strings.append(col_str)
            
        table_str = f"{table_name.upper()}({', '.join(col_strings)})"
        output_lines.append(table_str)
        
    return "\n".join(output_lines)

def main():
    parser = argparse.ArgumentParser(description="Oracle Schema Compressor Utility")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", help="Path to local DDL SQL file")
    group.add_argument("-d", "--db", help="Oracle connection string (user/pass@host:port/service)")
    parser.add_argument("-o", "--output", help="Path to output text file (default: stdout)")
    
    args = parser.parse_args()
    
    try:
        if args.file:
            schema = parse_ddl_file(args.file)
        else:
            schema = parse_database(args.db)
            
        compressed = compress_schema(schema)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(compressed + "\n")
            print(f"Compressed schema successfully saved to '{args.output}'")
        else:
            print(compressed)
            
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
