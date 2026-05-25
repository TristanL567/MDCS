# SQL Result Validation Prompt Chain

## Use Case

Use this chain when a human analyst needs Edge Copilot to validate that Oracle
SQL results are correct, not merely that the SQL parses or runs.

The workflow is for result correctness review after a query exists or while a
query is being finalized. It forces Copilot to propose checks the analyst can
run locally for output grain, row counts, duplicates, required-field nulls,
aggregate reconciliation, CTE-level counts, join row multiplication, and
date-window boundaries.

Copilot does not have database access. It must propose validation SQL or manual
checks for the analyst to run in the local database environment, then interpret
the analyst-provided evidence.

## Required Local Preparation

- Have the current Oracle SQL ready, including all CTEs, joins, filters, and
  final output columns.
- Prepare the business intent, expected output grain, required fields, key
  dimensions, metric definitions, date-window rules, and acceptance criteria.
- Gather compact schema context for source tables, keys, join columns, date
  fields, required non-null fields, and known one-to-one or one-to-many
  relationships.
- Keep local run results available as the chain progresses, such as row counts,
  duplicate checks, null counts, reconciliation totals, CTE-level counts,
  join-step counts, boundary-date samples, or old-vs-new comparison evidence.

## Prompt Sequence

1. `01-query-and-intent-intake.md`: provide the SQL, business intent, expected
   grain, key dimensions, required fields, metrics, date window, and available
   evidence.
2. `02-logic-and-grain-review.md`: require Copilot to map the result grain,
   logic, required columns, metric definitions, filters, and unresolved
   assumptions before generating checks.
3. `03-row-count-and-duplicate-checks.md`: generate local checks for final
   output grain, row counts by key dimensions, duplicate keys, required-field
   nulls, and date-window boundaries.
4. `04-cte-and-join-checks.md`: generate local checks for CTE-level row counts,
   CTE grain, join row multiplication, unmatched joins, and aggregate
   reconciliation.
5. `05-final-validation-report.md`: convert the analyst-run evidence into a
   final validation report table and decision.

## Related Reference Drawers

- `references/oracle-sql/sections/cte_patterns.md`
- `references/oracle-sql/sections/join_patterns.md`
- `references/oracle-sql/sections/aggregation_patterns.md`

Use these drawers when detailed CTE, join, or aggregation guidance is needed.
Do not duplicate long SQL tutorial content from the drawers in Copilot prompt
responses; use them as local references for designing focused validation
checks.

## Relationship To Existing Flows

- Use `prompt-chains/sql-general/` first when the request is broad or when the
  analyst still needs help classifying, drafting, or explaining the SQL task.
- Use this chain after `sql-general` when the SQL exists and the main question
  is whether the returned results are correct.
- Use `prompt-chains/sql-cte-validation/` when the primary need is detailed CTE
  mapping or CTE refactor review. Use this result-validation chain when the CTE
  checks must roll into final result correctness evidence.
- Use `prompt-chains/sql-joins/` when the primary need is choosing or
  explaining join types. Use this chain when join behavior must be tested for
  dropped rows, duplicated rows, or row multiplication in the final output.
- Use `prompt-chains/sql-aggregation/` when the primary need is metric and
  grouping design. Use this chain when aggregate totals must be reconciled
  against source data or acceptance criteria.
- Use `prompt-chains/query-tuning/` after result correctness is established and
  the main problem is runtime, plan evidence, indexing, or optimizer behavior.
