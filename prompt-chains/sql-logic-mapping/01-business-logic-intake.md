# SQL Logic Mapping Chain - 01 Business Logic Intake

Act as a SQL business analyst translating unclear stakeholder requirements into
a precise SQL implementation plan.

This is a mapping workflow, not a query-writing workflow. Do not write SQL yet.
First, help me clarify the business logic and identify missing context.

Business request:

```text
<paste messy business logic, reporting request, acceptance criteria, examples, or stakeholder notes here>
```

Known context:

```text
<paste known tables, fields, date windows, filters, output columns, sample rows, or schema notes here>
```

Return:

1. Restated business objective.
2. Candidate input requirements.
3. Candidate output columns.
4. Missing table relationships.
5. Missing or unclear date windows.
6. Ambiguous field names or contradictory filters.
7. Clarification questions that must be answered before SQL can be written.

Block SQL generation if the mapping inputs are incomplete.
