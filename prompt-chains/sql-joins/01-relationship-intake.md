# SQL Joins Chain - 01 Relationship Intake

Act as a senior Oracle SQL assistant focused on join correctness.

This is a join explanation and validation workflow, not a final SQL workflow
yet. Do not produce final SQL until the relationship map, join choices,
cardinality risks, duplicate checks, and row-preservation checks are complete.

Business objective:

```text
<paste the reporting question, business rule, expected result, or acceptance criteria here>
```

Candidate tables and fields:

```text
<paste table names, aliases, relevant columns, primary keys, foreign keys, natural keys, nullable join columns, status/date fields, and filters here>
```

Expected output:

```text
<paste expected output grain, required columns, rows that must be preserved, rows that may be excluded, and any known row-count expectations here>
```

Known sample rows or validation evidence:

```text
<paste sample rows, table row counts, distinct key counts, duplicate checks, unmatched-row checks, or reconciliation totals here>
```

Return:

1. Restated business objective.
2. Expected output grain and row-preservation requirement, if inferable.
3. Candidate left-side and right-side tables for each relationship.
4. Known join keys and missing join keys.
5. Known or likely cardinality for each relationship: one-to-one,
   one-to-many, many-to-one, or many-to-many.
6. Nullable keys, optional relationships, or filters that could affect row
   preservation.
7. Missing schema, key, sample-row, or validation context needed before join
   types can be accepted.
8. Specific clarification questions required before writing final SQL.

Point me to `references/oracle-sql/sections/join_patterns.md` if detailed join
guidance is needed. Do not repeat long tutorial content from that drawer.
