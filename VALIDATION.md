# Validation and Review Scope

## Reproduce repository checks

With Python 3.9+ installed, run from the repository checkout:

```bash
python3 scripts/validate_portfolio.py
```

No third-party packages or credentials are required.

The script checks six original CSVs against 43 registered metric baselines/endpoints; expected periods and row counts; rate ranges under each dataset's storage convention; marketing return/ROAS calculations; OTIF intersection bounds; 13 main README endpoint values; the corrected marketing brief; and local Markdown file links.

The register is a regression baseline, not an independent source of business truth. When the scenario intentionally changes, update the source, register, narrative and expected README values together.

## Workbook inspection

Source commit inspected: `1c24c285f6c2b2bed9c8fdc3d142a57934b52f4f`.

All 13 existing XLSX files were inspected read-only as ZIP/XML. See [report](evidence/workbook_inspection.json). Checks covered sheet names, formula presence, stored formula values, stored error cells, and literal broken-reference text. The report does not establish recalculation correctness.

## Deliberately outside these checks

- Real employer outcomes or actual CRM execution.
- Full row-level reconstruction of original modeled rates.
- Live spreadsheet recalculation, chart behavior or visual layout.
- PDF guide content or consistency.
- External link availability and Markdown heading anchors.
- Statistical causality or validation of business assumptions.

## Review of new calculations

Worked examples expose the assumptions and arithmetic for labor options, CRM cost forecasts/change impact, onboarding cohort rates, marketing contribution, supplier inventory exposure and people-operations capacity value. Review both arithmetic and whether the assumptions would fit the actual business before reusing them.

## Acceptance record

The published upgrade includes the script and its local execution result in [validation result](evidence/validation_result.txt). This records repository checks only; it is not production sign-off or independent certification.
