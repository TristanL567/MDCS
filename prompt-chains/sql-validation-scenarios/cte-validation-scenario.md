# CTE Validation Scenario

## Business Request

An analyst has a multi-CTE Oracle SQL query that produces one row per active
customer for the current month. The query first filters customers, then
summarizes monthly orders, then joins the summary to customer attributes.

Ask Copilot to validate whether the CTE stages are logically correct before any
rewrite is suggested.

## Tiny Generic Schema Context

| Table | Important columns | Notes |
| --- | --- | --- |
| `customers` | `customer_id`, `status`, `signup_date`, `region_code` | One row per customer. `status = 'ACTIVE'` means the customer is active. |
| `orders` | `order_id`, `customer_id`, `order_date`, `order_status`, `order_amount` | Many rows per customer. Cancelled orders should not count. |
| `regions` | `region_code`, `region_name` | One row per region code. |

Expected output grain: one row per active customer with current-month order
count, current-month order amount, and region name.

Known risk: joining `orders` before aggregation may duplicate customer rows.

## Expected Chain To Use

Use `prompt-chains/sql-cte-validation/`.

## Expected Copilot Behaviors

- Builds an inventory of every CTE before proposing any rewrite.
- States each CTE's purpose, source tables, dependencies, output fields, and
  expected grain.
- Identifies where filters belong, especially active-customer status, current
  month date boundaries, and cancelled-order exclusion.
- Proposes stage-level validation checks such as row counts, duplicate checks
  by `customer_id`, current-month boundary checks, and null checks for region.
- Separates correctness validation from performance or style recommendations.
- Asks for the actual SQL if it has not been provided, instead of inventing a
  full query.

## Unacceptable Copilot Behaviors

- Immediately rewrites the SQL before mapping CTE stages.
- Assumes private table names, hidden columns, database credentials, or actual
  production row counts.
- Treats the final output as validated without analyst-run evidence.
- Ignores output grain or duplicate risk from the orders relationship.
- Collapses the CTEs into one query without explaining whether stage-level
  validation is preserved.

## Manual Pass/Fail Checklist

| Check | Pass/Fail |
| --- | --- |
| Copilot used or clearly followed the CTE validation chain. |  |
| Copilot created a CTE-stage map before rewrite advice. |  |
| Copilot stated expected grain for each stage and the final output. |  |
| Copilot identified duplicate risk from many orders per customer. |  |
| Copilot proposed manual validation checks the analyst could run locally. |  |
| Copilot did not claim database validation without evidence. |  |
| Copilot did not invent non-generic schema details or real data. |  |

