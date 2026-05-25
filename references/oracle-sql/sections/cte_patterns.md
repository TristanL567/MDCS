relevant-when: Open this drawer when decomposing Oracle SQL query logic with WITH clauses or validating staged transformations.

# Oracle CTE Patterns Reference

## 1. Purpose
Common table expressions (CTEs), also called subquery factoring, make query logic explicit by naming intermediate rowsets before the final `SELECT`.

Use CTEs to:
*   Separate filtering, joining, aggregation, and final presentation steps.
*   Reuse the same derived rowset more than once.
*   Validate row counts and keys at each stage.

```sql
WITH filtered_orders AS (
    SELECT order_id, customer_id, order_date, status
    FROM orders
    WHERE order_date >= DATE '2026-01-01'
),
customer_orders AS (
    SELECT customer_id, COUNT(*) order_count
    FROM filtered_orders
    GROUP BY customer_id
)
SELECT customer_id, order_count
FROM customer_orders
WHERE order_count > 1;
```

## 2. Staged CTEs
Order stages from raw inputs to final business grain. Each CTE should have one clear job.

```sql
WITH base_rows AS (
    SELECT item_id, category_id, amount
    FROM source_items
    WHERE active_flag = 'Y'
),
categorized AS (
    SELECT b.item_id, c.category_name, b.amount
    FROM base_rows b
    JOIN categories c
        ON c.category_id = b.category_id
),
category_totals AS (
    SELECT category_name, SUM(amount) total_amount
    FROM categorized
    GROUP BY category_name
)
SELECT category_name, total_amount
FROM category_totals;
```

## 3. Naming and Dependency Order
Name CTEs for their rowset, not the implementation detail. Later CTEs may reference earlier CTEs; earlier CTEs cannot reference later ones.

Preferred names:
*   `base_orders`
*   `valid_customers`
*   `order_totals`
*   `ranked_results`

Avoid names like:
*   `cte1`
*   `temp`
*   `final2`

## 4. Final-Select Validation
Keep the final `SELECT` small. It should project, filter, and order the already-shaped result, not hide major transformations.

```sql
WITH result_rows AS (
    SELECT customer_id, SUM(amount) total_amount
    FROM orders
    GROUP BY customer_id
)
SELECT customer_id, total_amount
FROM result_rows
WHERE total_amount > 0
ORDER BY total_amount DESC;
```

Validation checks:
```sql
-- Row count at each stage
WITH base_rows AS (...),
joined_rows AS (...),
final_rows AS (...)
SELECT 'base_rows' stage, COUNT(*) row_count FROM base_rows
UNION ALL
SELECT 'joined_rows', COUNT(*) FROM joined_rows
UNION ALL
SELECT 'final_rows', COUNT(*) FROM final_rows;

-- Grain check for expected one row per business key
SELECT business_key, COUNT(*) rows_per_key
FROM final_rows
GROUP BY business_key
HAVING COUNT(*) > 1;
```

## 5. Over-Fragmented CTEs
Too many tiny CTEs can make a query harder to reason about and may obscure optimizer behavior.

Signs of over-fragmentation:
*   A CTE only renames columns and is never reused.
*   Multiple consecutive CTEs each add one simple expression.
*   The reader must jump through many names to understand one filter.

Combine adjacent stages when they share the same grain and purpose. Keep separate stages when row counts, grain, or business meaning changes.
