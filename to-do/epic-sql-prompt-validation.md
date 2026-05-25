# Epic: SQL Prompt Implementation And Validation

This epic expands MDCS with a focused SQL prompt library for business-analysis
SQL work. It targets the gap between vague business requests and correct,
efficient Oracle SQL by adding prompt chains and reference drawers for CTEs,
joins, aggregation, validation, and reusable SQL reasoning patterns.

## Goal

Help a human analyst guide Copilot through SQL tasks in a structured way:

- translate business logic into table, field, join, filter, and output maps;
- explain and validate CTE-based query structure;
- choose and explain joins with concrete examples;
- apply `GROUP BY`, `HAVING`, aggregate functions, and analytic alternatives
  with clear output grain;
- validate SQL results through row counts, duplicate checks, CTE-level checks,
  reconciliation totals, and ambiguity review;
- route everyday SQL work to the correct specialized prompt chain.

## Architecture Fit

This epic follows the MDCS adaptation of Aegis progressive disclosure:

- **Prompt chains** under `prompt-chains/` orchestrate multi-turn Copilot usage.
- **Procedure closets** under `procedures/` remain compact workflow contracts.
- **Reference drawers** under `references/` hold dense SQL patterns and examples.
- **Validation scenarios** provide manual prompt checks without pretending to be
  automated database tests.

Prompt chains should not duplicate long Oracle tutorials. When detailed SQL
knowledge is needed, chains point to the relevant `references/oracle-sql/`
drawer.

## Ticket List

| Ticket ID | Title | Status | Depends On |
| --- | --- | --- | --- |
| `MDCS-TICKET-014` | Expand Oracle SQL reference drawers for CTEs, joins, and aggregation | ready | `MDCS-TICKET-004` |
| `MDCS-TICKET-015` | Create CTE validation prompt chain | ready | `MDCS-TICKET-014` |
| `MDCS-TICKET-016` | Create join explanation and validation prompt chain | ready | `MDCS-TICKET-014` |
| `MDCS-TICKET-017` | Create aggregation, GROUP BY, and HAVING prompt chain | ready | `MDCS-TICKET-014` |
| `MDCS-TICKET-018` | Create SQL result validation prompt chain | ready | `MDCS-TICKET-014` |
| `MDCS-TICKET-019` | Integrate SQL prompt routing into the general SQL chain | ready | `MDCS-TICKET-015`, `MDCS-TICKET-016`, `MDCS-TICKET-017`, `MDCS-TICKET-018` |
| `MDCS-TICKET-020` | Add manual validation scenarios for SQL prompt chains | ready | `MDCS-TICKET-019` |

## Validation Expectations

Every implementation ticket should run:

```powershell
py -3.10 tools\validate_mdcs_library.py
```

Prompt-chain tickets also require manual inspection that:

- each prompt is copy-paste ready;
- prompts ask for missing business and schema context before generating SQL;
- prompts separate business logic from SQL syntax;
- examples are generic and contain no private schema or data;
- specialized chains are routed from `sql-general` only after integration.

