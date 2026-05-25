---
id: MDCS-TICKET-015
title: Create CTE validation prompt chain.
epic: epic-sql-prompt-validation
status: ready
risk: medium
allowed_areas:
  - prompt-chains/sql-cte-validation/
must_not_touch:
  - tools/
  - procedures/
  - references/
requirements:
  - Create `prompt-chains/sql-cte-validation/`.
  - Create `README.md` and numbered prompt files:
    * `01-cte-intake.md`
    * `02-cte-logic-map.md`
    * `03-stepwise-validation.md`
    * `04-refactor-review.md`
    * `05-final-cte-checklist.md`
  - The chain must help Copilot validate and improve SQL built with CTEs.
  - The chain must require Copilot to identify:
    * each CTE name and purpose;
    * dependencies between CTEs;
    * source tables and fields used in each CTE;
    * output columns produced by each CTE;
    * row grain at each stage;
    * filters and joins introduced at each stage;
    * checks that prove each stage behaves as intended.
  - Include a required CTE map table:
    * `cte | purpose | source tables | input fields | joins/filters | output grain | output fields | validation check`
  - Prompt Copilot to avoid generating a final rewrite until the CTE map is
    complete.
  - Point to `references/oracle-sql/sections/cte_patterns.md` when detailed CTE
    guidance is needed.
non_goals:
  - Do not modify references or procedures.
  - Do not create join or aggregation chains in this ticket.
acceptance_criteria:
  - The chain is usable as a multi-turn Copilot workflow.
  - Prompts force stepwise CTE explanation before final SQL.
  - Prompts include CTE-level validation checks.
verification_commands:
  - py -3.10 tools\validate_mdcs_library.py
depends_on:
  - MDCS-TICKET-014
---

# Body

## Goal

Create a prompt chain for validating CTE-heavy SQL by mapping every stage before
asking Copilot for rewrites or final answers.

## Context

CTEs are useful for readable staged logic, but Copilot often treats them as
formatting only. This chain makes Copilot explain the logic, dependencies, and
validation checks for each CTE.

## Procedure

1. Create the chain directory and README.
2. Write the five numbered prompt files.
3. Ensure each prompt is copy-paste ready.
4. Run the MDCS validator.

