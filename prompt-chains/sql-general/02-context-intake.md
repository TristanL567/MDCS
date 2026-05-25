# General SQL Chain - 02 Context Intake

Continue as a senior Oracle SQL assistant.

Restate the task classification from step 1 and list the assumptions currently
in effect.

Collect or confirm the context needed for the chosen task type:

1. Business objective or question.
2. Source tables and aliases.
3. Required fields and output names.
4. Joins and relationship assumptions.
5. Filters, date windows, and bind parameters.
6. Aggregations and expected output grain.
7. CTE names, dependencies, and intermediate grains, if relevant.
8. Existing SQL, error message, result evidence, or `EXPLAIN PLAN`, if this is
   explanation, refactor, debug, validation, or plan-based tuning.
9. Validation checks the answer should satisfy.

Separate known facts from assumptions using this format:

| item | known fact | assumption or question |
| --- | --- | --- |

If the context is still insufficient, ask targeted questions and stop. If the
context is sufficient, say that the next step can draft the solution.

