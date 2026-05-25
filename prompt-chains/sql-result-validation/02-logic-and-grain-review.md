# SQL Result Validation Chain - 02 Logic And Grain Review

Continue the Oracle SQL result validation workflow.

Use the intake summary to review result logic and output grain before producing
validation SQL. This is not a syntax-only review and not a rewrite request.
Copilot does not have database access; identify checks I should run locally.

Intake summary:

```text
<paste Copilot's intake summary from prompt 01>
```

Current Oracle SQL:

```sql
<paste the current Oracle SQL again if needed>
```

Additional local context or evidence:

```text
<paste answers to missing-context questions, sample rows, row counts, schema notes, or acceptance criteria>
```

Return:

1. Final output grain statement in one sentence.
2. Grain risk review:
   - expected key columns;
   - where the SQL could create more than one row per expected key;
   - where the SQL could collapse rows too early.
3. Logic map from source data to final output:
   - source tables or CTEs;
   - filters;
   - joins;
   - aggregations;
   - derived fields;
   - final output fields.
4. Required-field null risk list.
5. Aggregate reconciliation risk list.
6. Date-window boundary risk list, including inclusive and exclusive boundary
   assumptions.
7. CTE and join stages that need row-count or row-multiplication checks.
8. A validation plan outline, without full SQL yet, grouped into:
   - output grain and duplicate checks;
   - row counts by key dimensions;
   - required-field null checks;
   - aggregate reconciliation checks;
   - CTE-level checks;
   - join row multiplication checks;
   - date-window boundary checks.

If the query uses CTE-heavy logic, point me to
`references/oracle-sql/sections/cte_patterns.md`. If join cardinality is a
major risk, point me to `references/oracle-sql/sections/join_patterns.md`. If
grouped metrics or totals are involved, point me to
`references/oracle-sql/sections/aggregation_patterns.md`. Do not duplicate long
tutorial content from those drawers.
