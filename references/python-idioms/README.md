# Python Idioms Reference Index

This reference contains Python drawer patterns for Oracle-to-Pandas ETL and
openpyxl Excel reporting work in MDCS. It is an index only; open the section
drawer that matches the active implementation task.

## Scope

- Modern `python-oracledb` Thin mode SELECT extraction into pandas.
- Memory-safe cursor fetching and DataFrame construction.
- openpyxl workbook, worksheet, table, and report formatting idioms.
- No generic Python algorithms, credentials, private schema names, or company data.

## Consuming Procedures

- `procedures/report_generator/SKILL.md`

## Sections

| id | topic | open when |
|---|---|---|
| pandas_etl | Oracle Thin mode connections, SELECT execution, cursor fetching, DataFrame mapping, chunking, and safe type conversion | extracting Oracle data into pandas or normalizing database values |
| openpyxl_excel | Workbook creation, multi-sheet reports, DataFrame writes, styles, column sizing, freeze panes, filters, and number formats | building or formatting Excel reports with openpyxl |
