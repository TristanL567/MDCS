---
id: MDCS-TICKET-019
title: Integrate SQL prompt routing into the general SQL chain.
epic: epic-sql-prompt-validation
status: ready
risk: low
allowed_areas:
  - prompt-chains/README.md
  - prompt-chains/sql-general/
  - to-do/skill-map.md
must_not_touch:
  - tools/
  - procedures/
  - references/
requirements:
  - Update `prompt-chains/README.md` to index the new SQL chains:
    * `sql-cte-validation`
    * `sql-joins`
    * `sql-aggregation`
    * `sql-result-validation`
  - Update `prompt-chains/sql-general/README.md` routing guidance so the
    general chain directs specialized cases to the new chains.
  - Update relevant `prompt-chains/sql-general/*.md` prompts if needed so
    Copilot can classify:
    * CTE validation;
    * join explanation and validation;
    * aggregation design;
    * result validation.
  - Update `to-do/skill-map.md` to mention the expanded SQL prompt-chain layer.
non_goals:
  - Do not create or modify reference drawers.
  - Do not modify procedure closets.
  - Do not add new specialized chains in this ticket.
acceptance_criteria:
  - `sql-general` clearly routes specialized SQL tasks to the correct chain.
  - `prompt-chains/README.md` lists the new chains.
  - The MDCS validator passes.
verification_commands:
  - py -3.10 tools\validate_mdcs_library.py
depends_on:
  - MDCS-TICKET-015
  - MDCS-TICKET-016
  - MDCS-TICKET-017
  - MDCS-TICKET-018
---

# Body

## Goal

Make the general SQL chain the front door for the expanded SQL prompt library.

## Context

Specialized chains are useful only if the analyst can route to them easily.
This ticket updates the index and routing prompts after the specialized chains
exist.

## Procedure

1. Update the prompt-chain index.
2. Update SQL-general routing guidance.
3. Update the skill map.
4. Run the MDCS validator.

