# SQL Joins Chain - 05 Final Join Validation

Continue the Oracle SQL join explanation workflow.

Use this final checklist before accepting an Oracle SQL query whose correctness
depends on join choices.

Final or proposed Oracle SQL:

```sql
<paste the final or proposed Oracle SQL here>
```

Completed join map:

```text
<paste the completed join map table here>
```

Validation results:

```text
<paste row counts, duplicate checks, distinct key counts, unmatched-row checks, sample-output checks, reconciliation totals, or old-vs-new comparison results here>
```

Return:

1. Whether the final SQL matches the completed join map.
2. Confirmation that every join has stated left table, right table, join type,
   join keys, cardinality, preserved rows, duplicate risk, and validation
   check.
3. Confirmation that inner joins drop only rows the business logic allows to be
   dropped.
4. Confirmation that left joins preserve all required left-side rows.
5. Confirmation that full joins preserve required unmatched rows from both
   sides.
6. Confirmation that cross joins are intentional, bounded, and not accidental.
7. Confirmation that `EXISTS` semi joins are used where existence checks should
   not multiply rows.
8. Confirmation that `NOT EXISTS` anti joins are used where missing related
   rows are required.
9. Confirmation that one-to-one, one-to-many, many-to-one, and many-to-many
   assumptions have validation evidence.
10. Confirmation that duplicate and cardinality checks were run before final
   SQL acceptance.
11. Remaining correctness risks, if any.
12. Whether the final SQL can be accepted as validated.

If any join is missing cardinality evidence, duplicate checks, row-preservation
checks, or unresolved many-to-many risk handling, do not approve the final SQL.
List the missing item and the next validation check to run.

Point me to `references/oracle-sql/sections/join_patterns.md` if detailed join
guidance is needed, but do not repeat long tutorial content from that drawer.
