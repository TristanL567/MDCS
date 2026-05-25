# SQL Joins Chain - 03 Duplicate Risk Check

Continue the Oracle SQL join explanation workflow.

Before final SQL is accepted, test the completed join map for cardinality and
duplicate risks.

Completed join map:

```text
<paste the join map table from step 02 here>
```

Known row counts, key counts, or sample rows:

```text
<paste table row counts, distinct join-key counts, duplicate counts by key, sample rows, or known unmatched rows here>
```

Return:

1. Expected output grain.
2. Join relationships that appear one-to-one and why.
3. Join relationships that appear one-to-many or many-to-one and how that
   affects output rows.
4. Join relationships that may be many-to-many and why they are risky.
5. Relationships where nullable keys, non-unique keys, date-effective records,
   status filters, or missing predicates could multiply rows.
6. Semi join or anti join opportunities where `EXISTS` or `NOT EXISTS` would
   avoid unnecessary row multiplication.
7. Cross joins that must be removed or explicitly justified as intentional and
   bounded.
8. Exact validation checks to run before final SQL is accepted.

For validation checks, include Oracle SQL snippets or pseudocode for:

1. Counting rows before and after each join.
2. Counting duplicate output keys after each join.
3. Counting distinct join keys on both sides.
4. Finding unmatched rows for outer joins.
5. Detecting many-to-many joins before the final query.

If any relationship can multiply rows beyond the expected output grain, do not
approve final SQL. State whether the next step is to add a missing predicate,
pre-aggregate, deduplicate with a business rule, switch to `EXISTS`, switch to
`NOT EXISTS`, or ask for more context.

Point me to `references/oracle-sql/sections/join_patterns.md` if detailed join
guidance is needed, but do not repeat long tutorial content from that drawer.
