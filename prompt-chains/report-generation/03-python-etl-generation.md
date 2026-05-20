# Report Generation Chain - 03 Python ETL Generation

Continue following `procedures/report_generator/SKILL.md`.

Generate the Python extraction and pandas transformation portions of the report
script. Use `references/python-idioms/sections/pandas_etl.md` as the relevant
drawer, but do not duplicate tutorial content from it.

Return code that includes:

1. Configuration placeholders for connection settings, SQL, bind parameters,
   and output paths.
2. Oracle extraction using `python-oracledb` Thin mode with safe cleanup.
3. pandas transformations with explicit dtype and null handling.
4. Clear function boundaries for extraction, transform, and orchestration.
5. Concise assumptions for any unresolved requirement gaps.

Do not add Excel styling yet unless it is required to keep the script coherent.
