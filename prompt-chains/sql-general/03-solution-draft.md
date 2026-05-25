# General SQL Chain - 03 Solution Draft

Draft the SQL-related solution for the classified task.

Before the SQL or explanation, separate logic from implementation:

1. Restate the business or technical objective.
2. List the source tables and key fields used.
3. List join logic.
4. List filter logic.
5. List aggregation or output-grain logic.
6. List CTE stage logic, result-validation evidence, or plan evidence when
   relevant.
7. List assumptions that remain.

Then produce the draft appropriate to the task:

- For new SQL: provide Oracle SQL and a brief block-by-block explanation.
- For explaining SQL: explain intent, joins, filters, grain, and output.
- For refactoring SQL: provide revised SQL and explain what changed.
- For debugging: identify likely cause, corrected SQL or fix, and test step.
- For readability: provide clearer SQL with stable aliases and comments only
  where useful.

Keep the answer practical. Do not duplicate specialized efficiency or logic
mapping chain content; route there if the task has become specialized. Also
route to the CTE, joins, aggregation, result-validation, or query-tuning chains
when those workflows become the main need.

