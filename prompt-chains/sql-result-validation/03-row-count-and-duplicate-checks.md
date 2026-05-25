# SQL Result Validation Chain - 03 Row Count And Duplicate Checks

Continue the Oracle SQL result validation workflow.

Generate focused Oracle SQL or manual checks I can run locally for final-output
correctness. Copilot does not have database access, so do not claim any check
passes until I provide results.

Current query or final-output CTE:

```sql
<paste the current Oracle SQL, or wrap the final query as a CTE named final_result>
```

Accepted output grain and key columns:

```text
<paste expected grain and key columns from prompt 02>
```

Key dimensions for row-count checks:

```text
<paste dimensions such as period, product, status, region, source system, customer type>
```

Required output fields:

```text
<paste fields that should not be null, plus fields where null is acceptable>
```

Date-window rules:

```text
<paste date field, start date, end date, inclusive/exclusive boundary rules, and reporting period logic>
```

Return validation checks for me to run locally:

1. Final output total row count.
2. Row counts by each key dimension and important dimension combinations.
3. Duplicate-key check for the expected output grain.
4. Null checks for all required output fields.
5. Date-window boundary checks:
   - rows before the expected start boundary;
   - rows on the start boundary;
   - rows on the end boundary;
   - rows after the expected end boundary;
   - suspicious time components if date truncation matters.
6. Small sample-row checks for duplicate keys, null required fields, and boundary
   dates.
7. Expected pass/fail signal for each check.
8. How I should paste the local results back for interpretation.

Use small Oracle SQL snippets that inspect the final result. If wrapping the
query in a CTE is useful, use a placeholder like:

```sql
WITH final_result AS (
  <paste current query here>
)
SELECT ...
FROM final_result;
```

Keep the snippets focused on validation, not final rewrites.
