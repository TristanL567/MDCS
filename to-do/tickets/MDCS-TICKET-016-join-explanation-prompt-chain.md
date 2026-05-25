---
id: MDCS-TICKET-016
title: Create join explanation and validation prompt chain.
epic: epic-sql-prompt-validation
status: ready
risk: medium
allowed_areas:
  - prompt-chains/sql-joins/
must_not_touch:
  - tools/
  - procedures/
  - references/
requirements:
  - Create `prompt-chains/sql-joins/`.
  - Create `README.md` and numbered prompt files:
    * `01-relationship-intake.md`
    * `02-join-choice-explanation.md`
    * `03-duplicate-risk-check.md`
    * `04-example-driven-query.md`
    * `05-final-join-validation.md`
  - The chain must help Copilot explain and choose joins for Oracle SQL.
  - Prompt Copilot to produce a join map with:
    * `left table | right table | join type | join keys | cardinality | preserved rows | duplicate risk | validation check`
  - Include explicit handling for:
    * inner joins;
    * left joins;
    * full joins;
    * cross joins;
    * semi joins with `EXISTS`;
    * anti joins with `NOT EXISTS`;
    * one-to-one, one-to-many, and many-to-many risks.
  - Require generic mini-examples explaining how rows are kept or dropped.
  - Point to `references/oracle-sql/sections/join_patterns.md` when detailed
    join guidance is needed.
non_goals:
  - Do not modify references or procedures.
  - Do not duplicate long SQL tutorials in the prompt files.
acceptance_criteria:
  - Chain helps a user understand which join type matches the business logic.
  - Chain includes duplicate and cardinality checks.
  - Chain is copy-paste ready for Copilot.
verification_commands:
  - py -3.10 tools\validate_mdcs_library.py
depends_on:
  - MDCS-TICKET-014
---

# Body

## Goal

Create a prompt chain that makes Copilot explain joins clearly and validate row
preservation, cardinality, and duplicate risk before returning final SQL.

## Context

Join mistakes are one of the fastest ways to produce wrong business-analysis
data. This chain forces Copilot to map relationships and explain expected row
behavior before generating or approving SQL.

## Procedure

1. Create the chain directory and README.
2. Write the five numbered prompt files.
3. Include a reusable join map.
4. Run the MDCS validator.

