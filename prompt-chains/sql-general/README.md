# General SQL Assistant Prompt Chain

## Use Case

Use this chain as the everyday Oracle SQL entry point for Copilot. It helps the
analyst classify the request, collect missing context, route specialized cases,
and produce a predictable final answer.

Use this chain when the task is not clearly one of the specialized workflows
yet.

## Supported Task Types

- Write new SQL.
- Explain existing SQL.
- Refactor SQL.
- Debug a SQL error.
- Improve query readability.
- Improve query efficiency.
- Map business logic to fields and tables.
- Validate or explain CTE-based SQL.
- Explain, choose, or validate joins.
- Design aggregations and grouped metrics.
- Validate SQL result correctness.
- Diagnose plan-based query tuning needs.

## Routing Guidance

- Use `prompt-chains/sql-efficiency/` when the main goal is faster SQL from a
  business requirement.
- Use `prompt-chains/sql-logic-mapping/` when the main goal is clarifying
  logic, table, and field mappings before implementation.
- Use `prompt-chains/sql-cte-validation/` when correctness depends on mapping,
  validating, explaining, or refactoring CTE stages.
- Use `prompt-chains/sql-joins/` when the task centers on join choice, join
  explanation, row-preservation behavior, or duplicate risk.
- Use `prompt-chains/sql-aggregation/` when the task centers on grouped
  metrics, output grain, `GROUP BY`, `HAVING`, null handling, or aggregation
  validation.
- Use `prompt-chains/sql-result-validation/` when SQL already exists and the
  main question is whether returned results are correct.
- Use `procedures/query_tuner/SKILL.md` or `prompt-chains/query-tuning/` when
  `EXPLAIN PLAN` based tuning, optimizer diagnosis, indexing, or runtime
  evidence is needed.

## Prompt Sequence

1. `01-task-classification.md`: classify the SQL task and route specialized
   cases.
2. `02-context-intake.md`: collect source context and missing details.
3. `03-solution-draft.md`: draft the solution with logic separated from SQL.
4. `04-review-and-refine.md`: review assumptions, correctness, readability,
   and efficiency risks.
5. `05-final-answer-format.md`: produce the final answer in a predictable
   structure.

## Related References

- `references/oracle-sql/sections/oracle_idioms.md`
- `references/oracle-sql/sections/query_tuning.md`

