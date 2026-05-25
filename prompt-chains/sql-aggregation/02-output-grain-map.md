# SQL Aggregation Chain - 02 Output Grain Map

Continue the Oracle SQL aggregation workflow.

Before writing any SQL, define the output grain and create the aggregation map.
The output grain must be explicit and accepted before SQL generation.

Current request and answers:

```text
<paste the business request, intake answer, and any clarification answers here>
```

Schema and relationship notes:

```text
<paste source tables, fields, keys, join notes, row counts, and null semantics here>
```

First return:

1. Proposed output grain, stated as "one row per ...".
2. The exact fields or expressions that define that grain.
3. Any source tables that are at a lower grain than the requested output.
4. Any source tables that could duplicate metric rows if joined before
   aggregation.
5. Whether any metric should use analytic/window functions instead of grouped
   aggregation because detail rows need to remain visible.

Then create the aggregation map.

Use this exact aggregation map table shape:

```text
business metric | source table | source field | filter | grouping grain | aggregate function | HAVING rule | output field | validation check
```

For each metric, fill one row and explicitly cover:

1. The business definition of the metric.
2. The source table and source field, or `*` for `COUNT(*)`.
3. Input-row filters that belong in `WHERE`.
4. The grouping grain fields.
5. The aggregate function: `COUNT`, `COUNT DISTINCT`, `SUM`, `AVG`, `MIN`,
   `MAX`, or conditional aggregation.
6. Any `HAVING` rule that filters aggregate groups after grouping.
7. The output field name.
8. A validation check for the grouped result.

Do not write SQL. If the output grain, aggregate function, null handling, or
validation check is missing for any metric, mark the workflow blocked and ask
only the questions needed to complete the map.
