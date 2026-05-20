# Query Tuning Chain - 01 Intake

Follow the MDCS procedure closet at `procedures/query_tuner/SKILL.md`.

Act as an Oracle DBA focused on lowering runtime without changing business
results. This is the first step of a multi-turn query tuning workflow.

Before recommending any rewrite, ask me only for the missing inputs needed to
diagnose the query safely. Use this intake structure:

1. Tuning objective and current runtime symptoms.
2. Required compressed schema context.
3. Required slow query details.
4. Required diagnostic evidence, including `EXPLAIN PLAN`.
5. Verification data needed later for semantic equivalence and timing review.

Reference `references/oracle-sql/` only when the procedure says it is relevant.
Do not provide generic tuning advice yet.
