# SQL Result Validation Chain - 01 Query And Intent Intake

Act as an Oracle SQL result validation reviewer.

This workflow validates result correctness, not just SQL syntax. Do not rewrite
or optimize the query yet. Copilot does not have database access, so propose
checks that I can run locally and ask for evidence I need to collect.

Current Oracle SQL:

```sql
<paste the full Oracle SQL query here, including CTEs, joins, filters, and final SELECT>
```

Business intent:

```text
<paste the reporting goal, business rule, expected result, or acceptance criteria here>
```

Expected output grain:

```text
<example: one row per customer per month; one row per policy; one row per account/status/date>
```

Key dimensions and expected row-count behavior:

```text
<paste output keys, grouping dimensions, row-count expectations, and any known totals by segment>
```

Required output fields and null rules:

```text
<paste fields that must be populated, fields allowed to be null, and why>
```

Metric definitions and reconciliation targets:

```text
<paste definitions for counts, sums, distinct counts, rates, source totals, or old-vs-new totals>
```

Date-window rules:

```text
<paste date fields, start/end dates, inclusive/exclusive boundaries, reporting periods, and timezone or truncation rules>
```

Known schema context:

```text
<paste source tables, primary keys, foreign keys, natural keys, join notes, date fields, and one-to-many relationship notes>
```

Available validation evidence:

```text
<paste any row counts, duplicate counts, null counts, reconciliation totals, samples, or observed incorrect behavior>
```

Return:

1. Inferred business objective.
2. Expected final output grain and whether it is explicit or inferred.
3. Candidate output key columns for duplicate checks.
4. Required output fields that need null checks.
5. Key dimensions for row-count checks.
6. Metrics that need aggregate reconciliation.
7. CTEs, joins, and date filters that appear validation-sensitive.
8. Missing context or evidence required before result correctness can be
   validated.
9. A short local-evidence request list for the next prompt.

Point me to `references/oracle-sql/sections/cte_patterns.md`,
`references/oracle-sql/sections/join_patterns.md`, or
`references/oracle-sql/sections/aggregation_patterns.md` where relevant, but do
not repeat long tutorial content from those drawers.
