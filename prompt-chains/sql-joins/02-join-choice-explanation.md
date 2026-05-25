# SQL Joins Chain - 02 Join Choice Explanation

Continue the Oracle SQL join explanation workflow.

Using the relationship intake and any clarifications already provided, choose
the appropriate Oracle SQL join pattern for each table relationship. Do not
produce final SQL yet.

Relationship intake and clarifications:

```text
<paste Copilot's intake response and any answered clarification questions here>
```

Additional schema or business context:

```text
<paste any new keys, row-count notes, sample rows, optional relationship rules, or required filters here>
```

Return one row per relationship using exactly this table shape:

`left table | right table | join type | join keys | cardinality | preserved rows | duplicate risk | validation check`

For each relationship, explain:

1. Why the selected join type matches the business requirement.
2. Which rows are preserved and which rows can be dropped.
3. Whether the relationship is one-to-one, one-to-many, many-to-one, or
   many-to-many.
4. Whether the join can introduce duplicate output rows.
5. The validation check needed before the join can be accepted.

Cover these join patterns when relevant:

1. Inner join when only matching rows should remain.
2. Left join when every row from the left table must remain.
3. Full join when unmatched rows from both sides must remain.
4. Cross join only when every combination is intentional and bounded.
5. Semi join with `EXISTS` when the query needs to test whether a matching row
   exists without multiplying rows.
6. Anti join with `NOT EXISTS` when the query needs rows with no matching
   related row.

After the table, provide generic mini-examples for each join type used. Use
small invented tables with two or three rows and explain which rows are kept,
dropped, or duplicated. Keep the examples generic and short.

Do not approve final SQL until every relationship has a join type, join key,
cardinality statement, preserved-row statement, duplicate-risk statement, and
validation check.

Use `references/oracle-sql/sections/join_patterns.md` only when detailed join
guidance is needed.
