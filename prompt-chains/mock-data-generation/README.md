# Mock Data Generation Prompt Chain

## Use Case

Use this chain when a human analyst needs Edge Copilot to generate schema-valid
synthetic data artifacts from compressed Oracle schema context.

## Required Local Preparation

- Prepare compressed schema context with tables, columns, data types, PKs, FKs,
  nullability, and uniqueness notes where available.
- Decide target row counts, realism rules, date ranges, and domain constraints.
- Choose whether the final artifact should be SQL inserts, a PL/SQL block, a
  Python generator, or CSV files.
- Keep a way to inspect FK integrity and row counts locally before use.

## Prompt Sequence

1. `01-schema-submission.md`: submit compressed schema and generation objective.
2. `02-pk-fk-hierarchy-analysis.md`: derive parent-child load order.
3. `03-output-mode-selection.md`: choose the artifact style and assumptions.
4. `04-data-generation.md`: generate the requested mock-data artifact.
5. `05-integrity-verification.md`: review FK validity, constraints, and realism.

## Related Procedure Closet

- `procedures/mock_data_generator/SKILL.md`

## Related Reference Drawers

- `references/oracle-sql/sections/plsql_basics.md`
- `references/oracle-sql/sections/oracle_idioms.md`
