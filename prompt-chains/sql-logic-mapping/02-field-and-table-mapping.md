# SQL Logic Mapping Chain - 02 Field And Table Mapping

Continue the SQL logic mapping workflow.

Using the business request and context already provided, create a structured
logic-map table before writing any SQL.

Use exactly these columns:

| input requirement | business rule | table | field | join key | filter condition | derived calculation | aggregation level | output column | ambiguity or assumption |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

For each row, map one business requirement or output element to the likely SQL
implementation components.

Explicitly flag:

1. Missing table relationships.
2. Missing or unclear fields.
3. Ambiguous field names.
4. Missing date windows.
5. Contradictory filters.
6. Rules that need derived calculations.
7. Requirements that have no known source table.

Do not write SQL. If any row has unresolved ambiguity, ask clarification
questions after the table.
