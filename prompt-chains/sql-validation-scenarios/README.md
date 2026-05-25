# SQL Validation Scenarios

## Purpose

These scenarios are manual validation checks for SQL prompt chains. A human
reviewer can paste each scenario into Copilot and confirm whether Copilot uses
the intended chain behavior before writing or accepting SQL.

The scenarios are not automated database tests. They do not require real
database access, credentials, private schemas, or production data. They are
designed to check whether Copilot asks for the right context, maps logic before
SQL, identifies correctness risks, and provides manual checks the analyst can
run locally.

## How To Use

1. Open one scenario file.
2. Paste the business request and schema context into Copilot.
3. Tell Copilot to follow the expected prompt chain named in the scenario.
4. Compare Copilot's response to the expected and unacceptable behaviors.
5. Complete the manual pass/fail checklist.

The reviewer should fail a scenario if Copilot skips the required mapping,
chooses SQL too early, ignores grain or duplicate risk, invents schema details,
or claims it has validated results without analyst-provided evidence.

## Scenario Coverage

| Scenario | Prompt chain exercised | Main behavior under review |
| --- | --- | --- |
| `cte-validation-scenario.md` | `prompt-chains/sql-cte-validation/` | CTE inventory, stage-level grain, dependencies, and validation checks before refactor advice. |
| `join-selection-scenario.md` | `prompt-chains/sql-joins/` | Join choice, row preservation, cardinality, duplicate risk, and final join validation. |
| `aggregation-scenario.md` | `prompt-chains/sql-aggregation/` | Metric definitions, output grain, grouping, `HAVING`, null handling, and reconciliation checks. |
| `daily-morning-extract-scenario.md` | `prompt-chains/sql-general/`, routed into `prompt-chains/sql-logic-mapping/`, `prompt-chains/sql-efficiency/`, and `prompt-chains/sql-result-validation/` where appropriate | General routing from a broad request into mapping, efficient SQL drafting, and result validation. |

## Review Notes

- Keep the scenarios generic. Do not add private company schema, credentials,
  server names, account numbers, customer records, or real data.
- Do not paste long content from prompt chains or reference drawers into these
  scenarios.
- Treat each checklist as a human judgment aid, not a substitute for running
  local SQL checks in the analyst's own environment.
