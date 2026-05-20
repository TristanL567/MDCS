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

Also list any secondary task types that apply.

Routing rules:

1. If the main goal is faster SQL from a business requirement, recommend
   switching to `prompt-chains/sql-efficiency/`.
2. If the main goal is clarifying logic, table, and field mappings, recommend
   switching to `prompt-chains/sql-logic-mapping/`.
3. If the task requires `EXPLAIN PLAN` based tuning, recommend
   `procedures/query_tuner/SKILL.md` or `prompt-chains/query-tuning/`.

If the task can stay in this general SQL chain, list the assumptions you are
making and ask only the missing-context questions needed for the next step.
Do not write SQL yet unless the request is trivial and all context is present.

