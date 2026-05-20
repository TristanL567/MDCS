---
id: MDCS-TICKET-005
title: Create Python idioms reference drawers.
epic: epic-dumb-copilot
status: ready
risk: low
allowed_areas:
  - references/python-idioms/
must_not_touch:
  - tools/
  - procedures/
requirements:
  - Create the Python idioms reference directory structure: `references/python-idioms/sections/`.
  - Create `references/python-idioms/README.md` as the index. It must:
    * Declares the reference scope and consuming skills.
    * Limit the index size to at most 120 lines total.
    * Contain a markdown Sections table with columns: `id | topic | open when` (note the exact space in "open when").
    * Map the following drawers: `pandas_etl` and `openpyxl_excel`.
  - Create `references/python-idioms/sections/pandas_etl.md`:
    * Limit size to at most 150 lines total.
    * Begin with a one-line `relevant-when:` header key-style line.
    * Focus on connecting python to Oracle using `oracledb` in Thin mode.
    * Provide patterns for executing select queries, cursor fetching, and mapping to pandas DataFrames.
    * Handle memory allocation (e.g., chunking, using generators) and type conversion safety (e.g., converting decimals, mapping Oracle Dates).
  - Create `references/python-idioms/sections/openpyxl_excel.md`:
    * Limit size to at most 150 lines total.
    * Begin with a one-line `relevant-when:` header key-style line.
    * Provide patterns to format Excel workbooks generated via `openpyxl` (fonts, borders, cell fills, number formats).
    * Show how to auto-fit columns, freeze panes, apply filters, and write multi-sheet workbooks.
non_goals:
  - Do not cover generic python algorithms or frontend libraries. Focus strictly on Oracle-Pandas ETL and openpyxl formatting.
acceptance_criteria:
  - Running `python tools/validate_mdcs_library.py` passes on the Python references.
  - The index is ≤120 lines and sections are ≤150 lines.
  - Every drawer begins with a one-line `relevant-when:` header.
verification_commands:
  - python tools/validate_mdcs_library.py
depends_on:
  - MDCS-TICKET-001
---

# Body

## Goal

Compile standard, dense Python reference drawers to feed Copilot during active procedures for ETL and reporting tasks.

## Context

Writing data-loading and Excel-formatting scripts is a repetitive IT-BA task. Edge Copilot often produces outdated `cx_Oracle` code or unstyled Excel sheets. Providing these modern drawers ensures Copilot writes robust, copy-pasteable Python code.

## Procedure

1. Initialize `references/python-idioms/README.md` and write the index table.
2. Draft `references/python-idioms/sections/pandas_etl.md` starting with a `relevant-when:` header and showing how to execute database reads and convert cursors to dataframes using the modern `oracledb` thin mode.
3. Draft `references/python-idioms/sections/openpyxl_excel.md` starting with a `relevant-when:` header and detailing professional spreadsheet styling.
4. Run the validator tool to verify formatting and line count constraints.
