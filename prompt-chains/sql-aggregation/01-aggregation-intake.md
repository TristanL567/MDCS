# SQL Aggregation Chain - 01 Aggregation Intake

Act as a senior Oracle SQL analyst designing grouped metrics. This is step 1
of a multi-turn aggregation workflow.

This is not yet a final SQL-writing step. First, clarify the business metrics,
source context, output grain, and validation needs. Do not write SQL yet.

Business request:

```text
<paste reporting request, metric definitions, stakeholder notes, acceptance criteria, or sample output here>
```

Known source context:

```text
<paste relevant tables, fields, keys, joins, row counts, filters, date windows, and null semantics here>
```

Return:

1. Restated aggregation objective.
2. Candidate business metrics and whether each appears to need `COUNT`,
   `COUNT DISTINCT`, `SUM`, `AVG`, `MIN`, `MAX`, or conditional aggregation.
3. Candidate output grain, stated as "one row per ...".
4. Candidate source tables and source fields.
5. Known input filters that belong in `WHERE`.
6. Possible group-level rules that may belong in `HAVING`.
7. Null-handling questions for each metric.
8. Duplicate-risk questions, especially where joins may multiply rows before
   aggregation.
9. Whether grouped aggregation is appropriate, or whether analytic/window
   functions may be better because detail rows must remain visible.
10. Clarification questions that must be answered before SQL can be written.

Block SQL generation if metric definitions, output grain, source fields, join
paths, or validation expectations are incomplete.
