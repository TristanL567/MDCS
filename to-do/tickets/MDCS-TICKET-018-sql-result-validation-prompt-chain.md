---
id: MDCS-TICKET-018
title: Create SQL result validation prompt chain.
epic: epic-sql-prompt-validation
status: ready
risk: medium
allowed_areas:
  - prompt-chains/sql-result-validation/
must_not_touch:
  - tools/
  - procedures/
  - references/
requirements:
  - Create `prompt-chains/sql-result-validation/`.
  - Create `README.md` and numbered prompt files:
    * `01-query-and-intent-intake.md`
    * `02-logic-and-grain-review.md`
    * `03-row-count-and-duplicate-checks.md`
    * `04-cte-and-join-checks.md`
    * `05-final-validation-report.md`
  - The chain must validate SQL results, not just SQL syntax.
  - Prompt Copilot to produce validation SQL or manual checks for:
    * output grain;
    * row counts by key dimensions;
    * duplicate keys;
    * nulls in required output fields;
    * aggregate reconciliation;
    * CTE-level row counts;
    * join row multiplication;
    * date-window boundaries.
  - Require a final validation report format:
    * `check | purpose | SQL/manual step | expected signal | issue if failed`
  - Point to CTE, join, and aggregation reference drawers when relevant.
non_goals:
  - Do not modify references or procedures.
  - Do not implement executable database tests.
  - Do not require database access from Copilot.
acceptance_criteria:
  - Chain gives a practical validation workflow for analyst-run SQL.
  - Chain separates syntax review from result correctness.
  - Final prompt produces a validation report.
verification_commands:
  - py -3.10 tools\validate_mdcs_library.py
depends_on:
  - MDCS-TICKET-014
---

# Body

## Goal

Create a prompt chain that helps a user validate whether SQL results match the
business logic and expected output grain.

## Context

Copilot can produce plausible SQL that runs but returns incorrect data. This
chain focuses on checks the analyst can run locally or reason through with
sample outputs.

## Procedure

1. Create the chain directory and README.
2. Write the five numbered prompt files.
3. Include a final validation report shape.
4. Run the MDCS validator.

