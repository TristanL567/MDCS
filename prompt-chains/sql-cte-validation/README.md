# SQL CTE Validation Prompt Chain

## Use Case

Use this chain when a human analyst needs Edge Copilot to validate, explain,
or improve Oracle SQL built with common table expressions.

The workflow forces Copilot to map every CTE stage before recommending final
SQL or rewrites. It is best for multi-stage queries where correctness depends
on intermediate grain, joins, filters, derived fields, or dependency order.

## Required Local Preparation

- Have the current Oracle SQL query ready, including the full `WITH` clause and
  final `SELECT`.
- Prepare compact schema context for source tables, key fields, join columns,
  date fields, status fields, and any known row-count expectations.
- Gather business rules, expected output grain, sample rows, and known edge
  cases.
- Keep validation evidence available, such as row counts by CTE, duplicate
  checks, null checks, reconciliation totals, or comparison results from the
  old and revised SQL.

## Prompt Sequence

1. `01-cte-intake.md`: provide the SQL and context, then block rewrites until
   the CTE inventory is complete.
2. `02-cte-logic-map.md`: build the required CTE map covering purpose,
   dependencies, source tables, fields, grain, joins, filters, outputs, and
   checks.
3. `03-stepwise-validation.md`: turn the map into executable stage-level
   validation checks.
4. `04-refactor-review.md`: review possible rewrites only after the map and
   validation checks are complete.
5. `05-final-cte-checklist.md`: perform a final correctness, readability, and
   Oracle SQL safety review before accepting the query.

## Related Reference Drawer

- `references/oracle-sql/sections/cte_patterns.md`

Use the drawer when detailed CTE guidance is needed, such as naming patterns,
dependency ordering, materialization considerations, recursive CTE cautions, or
stage-by-stage validation patterns. Do not duplicate long Oracle SQL tutorial
content in the prompt response.

## Relationship To Existing Flows

- Use `prompt-chains/sql-general/` first when the request is broad, simple, or
  not clearly centered on CTE validation.
- Use this chain after `sql-general` when the task becomes a multi-CTE
  correctness, explanation, or refactor review.
- Use `prompt-chains/query-tuning/` when the primary evidence is `EXPLAIN PLAN`
  output, runtime behavior, indexing, or optimizer diagnosis.
- Use this chain before `query-tuning` when the query must first be proven
  logically correct stage by stage.
