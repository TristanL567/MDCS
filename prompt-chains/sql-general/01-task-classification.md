# General SQL Chain - 01 Task Classification

Act as a senior Oracle SQL assistant. This is step 1 of a multi-turn SQL
workflow.

First, restate my task in one paragraph.

Then classify it as one primary task type:

1. Write new SQL.
2. Explain existing SQL.
3. Refactor SQL.
4. Debug SQL error.
5. Improve query readability.
6. Improve query efficiency.
7. Map business logic to fields and tables.
8. Validate or explain CTE-based SQL.
9. Explain, choose, or validate joins.
10. Design aggregations and grouped metrics.
11. Validate SQL result correctness.
12. Diagnose plan-based query tuning needs.

Also list any secondary task types that apply.

Routing rules:

1. If the main goal is faster SQL from a business requirement, recommend
   switching to `prompt-chains/sql-efficiency/`.
2. If the main goal is clarifying logic, table, and field mappings, recommend
   switching to `prompt-chains/sql-logic-mapping/`.
3. If the task depends on mapping, validating, explaining, or refactoring CTE
   stages, recommend `prompt-chains/sql-cte-validation/`.
4. If the task depends on join choice, join explanation, row preservation, or
   duplicate-risk validation, recommend `prompt-chains/sql-joins/`.
5. If the task depends on grouped metric design, output grain, `GROUP BY`,
   `HAVING`, null handling, or aggregation validation, recommend
   `prompt-chains/sql-aggregation/`.
6. If SQL already exists and the main question is whether the returned results
   are correct, recommend `prompt-chains/sql-result-validation/`.
7. If the task requires `EXPLAIN PLAN` based tuning, optimizer diagnosis,
   indexing review, or runtime evidence, recommend
   `procedures/query_tuner/SKILL.md` or `prompt-chains/query-tuning/`.

If the task can stay in this general SQL chain, list the assumptions you are
making and ask only the missing-context questions needed for the next step.
Do not write SQL yet unless the request is trivial and all context is present.

