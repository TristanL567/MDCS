# Mock Data Generation Chain - 02 PK/FK Hierarchy Analysis

Continue following `procedures/mock_data_generator/SKILL.md`.

Using the compressed schema already provided, derive the parent-child dependency
order before generating any data.

Return:

1. Root parent tables.
2. Child tables and FK dependencies.
3. Proposed generation/load order.
4. Key pools that must be reserved for child rows.
5. Constraint details that remain ambiguous.

Keep this as a planning step only. Do not generate the final artifact yet.
