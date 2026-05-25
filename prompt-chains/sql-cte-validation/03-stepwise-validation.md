# SQL CTE Validation Chain - 03 Stepwise Validation

Continue the Oracle SQL CTE validation workflow.

Use the completed CTE map to design stage-by-stage validation checks. Do not
rewrite the query yet.

Completed CTE map:

```text
<paste the completed CTE map table here>
```

Available validation evidence:

```text
<paste row counts, sample rows, expected totals, known edge cases, or old-vs-new comparison evidence here>
```

Return:

1. Validation sequence in CTE dependency order.
2. A row-count check for each CTE.
3. A grain or duplicate check for each CTE.
4. A null, unmatched join, or dropped-row check where relevant.
5. A filter-placement check where a CTE introduces filters.
6. A derived-field check where a CTE creates calculated columns.
7. A reconciliation check between the final output and the business objective.
8. Expected pass/fail signal for each check.

For any check that needs SQL, provide small Oracle SQL snippets that inspect
intermediate stages. Keep snippets focused on validation, not final rewrites.

Flag any CTE that still lacks enough information to validate safely.
Do not generate a final rewrite until the validation sequence covers every CTE.
