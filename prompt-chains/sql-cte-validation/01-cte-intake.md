# SQL CTE Validation Chain - 01 CTE Intake

Act as an Oracle SQL reviewer focused on common table expression correctness.

This is a CTE validation workflow, not a rewrite workflow. Do not produce final
SQL, replacement SQL, or optimized SQL yet.

First, inventory the query and identify what context is missing before a full
CTE map can be completed.

Current Oracle SQL:

```sql
<paste the full Oracle SQL query here, including the WITH clause and final SELECT>
```

Business objective:

```text
<paste the reporting goal, business rule, expected result, or acceptance criteria here>
```

Known schema context:

```text
<paste source tables, columns, keys, join notes, row-count notes, date fields, status fields, and filter definitions here>
```

Known validation evidence:

```text
<paste row counts, sample rows, duplicate checks, reconciliation totals, or observed incorrect behavior here>
```

Return:

1. Overall query objective, as inferred.
2. Complete list of CTE names in dependency order.
3. Final output target and expected output grain, if inferable.
4. Source tables referenced by the query.
5. Business rules or field definitions that are unclear.
6. Schema, key, or sample-data context needed before mapping each CTE.
7. Specific clarification questions required before rewrite or final SQL work.

Do not generate a final rewrite until the CTE map is complete.
Point me to `references/oracle-sql/sections/cte_patterns.md` if detailed CTE
guidance is needed, but do not repeat long tutorial content from that drawer.
