# MDCS Use Cases

MDCS is a prompt library and local helper toolkit for making web-based Copilot
more useful on Oracle SQL, Python ETL, Excel reporting, and synthetic data
tasks. It is meant for a human analyst who copies structured prompts into
Copilot and supplies local, sanitized context.

The operating model is:

1. Use a prompt chain when the task needs several Copilot turns.
2. Use a procedure closet when Copilot needs a task-specific workflow and output
   contract.
3. Open reference drawers only when the chain or procedure says the technical
   detail is relevant.
4. Use local tools to compress schema context, anonymize data, or validate the
   MDCS library before relying on it.

In short: prompt chains orchestrate, procedure closets govern, reference drawers
teach, and tools prepare.

## Repository Layers

| Layer | Location | Purpose |
| --- | --- | --- |
| Prompt chains | `prompt-chains/` | Multi-turn copy-paste workflows for Copilot. |
| Procedures | `procedures/` | Compact task closets with triggers, workflow, verification, and output contracts. |
| References | `references/` | Dense Oracle/Python drawers opened only when needed. |
| Tools | `tools/` | Local preprocessing, anonymization, and validation utilities. |
| PDFs | `pdfs/` | Portable exports of the Markdown library. |

## Use Case: General Oracle SQL Assistance

Use when a user has a broad SQL request, such as:

```text
I need data on XY repeatedly each morning.
```

Start with `prompt-chains/sql-general/`.

This chain makes Copilot classify the request before drafting SQL. It routes the
task into a more precise workflow:

- write new SQL;
- explain existing SQL;
- refactor SQL;
- debug a SQL error;
- improve readability;
- improve efficiency;
- map business logic to tables and fields.

How it works:

1. `01-task-classification.md` asks Copilot what kind of SQL work this is.
2. `02-context-intake.md` collects available tables, fields, joins, filters,
   date windows, expected grain, and missing context.
3. `03-solution-draft.md` separates the business logic from the SQL draft.
4. `04-review-and-refine.md` checks assumptions, correctness, and efficiency.
5. `05-final-answer-format.md` forces a predictable final answer.

Expected result:

- clear task classification;
- assumptions and missing questions;
- candidate SQL or routing to a specialized chain;
- final output with logic summary, SQL, and validation checks.

## Use Case: Mapping Business Logic To SQL Structure

Use when the business request is imprecise, contradictory, or not yet ready for
SQL. Example:

```text
I need the morning XY report for active customers, excluding closed cases, with
the latest status and totals by region.
```

Start with `prompt-chains/sql-logic-mapping/`.

This chain prevents Copilot from writing SQL too early. It first maps business
rules to tables, fields, joins, filters, calculations, and output columns.

The central artifact is a logic map:

| input requirement | business rule | table | field | join key | filter condition | derived calculation | aggregation level | output column | ambiguity or assumption |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

How it works:

1. `01-business-logic-intake.md` collects the request and blocks premature SQL.
2. `02-field-and-table-mapping.md` maps rules to source tables and fields.
3. `03-grain-and-join-validation.md` checks output grain, duplicate risk,
   many-to-many joins, missing date windows, and unclear relationships.
4. `04-sql-implementation-plan.md` turns the map into a SQL-ready plan.
5. `05-review-for-ambiguity.md` lists unresolved assumptions and clarification
   questions.

Expected result:

- a SQL-ready implementation plan;
- explicit join and grain decisions;
- field-to-output mapping;
- open questions before SQL generation.

## Use Case: Writing More Efficient SQL From Requirements

Use when the user wants new Oracle SQL that should be efficient from the start,
not when tuning an existing slow query with an explain plan.

Start with `prompt-chains/sql-efficiency/`.

This chain makes Copilot map the logic first, then draft SQL after the map is
approved. It nudges Copilot toward efficient Oracle patterns:

- selective predicates;
- explicit joins;
- staged CTEs for readable logic;
- clear aggregation grain;
- avoiding unnecessary `DISTINCT`;
- avoiding functions on indexed filter columns where possible;
- validation queries for row counts and duplicates.

How it works:

1. `01-requirement-intake.md` restates business objective, source tables,
   fields, joins, filters, aggregations, and output grain.
2. `02-logic-map.md` builds the required rule-to-field map.
3. `03-sql-draft.md` writes SQL only after the map is approved.
4. `04-efficiency-review.md` reviews avoidable inefficiency.
5. `05-final-query-and-checks.md` returns final SQL, efficiency rationale, and
   validation checks.

Expected result:

- final Oracle SQL;
- explanation of the logic encoded in the query;
- efficiency notes;
- validation checklist for duplicates, grain, nulls, counts, and totals.

## Use Case: Tuning An Existing Slow Oracle Query

Use when a slow query already exists and the user can provide `EXPLAIN PLAN`
output or runtime evidence.

Use either:

- `prompt-chains/query-tuning/` for a multi-turn Copilot session; or
- `procedures/query_tuner/SKILL.md` as the governing procedure closet.

Relevant reference drawers:

- `references/oracle-sql/sections/query_tuning.md`;
- `references/oracle-sql/sections/oracle_idioms.md`.

How it works:

1. Prepare compressed schema context, the slow SQL, observed runtime, and plan
   output.
2. Ask Copilot to identify plan bottlenecks before suggesting rewrites.
3. Request multiple semantically equivalent rewrite candidates.
4. Verify row counts, key aggregates, sampled row parity, explain plan changes,
   and repeated timings.

Expected result:

- bottleneck summary tied to plan evidence;
- rewrite candidates with tradeoffs;
- local equivalence and timing checks.

## Use Case: Generating Python Oracle-To-Excel Reports

Use when the user wants a Python script that queries Oracle, transforms data
with pandas, and writes a formatted Excel workbook.

Use either:

- `prompt-chains/report-generation/` for a multi-turn Copilot session; or
- `procedures/report_generator/SKILL.md` as the governing procedure closet.

Relevant reference drawers:

- `references/python-idioms/sections/pandas_etl.md`;
- `references/python-idioms/sections/openpyxl_excel.md`.

How it works:

1. Collect workbook requirements: sheets, headers, formatting, output path,
   sorting, grouping, and validation totals.
2. Provide SQL or compressed schema context.
3. Ask Copilot to generate the Oracle extraction and pandas transform code.
4. Ask Copilot to generate openpyxl workbook writing and styling code.
5. Review the full script for connection cleanup, memory handling, type
   conversion, workbook structure, and verification checks.

Expected result:

- maintainable Python script;
- clear separation between extraction, transformation, and styling;
- dependency assumptions and run instructions;
- local workbook verification checklist.

## Use Case: Generating Schema-Valid Mock Data

Use when the user needs synthetic rows that respect Oracle table relationships.

Use either:

- `prompt-chains/mock-data-generation/` for a multi-turn Copilot session; or
- `procedures/mock_data_generator/SKILL.md` as the governing procedure closet.

Relevant reference drawers:

- `references/oracle-sql/sections/plsql_basics.md`;
- `references/oracle-sql/sections/oracle_idioms.md`.

How it works:

1. Generate or paste compressed schema context from `tools/schema_compressor.py`.
2. Ask Copilot to derive the parent-child load order from PK/FK relationships.
3. Choose output mode: SQL inserts, PL/SQL block, Python generator, or CSVs.
4. Generate parent rows before child rows.
5. Verify FK validity, non-null fields, uniqueness, date ranges, domain values,
   and row counts.

Expected result:

- one chosen mock-data artifact style;
- explicit table generation order;
- row-count summary;
- constraint and realism validation notes.

## Use Case: Compressing Schema Context For Copilot

Use when raw DDL or database metadata is too large to paste into Copilot.

Tool:

- `tools/schema_compressor.py`

How it works:

1. Run the tool against a local DDL file or Oracle database metadata.
2. The tool emits compact table notation with columns, shortened types, PKs, and
   FKs.
3. Paste the compressed schema into a prompt chain or procedure.

Typical consumers:

- `prompt-chains/query-tuning/`;
- `prompt-chains/sql-logic-mapping/`;
- `prompt-chains/sql-efficiency/`;
- `prompt-chains/mock-data-generation/`;
- `procedures/query_tuner/SKILL.md`;
- `procedures/mock_data_generator/SKILL.md`.

Expected result:

- smaller prompt context;
- enough schema structure for joins, filters, mock data, and SQL generation;
- less risk of exceeding Copilot's context window.

## Use Case: Anonymizing Data Before Prompting

Use when the user wants to show Copilot representative data without exposing
real names, emails, phone numbers, identifiers, or sensitive numeric values.

Tool:

- `tools/data_anonymizer.py`

How it works:

1. Provide a local CSV or Excel input file.
2. Choose explicit columns or use automatic detection.
3. Apply hashing, masking, perturbation, or auto-detection strategies.
4. Paste only the anonymized output into Copilot.

Expected result:

- safer sample data for debugging or report generation;
- join-preserving masked IDs where needed;
- perturbed numeric values that preserve rough distribution without exposing
   exact figures.

## Use Case: Validating The MDCS Library

Use after editing procedures or references.

Tool:

- `tools/validate_mdcs_library.py`

Run:

```powershell
py -3.10 tools\validate_mdcs_library.py
```

The validator checks:

- every procedure closet has all required Aegis-style frontmatter keys;
- each `reference_pointers` entry is structured and resolves to a drawer;
- procedure closets stay under the line budget;
- reference indexes and drawers stay under their budgets;
- drawer files begin with `relevant-when:`.

Expected result:

- confidence that the prompt library still follows the MDCS architecture;
- fast feedback before relying on changed prompts.

## Use Case: Using PDFs Outside The Repo

Use when the analyst needs a portable copy for a work machine, printout, or
environment where the Markdown repo is not available.

Location:

- `pdfs/`

How it works:

1. Open the PDF matching the needed prompt chain, procedure, or reference.
2. Use it as a readable source beside Copilot.
3. Copy the corresponding Markdown text from the repo when possible; use the PDF
   for review, sharing, or offline reading.

Expected result:

- portable MDCS instructions;
- easier use in restricted or non-development environments.

## Example: Daily Morning Data Request

User request:

```text
I need data on XY repeatedly each morning.
```

Recommended MDCS path:

1. Start with `prompt-chains/sql-general/01-task-classification.md`.
2. Route to `prompt-chains/sql-logic-mapping/` because the business logic is
   vague.
3. Build the logic map:
   - what "XY" means;
   - which tables and fields define it;
   - what the morning date window means;
   - what the output grain is;
   - which filters and joins apply;
   - which assumptions need confirmation.
4. Move to `prompt-chains/sql-efficiency/` once the mapping is approved.
5. Generate efficient Oracle SQL with validation checks.
6. If the query is slow after implementation, use `prompt-chains/query-tuning/`
   with `EXPLAIN PLAN`.

Final expected Copilot output:

- business objective;
- output grain;
- logic map;
- final Oracle SQL;
- validation queries;
- assumptions and open questions;
- efficiency notes.

