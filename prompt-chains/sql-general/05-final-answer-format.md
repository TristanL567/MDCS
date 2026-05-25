# General SQL Chain - 05 Final Answer Format

Produce the final answer in this predictable structure:

## Task Restatement

Restate the SQL task and the selected task type.

## Assumptions

List assumptions that remain. If none remain, write `None known`.

## Logic Summary

Summarize source tables, joins, filters, aggregations, and output grain.

## Final SQL Or Explanation

Provide the final Oracle SQL, explanation, refactor, or debug fix requested.

## Validation Checks

List concrete checks the user can run, such as:

1. Row count at expected grain.
2. Duplicate check on output key.
3. Null check for required fields.
4. Boundary checks for dates and filters.
5. Aggregate reconciliation, if relevant.
6. Sample record trace-back to source tables.

## Routing Note

State whether the task is complete in this general chain or should next move
to `sql-efficiency`, `sql-logic-mapping`, `sql-cte-validation`, `sql-joins`,
`sql-aggregation`, `sql-result-validation`, or `query-tuning`.

