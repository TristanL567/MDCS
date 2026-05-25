# Join Selection Scenario

## Business Request

An analyst needs a query that lists every active product and shows its latest
approved price if one exists. Products without an approved price should still
appear so the analyst can find missing pricing.

Ask Copilot to choose and explain the correct joins before drafting final SQL.

## Tiny Generic Schema Context

| Table | Important columns | Notes |
| --- | --- | --- |
| `products` | `product_id`, `product_name`, `status`, `category_id` | One row per product. `status = 'ACTIVE'` means the product should be included. |
| `price_history` | `price_id`, `product_id`, `effective_date`, `price_amount`, `approval_status` | Many rows per product over time. Only approved prices qualify. |
| `categories` | `category_id`, `category_name` | One row per category. |

Expected output grain: one row per active product.

Known risk: multiple approved prices per product can create duplicates unless
the latest approved row is selected before joining.

## Expected Chain To Use

Use `prompt-chains/sql-joins/`.

## Expected Copilot Behaviors

- Confirms that active products are row-preserved.
- Chooses a left join from active products to the latest approved price so
  products without approved prices remain in the result.
- Explains why an inner join would drop products without prices.
- Addresses the one-to-many relationship from products to price history.
- Requires a latest-price selection method before the final join, such as a
  ranked subquery or pre-filtered CTE.
- Proposes duplicate checks by `product_id` and unmatched-row checks for
  products with no approved price.

## Unacceptable Copilot Behaviors

- Uses an inner join without noting that missing-price products will be dropped.
- Joins directly to all approved price rows and ignores duplicate risk.
- Applies a right or full join without business justification.
- Moves approved-price filters into a `WHERE` clause in a way that cancels row
  preservation after a left join.
- Claims the join is correct without row-count, duplicate, or unmatched-row
  validation checks.

## Manual Pass/Fail Checklist

| Check | Pass/Fail |
| --- | --- |
| Copilot used or clearly followed the joins chain. |  |
| Copilot stated which table must be row-preserved. |  |
| Copilot selected a left join for optional price data. |  |
| Copilot explained why an inner join would be wrong for this request. |  |
| Copilot addressed latest-approved-price selection before joining. |  |
| Copilot proposed duplicate and unmatched-row checks. |  |
| Copilot avoided private schema details, credentials, and real data. |  |

