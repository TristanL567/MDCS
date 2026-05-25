# SQL CTE Validation Chain - 02 CTE Logic Map

Continue the Oracle SQL CTE validation workflow.

Using the query and context already provided, build a complete CTE map before
any rewrite, optimization, or final SQL recommendation.

Current CTE inventory and clarifications:

```text
<paste Copilot's CTE inventory and any answered clarification questions here>
```

Additional schema or business context:

```text
<paste any new table definitions, field meanings, keys, sample rows, or business rules here>
```

Return one row per CTE using exactly this table shape:

`cte | purpose | source tables | input fields | joins/filters | output grain | output fields | validation check`

For each CTE, identify:

1. The CTE name and its purpose.
2. Dependencies on earlier CTEs.
3. Source tables and source CTEs used.
4. Input fields used from each source.
5. Joins and filters introduced at that stage.
6. Output row grain at that stage.
7. Output fields produced by that stage, including derived fields.
8. Validation check proving the stage behaves as intended.

After the table, return:

1. Dependency order from earliest source stage to final output.
2. Any missing source fields or unresolved aliases.
3. Grain changes between stages.
4. Filters or joins whose placement could change results.
5. CTEs that cannot yet be validated and why.

Do not generate a final rewrite until every CTE has a complete purpose,
dependency, source-field, output-field, grain, join/filter, and validation-check
entry.
Use `references/oracle-sql/sections/cte_patterns.md` only when detailed CTE
guidance is needed.
