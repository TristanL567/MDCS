# Query Tuning Chain - 02 Query Context

Continue following `procedures/query_tuner/SKILL.md`.

I am providing the compressed schema context and the slow Oracle SQL query.
Analyze only what can be inferred from this context, then tell me what plan
evidence is still needed before rewrite recommendations.

Compressed schema context:

```text
<paste compressed schema context here>
```

Slow query:

```sql
<paste slow Oracle SQL query here>
```

Observed runtime context:

```text
<paste runtime, bind shape, date window, row-volume notes, or SLA here>
```

Return:

1. A concise restatement of the tuning objective.
2. Relevant tables, joins, predicates, and indexes to watch in the plan.
3. Specific `EXPLAIN PLAN` or execution evidence I should paste next.
4. Any semantic risks that must be preserved during rewrite.
