# SQL Joins Prompt Chain

## Use Case

Use this chain when a human analyst needs Edge Copilot to explain and choose
Oracle SQL joins before final SQL is accepted.

The workflow forces Copilot to map table relationships, state row-preservation
behavior, identify cardinality and duplicate risks, produce small generic row
examples, and validate the final join logic.

Use this chain for queries where correctness depends on choosing between inner
joins, left joins, full joins, cross joins, semi joins with `EXISTS`, or anti
joins with `NOT EXISTS`.

## Required Local Preparation

- Have the business question, expected output grain, and required row
  preservation behavior ready.
- Prepare compact schema context for relevant tables, primary keys, foreign
  keys, natural keys, nullable join columns, filter columns, and known
  one-to-one, one-to-many, or many-to-many relationships.
- Gather representative sample rows or row-count expectations for the tables
  being joined.
- Keep validation evidence available, such as pre-join row counts, post-join
  row counts, duplicate checks by output key, unmatched-row checks, or
  reconciliation totals.

## Prompt Sequence

1. `01-relationship-intake.md`: collect the business objective, candidate
   tables, expected output grain, join keys, and missing relationship context.
2. `02-join-choice-explanation.md`: require Copilot to choose and explain join
   types with row-preservation mini-examples.
3. `03-duplicate-risk-check.md`: force cardinality, many-to-many, and duplicate
   risk checks before SQL is accepted.
4. `04-example-driven-query.md`: draft Oracle SQL from the approved join map
   and explain how each join keeps or drops rows.
5. `05-final-join-validation.md`: validate row preservation, duplicate checks,
   and cardinality assumptions before accepting final SQL.

## Related Reference Drawer

- `references/oracle-sql/sections/join_patterns.md`

Use the drawer when detailed join guidance is needed, such as Oracle join
syntax, join pattern selection, semi and anti join patterns, row-preservation
rules, or duplicate-risk examples. Do not duplicate long SQL tutorial content
from the drawer in prompt responses.

## Relationship To Existing Flows

- Use `prompt-chains/sql-general/` first when the SQL request is broad, simple,
  or not clearly centered on join behavior.
- Use this chain after `sql-general` when the task depends on explaining table
  relationships, choosing join types, or proving row-preservation behavior.
- Use `prompt-chains/query-tuning/` when the primary problem is runtime,
  indexing, optimizer behavior, or `EXPLAIN PLAN` evidence.
- Use this chain before `query-tuning` when a slow join query must first be
  proven logically correct.
