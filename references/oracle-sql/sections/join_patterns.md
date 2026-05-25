relevant-when: Open this drawer when choosing Oracle SQL join types, checking row preservation, or diagnosing duplicate rows after joins.

# Oracle Join Patterns Reference

## 1. Inner Join
Returns only rows with matching keys on both sides.

```sql
SELECT o.order_id, c.customer_name
FROM orders o
JOIN customers c
    ON c.customer_id = o.customer_id;
```

Expected behavior: orders without a matching customer are removed; customers without orders are not returned.

## 2. Left Outer Join
Preserves all rows from the left rowset and returns `NULL` for missing right-side matches.

```sql
SELECT c.customer_id, o.order_id
FROM customers c
LEFT JOIN orders o
    ON o.customer_id = c.customer_id;
```

Expected behavior: every customer appears at least once. Customers with no orders have `NULL` order columns.

## 3. Right Outer Join
Preserves all rows from the right rowset. Prefer rewriting as a `LEFT JOIN` when it improves readability.

```sql
SELECT c.customer_id, o.order_id
FROM orders o
RIGHT JOIN customers c
    ON c.customer_id = o.customer_id;
```

Expected behavior: equivalent row preservation to the left join above.

## 4. Full Outer Join
Preserves unmatched rows from both sides.

```sql
SELECT a.account_id, b.balance_id
FROM accounts a
FULL OUTER JOIN balances b
    ON b.account_id = a.account_id;
```

Expected behavior: matched accounts share one row; unmatched accounts or balances appear with `NULL` columns from the missing side.

## 5. Cross Join
Returns the Cartesian product of both rowsets. Use only when every combination is intended.

```sql
SELECT d.calendar_date, p.product_id
FROM calendar_days d
CROSS JOIN products p;
```

Expected behavior: result rows equal `COUNT(calendar_days) * COUNT(products)`.

## 6. Semi Join
Returns rows from the left rowset when a match exists, without duplicating left rows due to multiple right-side matches. In Oracle SQL, express this with `EXISTS` or `IN`.

```sql
SELECT c.customer_id
FROM customers c
WHERE EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

Expected behavior: each qualifying customer appears once if `customers.customer_id` is unique.

## 7. Anti Join
Returns rows from the left rowset when no match exists. In Oracle SQL, prefer `NOT EXISTS` because it avoids `NULL` pitfalls from `NOT IN`.

```sql
SELECT c.customer_id
FROM customers c
WHERE NOT EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);
```

Expected behavior: only customers with no orders are returned.

## 8. Duplicate and Cardinality Checks
Joins can multiply rows when the join key is not unique on either side.

```sql
-- Check right-side key uniqueness before joining
SELECT customer_id, COUNT(*) rows_per_key
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 1;

-- Compare before and after row counts
WITH left_rows AS (
    SELECT customer_id FROM customers
),
joined_rows AS (
    SELECT c.customer_id, o.order_id
    FROM left_rows c
    LEFT JOIN orders o
        ON o.customer_id = c.customer_id
)
SELECT 'left_rows' stage, COUNT(*) row_count FROM left_rows
UNION ALL
SELECT 'joined_rows', COUNT(*) FROM joined_rows;

-- Check whether one expected output row per customer was preserved
SELECT customer_id, COUNT(*) output_rows
FROM joined_rows
GROUP BY customer_id
HAVING COUNT(*) > 1;
```

For outer joins, put filters on the optional table inside the `ON` clause when the filter should not remove preserved rows.
