# SQL Logic Mapping Prompt Chain

## Use Case

Use this chain when a human analyst needs Edge Copilot to turn messy business
logic, reporting notes, or stakeholder language into a precise SQL-ready
implementation plan.

The chain is for mapping and validation before SQL. It should not produce final
SQL until the mapping is complete and unresolved assumptions have been answered.

## Required Local Preparation

- Gather the business request, acceptance criteria, sample output, and any known
  filters or date windows.
- Prepare table names, field names, relationship notes, and compressed schema
  context when available.
- Identify the expected output grain, such as one row per customer, account,
  order, day, month, product, or business event.
- Keep examples of edge cases, exclusions, and known contradictory rules ready.

## Prompt Sequence

1. `01-business-logic-intake.md`: collect business rules and block premature
   SQL generation.
2. `02-field-and-table-mapping.md`: produce the reusable logic-map table.
3. `03-grain-and-join-validation.md`: validate grain, joins, duplicates, and
   many-to-many risks.
4. `04-sql-implementation-plan.md`: convert the completed map into a SQL-ready
   implementation plan.
5. `05-review-for-ambiguity.md`: review the plan for unresolved assumptions and
   clarification questions.

## Related Procedure Closet

- None yet. This chain is a prompt-chain-only workflow.

## Related Reference Drawers

- `references/oracle-sql/sections/oracle_idioms.md`
