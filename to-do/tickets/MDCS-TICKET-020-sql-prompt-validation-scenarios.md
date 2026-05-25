---
id: MDCS-TICKET-020
title: Add manual validation scenarios for SQL prompt chains.
epic: epic-sql-prompt-validation
status: ready
risk: low
allowed_areas:
  - prompt-chains/sql-validation-scenarios/
must_not_touch:
  - tools/
  - procedures/
  - references/
requirements:
  - Create `prompt-chains/sql-validation-scenarios/`.
  - Create `README.md` with manual validation guidance for the expanded SQL
    prompt chains.
  - Add scenario files:
    * `cte-validation-scenario.md`
    * `join-selection-scenario.md`
    * `aggregation-scenario.md`
    * `daily-morning-extract-scenario.md`
  - Each scenario must include:
    * business request;
    * tiny generic schema context;
    * expected chain to use;
    * expected Copilot behaviors;
    * unacceptable Copilot behaviors;
    * manual pass/fail checklist.
  - Scenarios must be generic and must not contain private company schema,
    credentials, or real data.
non_goals:
  - Do not build an automated test runner.
  - Do not modify existing chains, references, or procedures.
  - Do not generate PDF exports in this ticket.
acceptance_criteria:
  - Scenarios cover CTEs, joins, aggregation, and a recurring daily extract.
  - Each scenario can be used by a human to test whether a prompt chain makes
    Copilot behave correctly.
  - The MDCS validator still passes.
verification_commands:
  - py -3.10 tools\validate_mdcs_library.py
depends_on:
  - MDCS-TICKET-019
---

# Body

## Goal

Create manual validation scenarios for the SQL prompt chains so a human can test
whether Copilot follows the intended reasoning structure.

## Context

MDCS prompt chains cannot be fully validated by the existing structural
validator. Manual scenarios provide realistic checks for whether Copilot asks
for missing context, maps logic, explains SQL choices, and produces validation
steps before final answers.

## Procedure

1. Create the validation-scenarios directory.
2. Add one scenario for each major SQL behavior.
3. Include pass/fail checklists.
4. Run the MDCS validator.

