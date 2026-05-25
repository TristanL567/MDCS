# SQL Aggregation Chain - 04 Aggregation Edge Cases

Continue the Oracle SQL aggregation workflow.

Review the aggregation design for correctness risks before final SQL is
written.

Current aggregation design:

```text
<paste the output grain, aggregation map, GROUP BY plan, WHERE plan, HAVING plan, and null-handling notes here>
```

Join and row-grain notes:

```text
<paste join paths, PK/FK notes, source table grains, row counts, or duplicate examples here>
```

Return an edge-case review with:

1. Output grain confirmation.
2. Null-handling risks for `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`.
3. `COUNT(*)` versus `COUNT(field)` versus `COUNT DISTINCT field` risks.
4. Conditional aggregation risks, including whether false-case values should be
   `0` or `NULL`.
5. Duplicate amplification risk from joins before aggregation.
6. Pre-aggregation or deduplication needed before joins.
7. Many-to-many join risks that could inflate metrics.
8. `HAVING` versus `WHERE` mistakes to correct.
9. Cases where analytic/window functions are better than grouped aggregation
   because detail rows should remain visible.
10. Validation checks that must be run before accepting the final SQL.

For validation checks, require checks for:

1. Output grain uniqueness.
2. Reconciliation between detail totals and grouped totals where applicable.
3. Null impact, such as non-null counts versus row counts.
4. Distinct-count key validity.
5. Join amplification, such as row counts before and after joins.

Do not write final SQL if any edge-case risk changes the metric definition,
grouping grain, join order, or validation plan.
