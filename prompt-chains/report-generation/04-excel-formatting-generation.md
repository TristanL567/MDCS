# Report Generation Chain - 04 Excel Formatting Generation

Continue following `procedures/report_generator/SKILL.md`.

Extend the report script with Excel workbook writing and formatting. Use
`references/python-idioms/sections/openpyxl_excel.md` as the relevant drawer,
but do not repeat its reference content.

Workbook formatting requirements:

```text
<paste confirmed sheet names, column order, formats, widths, freeze panes, filters, highlights, and output path here>
```

Return:

1. Workbook writing code with stable sheet ordering.
2. A separate openpyxl styling pass.
3. Column formats for dates, numbers, IDs, percentages, and text as applicable.
4. Empty-result and file-write behavior.
5. A short note on how styling remains separate from data logic.
