---
id: MDCS-TICKET-014
title: Expand Oracle SQL reference drawers for CTEs, joins, and aggregation.
epic: epic-sql-prompt-validation
status: ready
risk: low
allowed_areas:
  - references/oracle-sql/
must_not_touch:
  - tools/
  - procedures/
  - prompt-chains/
requirements:
  - Update `references/oracle-sql/README.md` to index three new drawers:
    * `cte_patterns`
    * `join_patterns`
    * `aggregation_patterns`
  - Create `references/oracle-sql/sections/cte_patterns.md`.
    * Stay under 150 lines.
    * Begin with a one-line `relevant-when:` header.
    * Explain how CTEs structure query logic, including staged CTEs, naming,
      dependency order, final-select validation, and when CTEs become
      over-fragmented.
    * Include small generic examples of CTE validation checks, such as checking
      row counts at each stage.
  - Create `references/oracle-sql/sections/join_patterns.md`.
    * Stay under 150 lines.
    * Begin with a one-line `relevant-when:` header.
    * Explain inner, left, right, full, cross, semi, and anti joins in Oracle
      terms.
    * Include examples that show expected row-preservation behavior and
      duplicate risk.
  - Create `references/oracle-sql/sections/aggregation_patterns.md`.
    * Stay under 150 lines.
    * Begin with a one-line `relevant-when:` header.
    * Explain aggregate functions, `GROUP BY`, `HAVING`, output grain,
      conditional aggregation, distinct counts, null handling, and when an
      analytic/window function may be better than collapsing rows.
non_goals:
  - Do not create prompt chains in this ticket.
  - Do not modify procedure closets.
  - Do not include private schemas, credentials, or company data.
acceptance_criteria:
  - The Oracle SQL reference index remains under 120 lines.
  - Each new drawer remains under 150 lines and starts with `relevant-when:`.
  - The validator passes.
verification_commands:
  - py -3.10 tools\validate_mdcs_library.py
depends_on:
  - MDCS-TICKET-004
---

# Body

## Goal

Add dense Oracle SQL reference drawers that specialized prompt chains can point
to when they need CTE, join, or aggregation knowledge.

## Context

Prompt chains should stay lightweight and procedural. Detailed explanations and
generic examples belong in reference drawers so the user can open only the
drawer needed for the active SQL task.

## Procedure

1. Update the Oracle SQL reference index.
2. Add `cte_patterns.md`, `join_patterns.md`, and `aggregation_patterns.md`.
3. Keep examples generic and compact.
4. Run the MDCS validator.

