# Report Generation Prompt Chain

## Use Case

Use this chain when a human analyst needs Edge Copilot to generate a maintainable
Python script that extracts Oracle data, transforms it with pandas, and writes a
formatted Excel workbook.

## Required Local Preparation

- Gather business reporting requirements, workbook layout, sheet names, and
  expected formatting.
- Prepare SQL or compressed schema context plus extraction intent.
- Know the local Python version, dependency constraints, credential method, and
  output file path.
- Prepare sample row counts, validation totals, or expected workbook checks.

## Prompt Sequence

1. `01-requirements-intake.md`: collect report and runtime requirements.
2. `02-sql-schema-submission.md`: submit SQL, schema notes, and data rules.
3. `03-python-etl-generation.md`: request extraction and pandas transform code.
4. `04-excel-formatting-generation.md`: request workbook writing and styling.
5. `05-script-review-verification.md`: review the full script and local checks.

## Related Procedure Closet

- `procedures/report_generator/SKILL.md`

## Related Reference Drawers

- `references/python-idioms/sections/pandas_etl.md`
- `references/python-idioms/sections/openpyxl_excel.md`
