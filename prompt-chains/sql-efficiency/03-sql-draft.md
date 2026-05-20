# SQL Efficiency Chain - 03 SQL Draft

The logic map is approved. Now draft Oracle SQL from the approved map.

Use Oracle-efficient structures:

1. Apply selective predicates as early as practical.
2. Use explicit joins with clear join conditions.
3. Use CTEs for readable staged logic when they clarify filters,
   deduplication, aggregation, or joins.
4. Avoid unnecessary `DISTINCT`; explain any `DISTINCT` that remains.
5. Avoid functions on indexed filter columns where possible.
6. Keep aggregation grain clear and aligned with the approved output grain.

Return:

1. The SQL draft.
2. A short mapping from each CTE or query block to the approved logic map.
3. Assumptions still present in the SQL.
4. Questions that must be resolved before finalizing, if any.

Do not perform `EXPLAIN PLAN` tuning in this step. If plan evidence is needed,
say that this belongs in the query tuning workflow.

