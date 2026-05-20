---
id: MDCS-TICKET-006
title: Create Query Tuner procedural closet.
epic: epic-dumb-copilot
status: ready
risk: low
allowed_areas:
  - procedures/query_tuner/
must_not_touch:
  - tools/
  - references/
requirements:
  - Create the Query Tuner procedural closet directory: `procedures/query_tuner/`.
  - Create `procedures/query_tuner/SKILL.md`.
  - Ensure the file has valid frontmatter containing all 10 canonical Aegis keys:
    * `trigger`, `non_trigger`, `failure_modes_addressed`, `attention_signals`, `procedure`, `scope_boundary`, `composition_points`, `reference_pointers`, `verification`, `output_contract`.
  - Ensure `reference_pointers` is a list of structured mappings, pointing to:
    * `ref: oracle-sql`, `section: query_tuning`, `open_when: the explain plan indicates performance bottlenecks (e.g. Table Access Full, nested loops, slow sorts).`
    * `ref: oracle-sql`, `section: oracle_idioms`, `open_when: query rewrites require date math, CTEs, or window functions.`
  - Write a step-by-step interactive prompt procedure (under 200 lines total).
  - Ensure the `procedure` field in the frontmatter serves as a compact skeleton of the steps, and details of the analysis go into the drawers.
  - The step-by-step prompt itself will:
    1. **Persona & Context Bootstrapping**: Sets up Copilot's Oracle DBA persona.
    2. **Metadata Intake**: Instructions to feed the compressed schema representation and the target slow query.
    3. **Diagnostic Intake**: Instructions to fetch the `EXPLAIN PLAN` output from Oracle and paste it into the chat.
    4. **Tuning Evaluation**: Prompts Copilot to identify key bottlenecks and suggest optimizations.
    5. **Optimized Rewrite**: Directs Copilot to generate alternative queries (using hints, CTEs, or index-friendly clauses) and write local verification instructions (timing comparisons).
non_goals:
  - Do not include actual SQL reference code blocks in the closet itself. The closet must remain a thin procedural prompt that references the drawers.
acceptance_criteria:
  - Running `python tools/validate_mdcs_library.py` executes successfully.
  - The `SKILL.md` is strictly under 200 lines and contains all 10 keys.
  - Pointers in `reference_pointers` are structured with `ref`, `section`, and `open_when` keys.
verification_commands:
  - python tools/validate_mdcs_library.py
depends_on:
  - MDCS-TICKET-004
---

# Body

## Goal

Create a lightweight procedural closet prompt that guides Copilot step-by-step through slow SQL query diagnostics and tuning.

## Context

Tuning queries requires a disciplined workflow (gathering schema info first, looking at the explain plan, rewriting, and validating). Copy-pasting a procedure into the web chat keeps the conversation structured and prevents Copilot from giving guessing-based, unvalidated tuning advice.

## Procedure

1. Create `procedures/query_tuner/SKILL.md` with appropriate YAML frontmatter.
2. Structure the prompt sections with clear headers and XML tags.
3. Write instructions directing Copilot to request specific inputs (schema, query, and explain plan) in sequence rather than all at once.
4. Add reference pointers linking to the Oracle SQL reference drawers.
5. Validate using the library validator.
