# Skill Map

This map places MDCS procedural closets and reference drawers on the IT-Business Analyst workflow axis. It serves as the index and overlap-detection catalog.

## Prompt Chains

Prompt chains are a lightweight orchestration layer for multi-turn Edge Copilot
workflows. They live under `prompt-chains/` and provide copy-paste prompt
sequences for a human analyst.

Chains should coordinate the analyst's turns through intake, analysis,
generation, review, or refinement steps. They must point to procedure closets
for workflow rules and output contracts, and to reference drawers for dense
technical knowledge, rather than duplicating that content.

The SQL prompt-chain layer now uses `prompt-chains/sql-general/` as the broad
entry point and routes specialized SQL work to focused chains for efficiency,
business-logic mapping, CTE validation, join explanation and validation,
aggregation design, SQL result validation, and plan-based query tuning. Dense
Oracle SQL guidance remains in `references/oracle-sql/` drawers.

## Procedures (Closets)

| Workflow phase | Closet Prompt | Status | Consulted references | Overlap boundary |
| --- | --- | --- | --- | --- |
| DB Intake & Diagnostics | `mock-data-generator` | proposed | `oracle-sql` | Generates schema-compatible mock datasets locally using compressed schemas. Excludes query tuning. |
| SQL Optimization | `query-tuner` | proposed | `oracle-sql` | Guides step-by-step query analysis and explain-plan evaluation. Excludes python scripting. |
| Python Reporting | `report-generator` | proposed | `python-idioms` | Handles pandas ETL and excel spreadsheet generation. Excludes direct Oracle schema generation. |

## References (Drawers)

| Reference | Status | Topic Areas | Consuming closets |
| --- | --- | --- | --- |
| `oracle-sql` | proposed | Oracle SQL dialect, analytical functions, query tuning guidelines, mock tables | `query-tuner`, `mock-data-generator` |
| `python-idioms` | proposed | `oracledb` database integration, pandas data manipulation, `openpyxl` reporting | `report-generator` |

---

## Overlap Findings
- Healthy composition: `mock-data-generator` uses compressed schema output produced by `schema_compressor.py`.
- No forbidden overlaps: Procedural closets remain highly distinct (query optimization vs. python ETL generation vs. mock data generation).

---

## Intentional MDCS Adaptations
* **Root-Level Folders**: In contrast to standard Aegis, procedures and references reside at the root of the workspace (`procedures/` and `references/`) for simplicity.
* **Human Prompt-Chain Layer**: MDCS includes a lightweight `prompt-chains/` layer for multi-turn Edge Copilot sessions. Chains orchestrate prompts, procedure closets define workflow, and reference drawers hold dense knowledge.
* **Simplified Scope**: We implement prompt chains, procedural closets, and reference drawers while intentionally omitting the role (Master, Worker, Validator) and operating discipline layers since this prompt library is used directly by a human.
