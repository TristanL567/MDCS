#!/usr/bin/env python3
import os
import sys
import re
import math
import random
import hashlib
import argparse
import pandas as pd

def hash_val(val, salt="mdcs_salt"):
    s_val = str(val).strip()
    return hashlib.sha256((s_val + salt).encode('utf-8')).hexdigest()

def deterministic_id_mapping(val, is_numeric=True, prefix="ID_", salt="mdcs_salt"):
    if pd.isna(val):
        return val
    try:
        # Check if the value is logically an integer
        # e.g., 1001 or 1001.0
        val_str = str(val)
        if val_str.endswith('.0'):
            val_str = val_str[:-2]
        
        h = hash_val(val_str, salt)
        int_val = int(h[:8], 16)
        
        # If it looks like a number or is_numeric is true
        if is_numeric:
            return 100000 + (int_val % 900000)
        else:
            return f"{prefix}{1000 + (int_val % 9000)}"
    except Exception:
        # Fallback to string hash
        h = hash_val(val, salt)
        return f"{prefix}{h[:8]}"

def perturb_numeric(val, min_pct=0.05, max_pct=0.15, salt="mdcs_salt"):
    if pd.isna(val):
        return val
    try:
        # Convert to float
        num_val = float(val)
        if math.isnan(num_val) or math.isinf(num_val):
            return val
            
        h = hash_val(str(val), salt)
        seed_val = int(h[:8], 16)
        rng = random.Random(seed_val)
        
        pct = rng.uniform(min_pct, max_pct)
        sign = rng.choice([-1, 1])
        
        new_val = num_val * (1.0 + sign * pct)
        
        # Match type
        if isinstance(val, (int, sys.maxsize.__class__)):
            return int(round(new_val))
        elif isinstance(val, float):
            return round(new_val, 2)
        else:
            # If it was a string representing a number, return as float or int
            if '.' in str(val):
                return round(new_val, 2)
            return int(round(new_val))
    except Exception:
        return val

def random_mask_string(val, prefix="USER_", salt="mdcs_salt"):
    if pd.isna(val):
        return val
    h = hash_val(val, salt)
    int_val = int(h[:8], 16)
    return f"{prefix}{1000 + (int_val % 9000)}"

def mask_email(email_str, salt="mdcs_salt"):
    if pd.isna(email_str):
        return email_str
    s = str(email_str).strip()
    m = re.search(r'\b([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Z|a-z]{2,})\b', s)
    if m:
        prefix = m.group(1)
        h = hash_val(prefix, salt)
        anon_id = int(h[:8], 16) % 10000
        return f"anon_user_{anon_id}@example.com"
    return s

def mask_phone(phone_str, salt="mdcs_salt"):
    if pd.isna(phone_str):
        return phone_str
    s = str(phone_str).strip()
    digits = ''.join(c for c in s if c.isdigit())
    if len(digits) >= 7:
        h = hash_val(digits, salt)
        offset = int(h[:8], 16) % 9000
        return f"+1-555-01{offset:02d}"
    return s

def auto_detect_and_mask(col_name, series, salt="mdcs_salt"):
    col_lower = col_name.lower()
    
    # 1. Header Name Checks
    if 'id' in col_lower:
        is_num = pd.api.types.is_numeric_dtype(series)
        return series.apply(lambda x: deterministic_id_mapping(x, is_numeric=is_num, salt=salt) if pd.notna(x) else x)
        
    if 'email' in col_lower or 'mail' in col_lower:
        return series.apply(lambda x: mask_email(x, salt) if pd.notna(x) else x)
        
    if 'phone' in col_lower or 'tel' in col_lower or 'mobile' in col_lower:
        return series.apply(lambda x: mask_phone(x, salt) if pd.notna(x) else x)
        
    if any(k in col_lower for k in ['name', 'fname', 'lname', 'fullname', 'contact', 'customer', 'employee', 'manager']):
        return series.apply(lambda x: random_mask_string(x, "NAME_", salt) if pd.notna(x) else x)
        
    if 'salary' in col_lower or 'wage' in col_lower or 'amount' in col_lower or 'cost' in col_lower or 'price' in col_lower or 'invoice' in col_lower:
        return series.apply(lambda x: perturb_numeric(x, salt=salt) if pd.notna(x) else x)
        
    # 2. Content Checks (Regex Fallbacks)
    non_nulls = series.dropna()
    if len(non_nulls) == 0:
        return series
        
    sample = non_nulls.head(20).astype(str)
    
    # Check email
    email_pattern = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$', re.IGNORECASE)
    email_matches = sum(1 for s in sample if email_pattern.match(s.strip()))
    if email_matches >= len(sample) * 0.5:
        return series.apply(lambda x: mask_email(x, salt) if pd.notna(x) else x)
        
    # Check phone
    phone_pattern = re.compile(r'^\+?[\d\s\-\(\)\.]{7,20}$')
    phone_matches = sum(1 for s in sample if phone_pattern.match(s.strip()))
    if phone_matches >= len(sample) * 0.5:
        return series.apply(lambda x: mask_phone(x, salt) if pd.notna(x) else x)
        
    # Check typical name pattern (Two capitalized words, e.g. "John Smith")
    name_pattern = re.compile(r'^[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+$')
    name_matches = sum(1 for s in sample if name_pattern.match(s.strip()))
    if name_matches >= len(sample) * 0.5:
        return series.apply(lambda x: random_mask_string(x, "NAME_", salt) if pd.notna(x) else x)
        
    return series

def main():
    parser = argparse.ArgumentParser(description="Lightweight Data Anonymizer")
    parser.add_argument("-i", "--input", required=True, help="Path to input CSV or Excel file")
    parser.add_argument("-o", "--output", required=True, help="Path to save output file")
    parser.add_argument("-c", "--columns", help="Comma-separated list of column names to mask")
    parser.add_argument("-s", "--strategy", choices=['hash', 'perturb', 'mask', 'auto'], default='auto',
                        help="Anonymization strategy: hash (join-preserving id), perturb (numeric noise), mask (random user ID), auto (run PII detector)")
    parser.add_argument("--salt", default="mdcs_salt", help="Salt value for deterministic hashing")
    parser.add_argument("--min-pct", type=float, default=0.05, help="Min numeric perturbation percentage (default: 0.05)")
    parser.add_argument("--max-pct", type=float, default=0.15, help="Max numeric perturbation percentage (default: 0.15)")
    
    args = parser.parse_args()
    
    try:
        # Load file
        ext = os.path.splitext(args.input)[1].lower()
        if ext == '.csv':
            df = pd.read_csv(args.input)
        elif ext in ['.xlsx', '.xls']:
            df = pd.read_excel(args.input)
        else:
            raise ValueError("Unsupported file format. Please use CSV or Excel (.xlsx, .xls)")
            
        columns_to_mask = []
        if args.columns:
            columns_to_mask = [col.strip() for col in args.columns.split(',')]
            # Check if columns exist
            for c in columns_to_mask:
                if c not in df.columns:
                    print(f"Warning: Column '{c}' not found in input data.", file=sys.stderr)
                    
        # Apply strategies
        if columns_to_mask:
            for col in columns_to_mask:
                if col not in df.columns:
                    continue
                if args.strategy == 'hash':
                    # Check if the column consists of mostly numeric types
                    is_num = pd.api.types.is_numeric_dtype(df[col])
                    df[col] = df[col].apply(lambda x: deterministic_id_mapping(x, is_numeric=is_num, salt=args.salt))
                elif args.strategy == 'perturb':
                    df[col] = df[col].apply(lambda x: perturb_numeric(x, args.min_pct, args.max_pct, salt=args.salt))
                elif args.strategy == 'mask':
                    df[col] = df[col].apply(lambda x: random_mask_string(x, "VAL_", salt=args.salt))
                elif args.strategy == 'auto':
                    df[col] = auto_detect_and_mask(col, df[col], salt=args.salt)
        else:
            # Auto-detect PII on all columns
            for col in df.columns:
                df[col] = auto_detect_and_mask(col, df[col], salt=args.salt)
                
        # Save output
        if ext == '.csv':
            df.to_csv(args.output, index=False)
        else:
            df.to_excel(args.output, index=False)
            
        print(f"Anonymized file successfully saved to '{args.output}'")
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
