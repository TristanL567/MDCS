# SQL Logic Mapping Chain - 03 Grain And Join Validation

Continue the SQL logic mapping workflow.

Validate the current logic-map table for output grain and join safety before
any SQL implementation plan is written.

Current logic map:

```text
<paste the current logic-map table here>
```

Schema or relationship notes:

```text
<paste PK/FK notes, table relationship notes, row-count notes, or compressed schema context here>
```

Return:

1. Expected output grain.
2. Grain of each source table, if inferable.
3. Join path between mapped tables.
4. Missing table relationships.
5. Duplicate-producing join risks.
6. Many-to-many join risks.
7. Aggregation or deduplication needed before joins.
8. Clarification questions required before SQL can be written.

Do not write SQL if grain, join path, or many-to-many handling remains unclear.
