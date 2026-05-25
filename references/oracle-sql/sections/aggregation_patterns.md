relevant-when: Open this drawer when summarizing Oracle SQL rows with grouped aggregates or validating metric grain.

# Oracle Aggregation Patterns Reference

## 1. Aggregate Functions
Aggregate functions summarize multiple input rows.

Common functions:
*   `COUNT(*)` counts rows.
*   `COUNT(column_name)` counts non-null values.
*   `SUM`, `AVG`, `MIN`, and `MAX` ignore null inputs.
*   `COUNT(DISTINCT column_name)` counts distinct non-null values.

```sql
SELECT
    COUNT(*) row_count,
    COUNT(amount) non_null_amounts,
    SUM(amount) total_amount,
    AVG(amount) avg_amount
FROM transactions;
```

## 2. GROUP BY and Output Grain
`GROUP BY` defines the output grain. Every selected non-aggregate expression must be grouped.

```sql
SELECT customer_id, status, SUM(amount) total_amount
FROM orders
GROUP BY customer_id, status;
```

Output grain: one row per `customer_id` and `status`.

Validation:
```sql
SELECT customer_id, status, COUNT(*) rows_per_group
FROM orders
GROUP BY customer_id, status;
```

## 3. HAVING
Use `WHERE` to filter input rows before aggregation. Use `HAVING` to filter aggregate groups after aggregation.

```sql
SELECT customer_id, SUM(amount) total_amount
FROM orders
WHERE status = 'COMPLETE'
GROUP BY customer_id
HAVING SUM(amount) > 1000;
```

## 4. Conditional Aggregation
Use `CASE` inside aggregate functions to compute multiple metrics at the same grain.

```sql
SELECT
    customer_id,
    COUNT(*) order_count,
    SUM(CASE WHEN status = 'COMPLETE' THEN 1 ELSE 0 END) complete_orders,
    SUM(CASE WHEN status = 'CANCELLED' THEN amount ELSE 0 END) cancelled_amount
FROM orders
GROUP BY customer_id;
```

For counts, make the returned value explicit. `SUM(CASE ... THEN 1 ELSE 0 END)` avoids ambiguity around nulls.

## 5. Distinct Counts
Distinct counts can be expensive and may hide grain problems. Validate the intended key first.

```sql
SELECT
    customer_id,
    COUNT(DISTINCT order_id) distinct_orders
FROM order_lines
GROUP BY customer_id;

-- Check whether detail rows duplicate the order key
SELECT order_id, COUNT(*) line_count
FROM order_lines
GROUP BY order_id
HAVING COUNT(*) > 1;
```

## 6. Null Handling
Aggregates generally ignore null inputs except `COUNT(*)`.

```sql
SELECT
    SUM(NVL(amount, 0)) total_amount_zero_filled,
    COUNT(amount) amount_present_count,
    COUNT(*) row_count
FROM transactions;
```

Use `NVL` only when missing values should behave as zero. Keep nulls when missing and zero have different meanings.

## 7. Analytic Functions Instead of Grouped Aggregation
Use analytic/window functions when detail rows must remain visible. Grouped aggregation collapses rows.

```sql
SELECT
    order_id,
    customer_id,
    amount,
    SUM(amount) OVER (PARTITION BY customer_id) customer_total
FROM orders;
```

Choose grouped aggregation for one output row per group. Choose analytic functions for group metrics attached to each detail row.

## 8. Validation Checks
Check grain, metric totals, and null effects.

```sql
-- Confirm output grain
WITH grouped_rows AS (
    SELECT customer_id, SUM(amount) total_amount
    FROM orders
    GROUP BY customer_id
)
SELECT customer_id, COUNT(*) rows_per_customer
FROM grouped_rows
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- Reconcile detail and grouped totals
WITH grouped_rows AS (
    SELECT customer_id, SUM(amount) total_amount
    FROM orders
    GROUP BY customer_id
)
SELECT
    (SELECT SUM(amount) FROM orders) detail_total,
    (SELECT SUM(total_amount) FROM grouped_rows) grouped_total
FROM dual;
```
