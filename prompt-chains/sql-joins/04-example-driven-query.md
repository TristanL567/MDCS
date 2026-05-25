# SQL Joins Chain - 04 Example-Driven Query

Continue the Oracle SQL join explanation workflow.

Draft Oracle SQL only after the join map and duplicate-risk checks are
complete. The SQL must preserve the approved output grain and row-preservation
behavior.

Approved join map:

```text
<paste the completed join map table here>
```

Duplicate and cardinality review:

```text
<paste Copilot's duplicate-risk findings and required mitigations here>
```

Query requirements:

```text
<paste selected columns, filters, grouping, ordering, bind variables, and final output requirements here>
```

Return:

1. The proposed Oracle SQL.
2. A short explanation of each join in query order.
3. For each join, a generic mini-example showing how rows are kept, dropped,
   preserved, or multiplied.
4. Any `EXISTS` semi join or `NOT EXISTS` anti join explanation, including why
   it avoids row multiplication.
5. Any cross join explanation, including why every combination is intentional
   and bounded.
6. Any duplicate-risk mitigation used in the SQL, such as pre-aggregation,
   deduplication by a business rule, or a more specific join predicate.
7. Validation queries or checks that must be run before accepting the SQL.

Do not hide uncertainty. If the approved join map is incomplete, or if the
duplicate-risk review found unresolved one-to-many or many-to-many risks, stop
and list the missing checks instead of producing final SQL.

Use `references/oracle-sql/sections/join_patterns.md` only when detailed join
guidance is needed.
