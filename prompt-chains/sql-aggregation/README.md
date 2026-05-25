# SQL Aggregation Prompt Chain

## Use Case

Use this chain when a human analyst needs Edge Copilot to design Oracle SQL
aggregations from explicit business metrics, source fields, grouping grain,
filters, `HAVING` rules, null handling, duplicate risk, and validation checks.

The chain is for aggregation design before final SQL. It should define the
output grain and metric map before any grouped query is accepted.

Use this chain for:

- `COUNT`, `COUNT DISTINCT`, `SUM`, `AVG`, `MIN`, and `MAX` metrics.
- Conditional aggregation with `CASE` inside aggregate functions.
- Choosing between `WHERE` and `HAVING`.
- Null handling decisions such as keeping nulls, excluding nulls, or using
  `NVL` only when missing values should behave as zero.
- Avoiding duplicate amplification from joins before aggregation.
- Deciding when analytic/window functions are better than grouped
  aggregation.

## Required Local Preparation

- Gather the business request, metric definitions, acceptance criteria, and
  sample output if available.
- Prepare relevant table names, source fields, relationship notes, keys,
  date windows, and known filters.
- Identify candidate output columns and expected reporting grain, such as one
  row per customer, account, product, day, month, status, or business event.
- Keep row-count notes, duplicate-risk notes, and known null semantics ready.
- Have representative validation checks or reconciliation totals available
  when possible.

## Prompt Sequence

1. `01-aggregation-intake.md`: collect the business request, candidate metrics,
   source context, grain expectations, and blockers.
2. `02-output-grain-map.md`: require Copilot to define output grain and build
   the aggregation map before SQL.
3. `03-group-by-and-having-design.md`: design `GROUP BY`, input filters, and
   `HAVING` rules from the accepted map.
4. `04-aggregation-edge-cases.md`: review null handling, distinct counts,
   conditional aggregation, join duplicate risk, and analytic/window function
   alternatives.
5. `05-final-aggregation-sql.md`: produce final Oracle SQL only after grouped
   result validation checks are defined.

## Related Reference Drawer

- `references/oracle-sql/sections/aggregation_patterns.md`

Open this drawer when detailed aggregation guidance is needed. Do not copy long
SQL tutorial content from the drawer into Copilot prompts; use it as a local
reference for checking the design.

## Relationship To Other SQL Flows

- Use `prompt-chains/sql-general/` when the SQL task is broad or not clearly an
  aggregation-design problem.
- Use this chain after `sql-general` routes a request toward grouped metrics,
  summary reporting, or aggregation validation.
- Use `prompt-chains/query-tuning/` after the aggregation logic is correct and
  the main problem is slow runtime, plan evidence, or rewrite performance.
