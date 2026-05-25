# SQL Result Validation Chain - 05 Final Validation Report

Finish the Oracle SQL result validation workflow.

Use the analyst-run evidence to decide whether the result set is validated,
blocked by missing evidence, or likely incorrect. This is result correctness
review, not a syntax-only review. Copilot does not have database access; base
the conclusion only on the evidence I paste below.

Current Oracle SQL or query version reviewed:

```sql
<paste the final SQL version or query identifier here>
```

Business intent and expected output grain:

```text
<paste the accepted business objective, expected grain, key columns, required fields, metrics, and date-window rules>
```

Validation checks Copilot proposed:

```text
<paste checks from prompts 03 and 04, or a summarized check list>
```

Local results from the analyst:

```text
<paste row counts, duplicate checks, null checks, CTE counts, join checks, aggregate reconciliation, date-window boundary results, sample rows, and any manual review notes>
```

Return:

1. Final decision:
   - validated;
   - validated with caveats;
   - blocked by missing evidence;
   - likely incorrect.
2. A validation report table with exactly this shape:

   `check | purpose | SQL/manual step | expected signal | issue if failed`

3. Evidence interpretation for:
   - output grain;
   - row counts by key dimensions;
   - duplicate keys;
   - nulls in required output fields;
   - aggregate reconciliation;
   - CTE-level row counts;
   - join row multiplication;
   - date-window boundaries.
4. Any failed checks, unclear signals, or missing local evidence.
5. Minimal recommended next action for each failure or evidence gap.
6. Whether the query should move to `prompt-chains/query-tuning/` only after
   result correctness is established.

If CTE, join, or aggregation details need deeper review, point me to the
relevant drawer:

- `references/oracle-sql/sections/cte_patterns.md`
- `references/oracle-sql/sections/join_patterns.md`
- `references/oracle-sql/sections/aggregation_patterns.md`

Do not duplicate long SQL tutorial content from those drawers.
