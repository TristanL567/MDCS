# SQL Aggregation Chain - 03 Group By And Having Design

Continue the Oracle SQL aggregation workflow.

Use the accepted output grain and aggregation map to design the grouped query
structure. Do not write final SQL yet.

Accepted output grain:

```text
<paste the accepted "one row per ..." output grain and grain fields here>
```

Accepted aggregation map:

```text
<paste the completed aggregation map here>
```

Return:

1. `SELECT` output fields, separating grouped fields from aggregate fields.
2. Required `GROUP BY` fields or expressions. Every non-aggregate selected
   expression must be accounted for.
3. Input filters that belong in `WHERE` before aggregation.
4. Group filters that belong in `HAVING` after aggregation.
5. Any aggregate expression repeated in `HAVING` and why it belongs there.
6. Conditional aggregation expressions needed for filtered metrics, with the
   `CASE` logic described in words.
7. Null handling for each metric, including whether nulls should be ignored,
   counted, preserved, or converted with `NVL`.
8. Any `COUNT(*)`, `COUNT(field)`, or `COUNT DISTINCT field` distinction that
   affects the business result.
9. Readiness status: ready for edge-case review or blocked.

Rules:

1. Use `WHERE` for input-row filters before aggregation.
2. Use `HAVING` only for rules that depend on aggregate results or grouped
   rows.
3. Do not use `NVL` to turn nulls into zero unless the business definition says
   missing values should behave as zero.
4. Do not write final SQL if any grouped field, aggregate expression, or
   `HAVING` rule is unresolved.
