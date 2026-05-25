# SQL CTE Validation Chain - 05 Final CTE Checklist

Continue the Oracle SQL CTE validation workflow.

Use this final checklist before accepting a CTE-based Oracle SQL query or
rewrite.

Final or proposed Oracle SQL:

```sql
<paste the final or proposed Oracle SQL here>
```

Completed CTE map:

```text
<paste the completed CTE map table here>
```

Validation results:

```text
<paste row counts, duplicate checks, reconciliation totals, sample-output checks, or old-vs-new comparison results here>
```

Return:

1. Final list of CTEs in dependency order.
2. Confirmation that every CTE has a stated purpose.
3. Confirmation that every CTE lists source tables or source CTEs.
4. Confirmation that every CTE lists input fields and output fields.
5. Confirmation that every CTE has an output grain.
6. Confirmation that joins and filters introduced at each stage are documented.
7. Confirmation that each CTE has a validation check and observed result.
8. Any remaining correctness risks.
9. Any remaining readability or maintainability risks.
10. Whether the final SQL can be accepted as validated.

If any CTE is missing purpose, dependencies, source tables, input fields,
joins/filters, output grain, output fields, or validation evidence, do not
approve the final SQL. List the missing items and the next check to run.
