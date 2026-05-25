# Prompt Chains

Prompt chains are copy-paste sequences for multi-turn Edge Copilot workflows.
They sit above MDCS procedure closets and reference drawers:

- **Prompt chains** orchestrate a sequence of Copilot prompts for a human
  analyst.
- **Procedure closets** define the workflow, output contract, and verification
  expectations for a task.
- **Reference drawers** hold dense Oracle SQL, Python, pandas, and openpyxl
  knowledge that should be consulted only when relevant.

This preserves progressive disclosure: a chain should tell the analyst which
prompt to paste next, which closet governs the workflow, and which drawers may
be relevant. It should not duplicate the detailed content from those closets or
drawers.

## Chain Contract

Each chain lives under:

```text
prompt-chains/<chain-name>/
```

Each chain directory must contain:

- `README.md`: describes the chain purpose, expected inputs, prompt sequence,
  related procedure closets, and related reference drawers.
- Numbered prompt files, for example:

```text
prompt-chains/<chain-name>/
  README.md
  01-intake.md
  02-analysis.md
  03-output.md
```

Each prompt file must be copy-paste ready for web Copilot. The analyst should
be able to paste the file as a standalone prompt, add the requested local
context, and continue the sequence.

Prompt files must reference existing procedure closets under `procedures/` and
reference drawers under `references/` rather than copying their detailed SQL,
Python, pandas, or openpyxl guidance.

## Index

| id | use case | prompt sequence | related closet | related references |
| --- | --- | --- | --- | --- |
| `sql-general` | General Oracle SQL entry point for writing, explaining, refactoring, debugging, readability, efficiency routing, and logic mapping. | `01-task-classification.md` -> `02-context-intake.md` -> `03-solution-draft.md` -> `04-review-and-refine.md` -> `05-final-answer-format.md` | none | `references/oracle-sql/` |
| `sql-cte-validation` | Validate, explain, or improve Oracle SQL built with CTE stages before accepting final SQL or rewrites. | `01-cte-intake.md` -> `02-cte-logic-map.md` -> `03-stepwise-validation.md` -> `04-refactor-review.md` -> `05-final-cte-checklist.md` | none | `references/oracle-sql/sections/cte_patterns.md` |
| `sql-joins` | Explain, choose, and validate Oracle SQL join behavior, row preservation, and duplicate risk. | `01-relationship-intake.md` -> `02-join-choice-explanation.md` -> `03-duplicate-risk-check.md` -> `04-example-driven-query.md` -> `05-final-join-validation.md` | none | `references/oracle-sql/sections/join_patterns.md` |
| `sql-aggregation` | Design grouped metrics, output grain, filters, `HAVING` rules, null handling, and aggregation validation checks. | `01-aggregation-intake.md` -> `02-output-grain-map.md` -> `03-group-by-and-having-design.md` -> `04-aggregation-edge-cases.md` -> `05-final-aggregation-sql.md` | none | `references/oracle-sql/sections/aggregation_patterns.md` |
| `sql-result-validation` | Validate existing Oracle SQL results for grain, row counts, duplicates, nulls, reconciliations, CTEs, joins, and date boundaries. | `01-query-and-intent-intake.md` -> `02-logic-and-grain-review.md` -> `03-row-count-and-duplicate-checks.md` -> `04-cte-and-join-checks.md` -> `05-final-validation-report.md` | none | `references/oracle-sql/sections/cte_patterns.md`, `references/oracle-sql/sections/join_patterns.md`, `references/oracle-sql/sections/aggregation_patterns.md` |
| `query-tuning` | Diagnose and rewrite a slow Oracle SQL query with plan evidence. | `01-intake.md` -> `02-query-context.md` -> `03-explain-plan.md` -> `04-rewrite-request.md` -> `05-verification-review.md` | `procedures/query_tuner/SKILL.md` | `references/oracle-sql/` |
| `report-generation` | Generate a Python Oracle-to-pandas-to-Excel report script. | `01-requirements-intake.md` -> `02-sql-schema-submission.md` -> `03-python-etl-generation.md` -> `04-excel-formatting-generation.md` -> `05-script-review-verification.md` | `procedures/report_generator/SKILL.md` | `references/python-idioms/` |
| `mock-data-generation` | Generate schema-valid synthetic data artifacts from compressed Oracle schema context. | `01-schema-submission.md` -> `02-pk-fk-hierarchy-analysis.md` -> `03-output-mode-selection.md` -> `04-data-generation.md` -> `05-integrity-verification.md` | `procedures/mock_data_generator/SKILL.md` | `references/oracle-sql/` |
