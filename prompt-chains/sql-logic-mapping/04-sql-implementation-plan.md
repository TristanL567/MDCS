# SQL Logic Mapping Chain - 04 SQL Implementation Plan

Continue the SQL logic mapping workflow.

Create a SQL-ready implementation plan from the completed logic map. Do not
write final SQL unless every mapping, grain, join, date window, and filter
assumption is resolved.

Completed logic map:

```text
<paste completed logic-map table here>
```

Validated grain and join notes:

```text
<paste grain, join-path, deduplication, aggregation, and clarification answers here>
```

Return:

1. SQL generation readiness: ready or blocked.
2. Required base tables and aliases.
3. Join sequence and join keys.
4. Pre-aggregation or deduplication steps.
5. Filter plan, including date windows.
6. Derived calculation plan.
7. Aggregation and grouping level.
8. Output column plan.
9. Remaining blockers, if any.

If blocked, ask only the clarification questions needed to unblock the plan.
