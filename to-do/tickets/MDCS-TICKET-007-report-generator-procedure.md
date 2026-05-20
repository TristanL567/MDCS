---
id: MDCS-TICKET-007
title: Create Report Generator procedural closet.
epic: epic-dumb-copilot
status: ready
risk: low
allowed_areas:
  - procedures/report_generator/
must_not_touch:
  - tools/
  - references/
requirements:
  - Create the Report Generator procedural closet directory: `procedures/report_generator/`.
  - Create `procedures/report_generator/SKILL.md`.
  - Ensure the file has valid frontmatter containing all 10 canonical Aegis keys:
    * `trigger`, `non_trigger`, `failure_modes_addressed`, `attention_signals`, `procedure`, `scope_boundary`, `composition_points`, `reference_pointers`, `verification`, `output_contract`.
  - Ensure `reference_pointers` is a list of structured mappings, pointing to:
    * `ref: python-idioms`, `section: pandas_etl`, `open_when: python script needs to query Oracle or load/map data to Pandas DataFrames.`
    * `ref: python-idioms`, `section: openpyxl_excel`, `open_when: script needs to generate or apply formatting/styling to an Excel workbook.`
  - Write a step-by-step interactive prompt procedure (under 200 lines total).
  - Ensure the `procedure` field in the frontmatter serves as a compact skeleton of the steps, and details of the analysis go into the drawers.
  - The step-by-step prompt itself will:
    1. **Persona & Context Bootstrapping**: Sets up Copilot's Senior Python Developer persona.
    2. **Requirements Intake**: Prompts Copilot to request:
       - The SQL query or compressed table schemas.
       - The target Excel spreadsheet layout (sheets, headers, formatting preferences).
    3. **Extraction & Transformation Code**: Directs Copilot to generate clean `oracledb` connection handling and Pandas mapping.
    4. **Spreadsheet Styling Code**: Directs Copilot to generate openpyxl styling blocks (colors, widths, borders).
    5. **Error & Memory Handling**: Instructs Copilot to add connection block cleanups and type checking.
non_goals:
  - Do not write concrete openpyxl or pandas formatting blocks directly in the closet SKILL.md. Use the reference drawers for this.
acceptance_criteria:
  - Running `python tools/validate_mdcs_library.py` executes successfully.
  - The `SKILL.md` is strictly under 200 lines and contains all 10 keys.
  - Pointers in `reference_pointers` are structured with `ref`, `section`, and `open_when` keys.
verification_commands:
  - python tools/validate_mdcs_library.py
depends_on:
  - MDCS-TICKET-005
---

# Body

## Goal

Create a lightweight procedural closet prompt that guides Copilot step-by-step to write Python scripts that load Oracle query results and format them in Excel.

## Context

Generating spreadsheets is a core task. Copilot tends to write single large blocks of code without styling or with legacy database connection methods. The closet guides it through modular development: database extraction first, then dataframe manipulation, then spreadsheet styling.

## Procedure

1. Create `procedures/report_generator/SKILL.md` with appropriate YAML frontmatter.
2. Draft the prompt sequence using clear tags.
3. Add reference pointers linking to the Python reference drawers.
4. Validate using the library validator.
