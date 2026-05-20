# Prompt Chains

Prompt chains are copy-paste sequences for multi-turn Edge Copilot workflows.
They sit above MDCS procedure closets and reference drawers:

- **Prompt chains** orchestrate a sequence of Copilot prompts for a human
  analyst.
- **Procedure closets** define the workflow, output contract, and verification
  expectations for a task.
- **Reference drawers** hold dense Oracle SQL, Python, pandas, and openpyxl
  knowledge that should be consulted only when relevant.

This preserves progressive disclosure: a chain should tell the analyst which
prompt to paste next, which closet governs the workflow, and which drawers may
be relevant. It should not duplicate the detailed content from those closets or
drawers.

## Chain Contract

Each chain lives under:

```text
prompt-chains/<chain-name>/
```

Each chain directory must contain:

- `README.md`: describes the chain purpose, expected inputs, prompt sequence,
  related procedure closets, and related reference drawers.
- Numbered prompt files, for example:

```text
prompt-chains/<chain-name>/
  README.md
  01-intake.md
  02-analysis.md
  03-output.md
```

Each prompt file must be copy-paste ready for web Copilot. The analyst should
be able to paste the file as a standalone prompt, add the requested local
context, and continue the sequence.

Prompt files must reference existing procedure closets under `procedures/` and
reference drawers under `references/` rather than copying their detailed SQL,
Python, pandas, or openpyxl guidance.

## Index

| id | use case | prompt sequence | related closet | related references |
| --- | --- | --- | --- | --- |
| _TBD_ | No use-case prompt chains have been authored yet. | _TBD_ | _TBD_ | _TBD_ |
