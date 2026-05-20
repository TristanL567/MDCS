---
id: MDCS-TICKET-004
title: Create Oracle SQL reference drawers.
epic: epic-dumb-copilot
status: ready
risk: low
allowed_areas:
  - references/oracle-sql/
must_not_touch:
  - tools/
  - procedures/
requirements:
  - Create the Oracle SQL reference directory structure: `references/oracle-sql/sections/`.
  - Create `references/oracle-sql/README.md` as the index. It must:
    * Declares the reference scope and consuming skills.
    * Limit the index size to at most 120 lines total.
    * Contain a markdown Sections table with columns: `id | topic | open when` (note the exact space in "open when").
    * Map the following drawers: `query_tuning`, `plsql_basics`, and `oracle_idioms`.
  - Create `references/oracle-sql/sections/query_tuning.md`:
    * Limit size to at most 150 lines total.
    * Begin with a one-line `relevant-when:` header key-style line.
    * Focus on Oracle explain plan analysis (interpreting Table Access Full, Index Range Scan, Nested Loops, Hash Joins).
    * Highlight Oracle-specific tuning hints (`/*+ INDEX */`, `/*+ LEADING */`, `/*+ PARALLEL */`).
    * Explain subquery factoring (CTEs) vs. subqueries in Oracle.
  - Create `references/oracle-sql/sections/plsql_basics.md`:
    * Limit size to at most 150 lines total.
    * Begin with a one-line `relevant-when:` header key-style line.
    * Explain cursor handling, exceptions, and bulk operations (`BULK COLLECT`, `FORALL`).
    * Demonstrate autonomous transactions (`PRAGMA AUTONOMOUS_TRANSACTION`).
  - Create `references/oracle-sql/sections/oracle_idioms.md`:
    * Limit size to at most 150 lines total.
    * Begin with a one-line `relevant-when:` header key-style line.
    * Detail analytical window functions (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LEAD`, `LAG`, `FIRST_VALUE`, `LISTAGG`).
    * Cover Oracle date arithmetic (e.g., handling `SYSDATE`, intervals, and timezone offsets).
    * Demonstrate hierarchical queries using `START WITH ... CONNECT BY PRIOR` and recursive CTEs.
non_goals:
  - Do not include project-private schema names, login details, or specific table structures. Keep references strictly generic and dialect-focused.
acceptance_criteria:
  - Running `python tools/validate_mdcs_library.py` passes on the Oracle SQL references.
  - The index is ≤120 lines and sections are ≤150 lines.
  - Every drawer begins with a one-line `relevant-when:` header.
verification_commands:
  - python tools/validate_mdcs_library.py
depends_on:
  - MDCS-TICKET-001
---

# Body

## Goal

Compile standard, dense Oracle SQL reference drawers to feed Copilot during active procedures, preventing dialect confusion.

## Context

Web-based Copilots often suggest generic SQL Server or PostgreSQL syntax (e.g. `LIMIT` instead of `ROWNUM`/`FETCH FIRST`, or generic interval math) which fails in Oracle SQL. Dedicated drawers teach the model Oracle-specific behavior.

## Procedure

1. Initialize `references/oracle-sql/README.md` and write the index table.
2. Draft `references/oracle-sql/sections/query_tuning.md` starting with a `relevant-when:` header and focusing on explaining Oracle's optimizer choices and hints.
3. Draft `references/oracle-sql/sections/plsql_basics.md` starting with a `relevant-when:` header and highlighting bulk binding and cursors.
4. Draft `references/oracle-sql/sections/oracle_idioms.md` starting with a `relevant-when:` header and outlining analytical functions, hierarchical queries, and dates.
5. Run the validator tool to check formatting and file line constraints.
