# Query Tuning Chain - 03 Explain Plan

Continue following `procedures/query_tuner/SKILL.md`.

I am providing the plan evidence for the current slow query. Use
`references/oracle-sql/sections/query_tuning.md` as the relevant drawer, but do
not repeat the drawer content back to me.

Plan output:

```text
<paste EXPLAIN PLAN or DBMS_XPLAN output here>
```

Additional evidence:

```text
<paste estimated vs actual row notes, bind values, waits, timing runs, or known indexes here>
```

Return:

1. The top bottlenecks, tied directly to plan operations.
2. The likely causes, with confidence level and assumptions.
3. Candidate optimization levers to test.
4. The minimum context still needed before generating rewrites.
