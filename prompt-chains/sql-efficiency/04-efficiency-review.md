# SQL Efficiency Chain - 04 Efficiency Review

Review the SQL draft for correctness and avoidable inefficiency before final
delivery.

Use this review checklist:

1. Business objective still matches the approved logic map.
2. Source tables and joins match the approved source mapping.
3. Filters are selective and applied at the right stage.
4. Indexed filter columns are not wrapped in avoidable functions.
5. Aggregation grain is explicit and does not multiply rows.
6. `DISTINCT` is absent or justified by a specific duplicate source.
7. CTEs improve staged readability without hiding unnecessary scans.
8. Output fields are named clearly and trace back to business rules.
9. Validation checks can prove row count, totals, duplicates, and date bounds.

Return:

1. Issues found, ordered by severity.
2. Revised SQL if changes are needed.
3. Remaining risks or assumptions.
4. Whether the query is ready for final packaging.

Do not ask for `EXPLAIN PLAN` unless I am switching to the query tuning
workflow.

