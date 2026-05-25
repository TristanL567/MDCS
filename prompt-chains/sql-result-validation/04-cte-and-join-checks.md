# SQL Result Validation Chain - 04 CTE And Join Checks

Continue the Oracle SQL result validation workflow.

Generate focused Oracle SQL or manual checks I can run locally for intermediate
CTEs, joins, and aggregates. Copilot does not have database access, so do not
claim any check passes until I provide results.

Current Oracle SQL:

```sql
<paste the full query with CTEs, joins, filters, aggregations, and final SELECT>
```

Output grain and validation plan:

```text
<paste the accepted output grain and validation plan from prompt 02>
```

Results from prompt 03, if available:

```text
<paste final-output row counts, duplicate counts, null checks, and boundary checks>
```

Known relationship and metric context:

```text
<paste known primary keys, foreign keys, one-to-many relationships, bridge tables, metric definitions, and reconciliation targets>
```

Return validation checks for me to run locally:

1. CTE-level row counts in dependency order.
2. CTE-level grain or duplicate checks for each stage where a key is expected.
3. CTE-level null checks where required fields are introduced or transformed.
4. Filter-impact checks where a CTE applies business filters.
5. Join row multiplication checks:
   - pre-join counts by join key;
   - duplicate join-key counts on each side;
   - post-join counts by join key;
   - unmatched rows for outer joins;
   - many-to-many risk checks.
6. Aggregate reconciliation checks:
   - source total versus final total;
   - source count versus final count;
   - grouped totals by key dimensions;
   - distinct-count checks where duplicate amplification is possible.
7. Expected pass/fail signal for each check.
8. How I should paste local results back for final report assembly.

Point me to `references/oracle-sql/sections/cte_patterns.md` for CTE-stage
validation patterns, `references/oracle-sql/sections/join_patterns.md` for
join-cardinality checks, and
`references/oracle-sql/sections/aggregation_patterns.md` for reconciliation
patterns when relevant. Do not repeat long SQL tutorial content from those
drawers.

Keep all SQL snippets focused on validation evidence, not final rewrites or
performance tuning.
