---
id: MDCS-TICKET-008
title: Create Mock Data Generator procedural closet.
epic: epic-dumb-copilot
status: ready
risk: low
allowed_areas:
  - procedures/mock_data_generator/
must_not_touch:
  - tools/
  - references/
requirements:
  - Create the Mock Data Generator procedural closet directory: `procedures/mock_data_generator/`.
  - Create `procedures/mock_data_generator/SKILL.md`.
  - Ensure the file has valid frontmatter containing all 10 canonical Aegis keys:
    * `trigger`, `non_trigger`, `failure_modes_addressed`, `attention_signals`, `procedure`, `scope_boundary`, `composition_points`, `reference_pointers`, `verification`, `output_contract`.
  - Ensure `reference_pointers` is a list of structured mappings, pointing to:
    * `ref: oracle-sql`, `section: plsql_basics`, `open_when: mock data needs to be populated via PL/SQL bulk blocks or loops.`
    * `ref: oracle-sql`, `section: oracle_idioms`, `open_when: mock data requires specific Oracle date styles or sequences.`
  - Write a step-by-step interactive prompt procedure (under 200 lines total).
  - Ensure the `procedure` field in the frontmatter serves as a compact skeleton of the steps, and details of the analysis go into the drawers.
  - The step-by-step prompt itself will:
    1. **Persona & Context Bootstrapping**: Sets up Copilot's Test Data Engineer persona.
    2. **Schema Intake**: Instructions to feed the compressed schema representation (from `schema_compressor.py`).
    3. **Integrity Hierarchy Analysis**: Prompts Copilot to determine the dependency hierarchy of the tables (generating parent tables with primary keys before child tables with foreign keys) to avoid integrity constraint violations.
    4. **Script Generation**: Directs Copilot to write a Python script or PL/SQL block that generates a defined number of rows (e.g. 100 rows per table) with realistic data values.
    5. **Format Execution**: Instructions on generating output either as SQL `INSERT` statements or CSVs.
non_goals:
  - Do not write concrete data generation code blocks directly in the closet SKILL.md.
acceptance_criteria:
  - Running `python tools/validate_mdcs_library.py` executes successfully.
  - The `SKILL.md` is strictly under 200 lines and contains all 10 keys.
  - Pointers in `reference_pointers` are structured with `ref`, `section`, and `open_when` keys.
verification_commands:
  - python tools/validate_mdcs_library.py
depends_on:
  - MDCS-TICKET-002
  - MDCS-TICKET-004
---

# Body

## Goal

Create a lightweight procedural closet prompt that guides Copilot step-by-step to generate schema-compliant mock data.

## Context

To test SQL scripts or Python reports safely, we need realistic dummy data. Generating this mock data manually is tedious. The closet guides Copilot to analyze foreign key dependencies and generate generation scripts (SQL or Python) that load tables in the correct order.

## Procedure

1. Create `procedures/mock_data_generator/SKILL.md` with appropriate YAML frontmatter.
2. Design the prompt workflow to analyze parent-child relationships first.
3. Add reference pointers linking to the Oracle SQL references.
4. Validate using the library validator.
