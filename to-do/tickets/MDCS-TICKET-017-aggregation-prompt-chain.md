---
id: MDCS-TICKET-017
title: Create aggregation, GROUP BY, and HAVING prompt chain.
epic: epic-sql-prompt-validation
status: ready
risk: medium
allowed_areas:
  - prompt-chains/sql-aggregation/
must_not_touch:
  - tools/
  - procedures/
  - references/
requirements:
  - Create `prompt-chains/sql-aggregation/`.
  - Create `README.md` and numbered prompt files:
    * `01-aggregation-intake.md`
    * `02-output-grain-map.md`
    * `03-group-by-and-having-design.md`
    * `04-aggregation-edge-cases.md`
    * `05-final-aggregation-sql.md`
  - The chain must help Copilot design Oracle SQL aggregations correctly.
  - Require an aggregation map:
    * `business metric | source table | source field | filter | grouping grain | aggregate function | HAVING rule | output field | validation check`
  - Cover:
    * `COUNT`, `COUNT DISTINCT`, `SUM`, `AVG`, `MIN`, `MAX`;
    * conditional aggregation;
    * null handling;
    * `GROUP BY` output grain;
    * `HAVING` vs `WHERE`;
    * duplicate amplification from joins before aggregation;
    * when analytic/window functions are better than grouped aggregation.
  - Point to `references/oracle-sql/sections/aggregation_patterns.md` when
    detailed aggregation guidance is needed.
non_goals:
  - Do not modify references or procedures.
  - Do not create the SQL result validation chain in this ticket.
acceptance_criteria:
  - Chain forces Copilot to define output grain before SQL.
  - Chain distinguishes `WHERE` from `HAVING`.
  - Chain includes validation checks for grouped results.
verification_commands:
  - py -3.10 tools\validate_mdcs_library.py
depends_on:
  - MDCS-TICKET-014
---

# Body

## Goal

Create a prompt chain that makes Copilot design grouped SQL around explicit
metric definitions, output grain, filters, and validation checks.

## Context

Aggregation bugs often come from unclear grain, joins that multiply rows, or
incorrect use of `HAVING`. This chain makes the grain and checks explicit before
final SQL is accepted.

## Procedure

1. Create the chain directory and README.
2. Write the five numbered prompt files.
3. Include the aggregation map in the relevant prompts.
4. Run the MDCS validator.

