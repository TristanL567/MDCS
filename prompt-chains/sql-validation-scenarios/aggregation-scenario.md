# Aggregation Scenario

## Business Request

An analyst needs a monthly summary by store showing total completed sales,
number of distinct buying customers, average completed sale amount, and the
count of refunded transactions. Only stores with at least 10 completed sales
for the month should appear.

Ask Copilot to design the aggregation before writing final SQL.

## Tiny Generic Schema Context

| Table | Important columns | Notes |
| --- | --- | --- |
| `stores` | `store_id`, `store_name`, `region_code`, `status` | One row per store. |
| `transactions` | `transaction_id`, `store_id`, `customer_id`, `transaction_date`, `transaction_status`, `sale_amount` | Many rows per store. Status can be `COMPLETED`, `REFUNDED`, or `CANCELLED`. |
| `regions` | `region_code`, `region_name` | One row per region. |

Expected output grain: one row per store per calendar month.

Known risk: joining to any one-to-many detail table before aggregation could
inflate sales totals or customer counts.

## Expected Chain To Use

Use `prompt-chains/sql-aggregation/`.

## Expected Copilot Behaviors

- Defines each metric before SQL, including numerator, eligible rows, and null
  handling.
- Confirms output grain as store-month.
- Distinguishes `WHERE` filters from `HAVING` rules, especially the completed
  sales threshold.
- Uses conditional aggregation for refunded transaction counts without mixing
  refunded amounts into completed sales.
- Uses `COUNT(DISTINCT customer_id)` for distinct buying customers if a
  customer can have multiple transactions.
- Proposes reconciliation checks for totals, distinct counts, group counts,
  date boundaries, and duplicate amplification.

## Unacceptable Copilot Behaviors

- Drafts grouped SQL before defining the metric map and output grain.
- Counts all transaction statuses as completed sales.
- Uses `COUNT(customer_id)` where distinct customers are requested.
- Places the 10 completed sales threshold in a row-level `WHERE` filter instead
  of a group-level rule.
- Treats null `sale_amount` values as zero without confirming that business
  rule.
- Claims aggregation correctness without reconciliation checks.

## Manual Pass/Fail Checklist

| Check | Pass/Fail |
| --- | --- |
| Copilot used or clearly followed the aggregation chain. |  |
| Copilot defined output grain before SQL. |  |
| Copilot mapped all requested metrics before SQL. |  |
| Copilot separated completed sales from refunded transactions. |  |
| Copilot used or recommended distinct customer counting. |  |
| Copilot placed the completed-sales threshold at group level. |  |
| Copilot proposed manual reconciliation and duplicate-risk checks. |  |
| Copilot avoided private schema details, credentials, and real data. |  |

