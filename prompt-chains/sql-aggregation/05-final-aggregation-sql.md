# SQL Aggregation Chain - 05 Final Aggregation SQL

Continue the Oracle SQL aggregation workflow.

Write final Oracle SQL only if the output grain, aggregation map, `GROUP BY`
fields, `WHERE` filters, `HAVING` rules, null handling, duplicate-risk handling,
and validation checks have all been defined.

Approved aggregation design:

```text
<paste the accepted output grain, completed aggregation map, GROUP BY plan, HAVING plan, edge-case review, and validation plan here>
```

Return:

1. Readiness status: ready or blocked.
2. If blocked, list only the missing decisions and do not write SQL.
3. If ready, write the final Oracle SQL.
4. After the SQL, list each metric and how it maps back to the approved
   aggregation map.
5. List the grouped-result validation checks that must pass before the SQL is
   accepted.
6. List any assumptions that remain and the risk of each assumption.

Final SQL requirements:

1. Preserve the approved output grain.
2. Include only grouped fields and aggregate expressions in the grouped
   `SELECT`.
3. Put input-row filters in `WHERE`.
4. Put aggregate group filters in `HAVING`.
5. Handle nulls exactly as approved.
6. Prevent duplicate amplification using the approved pre-aggregation,
   deduplication, or join sequence.
7. Use analytic/window functions instead of grouped aggregation only when the
   approved design says detail rows must remain visible.
8. Use clear aliases for output fields.

Do not accept the final SQL unless validation checks for grouped results are
included with it.
