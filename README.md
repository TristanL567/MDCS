# MDCS

Make Dumb Copilot Smarter.

MDCS is a small prompt and instruction library for making coding assistants
produce more reliable output on Oracle, Python ETL, and Excel reporting work.
It is not a runtime framework and it does not install into Copilot as a native
skill system. Treat it as a set of prepared operating instructions, reference
drawers, and utility scripts that you can paste into Copilot Chat or keep open
beside your editor.

## What This Repo Does

MDCS gives Copilot a stricter way to work:

- **Procedures** tell Copilot how to approach a task.
- **References** provide compact technical patterns Copilot should consult only
  when needed.
- **Tools** help prepare safe context, such as compressed schema summaries and
  anonymized inputs.
- **PDF exports** make the Markdown prompts portable for a work PC or another
  environment where this repo is not available.

The goal is to reduce vague answers, missing verification, unsafe assumptions,
and generic code that ignores Oracle SQL, pandas, or openpyxl details.

## Repository Layout

```text
procedures/
  query_tuner/
  report_generator/
  mock_data_generator/

references/
  oracle-sql/
  python-idioms/

tools/
  schema_compressor.py
  data_anonymizer.py
  validate_mdcs_library.py

pdfs/
  PDF copies of the Markdown prompt and reference files.
```

## How It Works

MDCS adapts Aegis-style progressive disclosure into a plain repository layout:

1. Start with a procedure closet under `procedures/`.
2. Give Copilot only the procedure that matches the task.
3. Open the referenced drawers under `references/` only when the procedure says
   they are relevant.
4. Use `tools/` to prepare compact, non-sensitive inputs before prompting.
5. Ask Copilot to follow the procedure output contract and verification steps.

This keeps prompts smaller and more targeted. The procedure controls workflow;
the reference drawers carry detailed Oracle, pandas, and Excel idioms.

## Available Procedures

### Query Tuner

Use `procedures/query_tuner/SKILL.md` when Copilot needs to diagnose or rewrite
a slow Oracle SQL query. It asks for compressed schema context, the target slow
query, and `EXPLAIN PLAN` output, then guides Copilot toward plan-based
optimization candidates and verification steps.

### Report Generator

Use `procedures/report_generator/SKILL.md` when Copilot needs to build a Python
script that extracts Oracle data, transforms it with pandas, and writes a
formatted Excel workbook with openpyxl.

### Mock Data Generator

Use `procedures/mock_data_generator/SKILL.md` when Copilot needs to generate
schema-compliant mock data from compressed schema input. It focuses on PK/FK
load order, nullability, uniqueness, realism, and output format choice.

## Available References

### Oracle SQL

`references/oracle-sql/` contains drawers for:

- query tuning and explain-plan interpretation
- PL/SQL blocks, cursors, loops, and bulk operations
- Oracle idioms such as date handling, sequences, hierarchy, and windows

### Python Idioms

`references/python-idioms/` contains drawers for:

- modern `python-oracledb` Thin mode extraction into pandas
- cursor fetching, chunking, and safe type conversion
- openpyxl workbook generation and Excel formatting patterns

## Tools

Run tools with Python 3.10:

```powershell
py -3.10 tools\validate_mdcs_library.py
```

Useful utilities:

- `tools/schema_compressor.py`: compresses schema metadata into a prompt-sized
  summary for Copilot.
- `tools/data_anonymizer.py`: helps remove or replace sensitive values before
  sending context to an assistant.
- `tools/validate_mdcs_library.py`: checks the MDCS structure, frontmatter,
  reference pointers, and line budgets.

## How To Use With Copilot

1. Pick the procedure that matches the task.
2. Paste the procedure into Copilot Chat.
3. Paste only the reference drawer sections named by the procedure and relevant
   to the current problem.
4. Add your actual task, schema summary, SQL, workbook requirements, or mock
   data requirements.
5. Ask Copilot to return output in the procedure's output contract.
6. Run the local verification steps before accepting the result.

Example prompt shape:

```text
Follow this MDCS procedure:
<paste procedure>

Open these relevant MDCS reference drawers:
<paste only the needed drawers>

Task:
<paste your concrete request and sanitized context>

Return the result using the procedure output_contract and include verification steps.
```

## PDF Exports

The `pdfs/` folder contains PDF copies of the Markdown files. Use these when you
need to move the instructions to a work PC, print them, or keep them open beside
Copilot without cloning the repository.

The PDFs mirror the source layout where possible, for example:

```text
pdfs/
  README.pdf
  procedures/query_tuner/SKILL.pdf
  references/oracle-sql/README.pdf
  references/oracle-sql/sections/query_tuning.pdf
```

Regenerate them from the repo root with Pandoc if the Markdown changes.

## Validation

Before relying on the library after edits, run:

```powershell
py -3.10 tools\validate_mdcs_library.py
```

The validator checks:

- every procedure has the required Aegis-style frontmatter keys
- every reference pointer resolves to a drawer
- procedure closets stay under the line budget
- reference indexes and drawers stay under their budgets
- drawers begin with `relevant-when:`

## Practical Note

This repo is intentionally pragmatic. The files may use the word "closet" or
"drawer" because they follow progressive disclosure conventions, but the
working use case is simple: prepared prompts and focused technical references
that make Copilot less vague and more dependable.
