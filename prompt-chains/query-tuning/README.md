# Query Tuning Prompt Chain

## Use Case

Use this chain when a human analyst needs Edge Copilot to diagnose a slow
Oracle SQL query, interpret plan evidence, propose safe rewrites, and review
timing or equivalence results.

## Required Local Preparation

- Prepare compressed schema context with relevant tables, row counts, keys,
  indexes, predicates, and join columns.
- Have the original slow query and observed runtime context ready.
- Capture `EXPLAIN PLAN` output before asking for rewrites.
- Keep representative bind values, row counts, and timing notes available for
  verification.

## Prompt Sequence

1. `01-intake.md`: establish task scope and ask Copilot what context it needs.
2. `02-query-context.md`: submit compressed schema context and the slow query.
3. `03-explain-plan.md`: submit plan output and ask for evidence-based
   bottleneck analysis.
4. `04-rewrite-request.md`: ask for semantically safe rewrite candidates.
5. `05-verification-review.md`: submit timing and equivalence results for
   review.

## Related Procedure Closet

- `procedures/query_tuner/SKILL.md`

## Related Reference Drawers

- `references/oracle-sql/sections/query_tuning.md`
- `references/oracle-sql/sections/oracle_idioms.md`
