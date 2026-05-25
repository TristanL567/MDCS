# SQL CTE Validation Chain - 04 Refactor Review

Continue the Oracle SQL CTE validation workflow.

Only review refactor or rewrite options if the CTE map is complete and the
stagewise validation checks have been defined.

Completed CTE map:

```text
<paste the completed CTE map table here>
```

Stepwise validation plan and results:

```text
<paste validation checks and any observed results here>
```

Refactor goal:

```text
<paste the goal: readability, safer CTE names, removing repeated logic, reducing grain risk, preparing for tuning, or preserving behavior while improving maintainability>
```

Return:

1. Whether the query is ready for refactor review.
2. Any CTEs that must not be changed until more validation evidence exists.
3. Safe readability improvements, such as clearer CTE names, alias cleanup, or
   separating mixed-grain logic.
4. Logic-preserving rewrite candidates, if safe.
5. For each candidate, the CTE stages affected and why behavior should remain
   equivalent.
6. Validation checks that must be rerun after each candidate.
7. Risks that could change row grain, filter scope, join behavior, or output
   fields.

If the CTE map is incomplete, stop and list the missing map fields instead of
producing rewritten SQL.
If detailed CTE guidance is needed, point to
`references/oracle-sql/sections/cte_patterns.md` without duplicating long
tutorial content.
