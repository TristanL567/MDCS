# SQL Efficiency Prompt Chain

## Use Case

Use this chain when a human analyst needs Copilot to turn a business
requirement into efficient Oracle SQL. The chain makes Copilot map business
logic first, then draft SQL only after the mapping is approved.

This is not an `EXPLAIN PLAN` tuning workflow. Use
`procedures/query_tuner/SKILL.md` when a slow query already exists and plan
evidence is available.

## Required Local Preparation

- Business objective and expected output grain.
- Candidate source tables and any known join keys.
- Required output fields, filters, aggregations, and date windows.
- Any known row-volume, partition, indexing, or performance constraints.
- Validation checks that prove the SQL matches the business requirement.

## Prompt Sequence

1. `01-requirement-intake.md`: restate objective, tables, fields, joins,
   filters, aggregations, and output grain.
2. `02-logic-map.md`: produce the required business-rule logic map table.
3. `03-sql-draft.md`: draft Oracle SQL only after the logic map is approved.
4. `04-efficiency-review.md`: review the draft for avoidable inefficiency.
5. `05-final-query-and-checks.md`: produce final SQL, efficiency explanation,
   and validation checklist.

## Related Procedure Closet

- `procedures/query_tuner/SKILL.md` for separate plan-based tuning workflows.

## Related Reference Drawers

- `references/oracle-sql/sections/oracle_idioms.md`
- `references/oracle-sql/sections/query_tuning.md`

