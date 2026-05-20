# Query Tuning Chain - 04 Rewrite Request

Continue following `procedures/query_tuner/SKILL.md`.

Using the compressed schema, slow query, and plan evidence already provided,
generate rewrite candidates now.

Return at least two semantically equivalent Oracle SQL alternatives. For each
candidate include:

1. The rewritten SQL.
2. Which plan bottleneck it targets.
3. Why it may improve runtime.
4. Semantic risk checks I must run.
5. Expected plan-level signals if it works.

Keep the response concise and evidence-first. Reference
`references/oracle-sql/sections/oracle_idioms.md` only if an Oracle idiom is
needed for a rewrite.
