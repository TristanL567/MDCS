# SQL Efficiency Chain - 02 Logic Map

Use my requirement details to create a business logic map before writing SQL.

Do not write SQL yet.

Return exactly this table format:

| business rule | source table | source field | join/filter logic | transformation | output field | validation check |
| --- | --- | --- | --- | --- | --- | --- |

Rules:

1. Include one row per business rule, output field, join rule, filter rule, or
   aggregation rule.
2. Make the expected output grain explicit.
3. Mark any uncertain source field, join, filter, or transformation as
   `needs confirmation`.
4. Include validation checks for row counts, null handling, duplicate risk,
   aggregation totals, and date/filter boundaries where relevant.
5. End with: `Approve this logic map before I draft SQL.`

After producing the table, stop. Do not draft SQL until I explicitly approve
the logic map.

