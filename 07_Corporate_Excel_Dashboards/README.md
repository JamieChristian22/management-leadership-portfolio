# 📊 Excel Workbook Review Guide

## Choose the right artifact

Project operating workbooks contain source-style tabs and operational records. Corporate dashboards provide presentation-oriented KPI views. The root overview workbook is a static summary: the structural inspection found no formula cells in it.

- [Retail_Operations_Turnaround_Operating_Workbook.xlsx](../01_Retail_Operations_Manager_Store_Performance_Turnaround/Retail_Operations_Turnaround_Operating_Workbook.xlsx)
- [CRM_Implementation_PMO_Operating_Workbook.xlsx](../02_IT_Project_Manager_CRM_Implementation/CRM_Implementation_PMO_Operating_Workbook.xlsx)
- [Product_Operations_Onboarding_Operating_Workbook.xlsx](../03_Product_Operations_Manager_Customer_Onboarding_Optimization/Product_Operations_Onboarding_Operating_Workbook.xlsx)
- [Marketing_ROI_Optimization_Operating_Workbook.xlsx](../04_Marketing_Manager_Digital_Campaign_ROI_Optimization/Marketing_ROI_Optimization_Operating_Workbook.xlsx)
- [Supplier_OTIF_Improvement_Operating_Workbook.xlsx](../05_Supply_Chain_Manager_Supplier_OTIF_Improvement/Supplier_OTIF_Improvement_Operating_Workbook.xlsx)
- [People_Operations_Onboarding_Retention_Operating_Workbook.xlsx](../06_People_Operations_Manager_Onboarding_Retention_System/People_Operations_Onboarding_Retention_Operating_Workbook.xlsx)
- [01_Retail_Operations_Corporate_Dashboard.xlsx](../07_Corporate_Excel_Dashboards/01_Retail_Operations_Corporate_Dashboard.xlsx)
- [02_CRM_Implementation_Corporate_Dashboard.xlsx](../07_Corporate_Excel_Dashboards/02_CRM_Implementation_Corporate_Dashboard.xlsx)
- [03_Product_Operations_Corporate_Dashboard.xlsx](../07_Corporate_Excel_Dashboards/03_Product_Operations_Corporate_Dashboard.xlsx)
- [04_Marketing_ROI_Corporate_Dashboard.xlsx](../07_Corporate_Excel_Dashboards/04_Marketing_ROI_Corporate_Dashboard.xlsx)
- [05_Supply_Chain_Corporate_Dashboard.xlsx](../07_Corporate_Excel_Dashboards/05_Supply_Chain_Corporate_Dashboard.xlsx)
- [06_People_Operations_Corporate_Dashboard.xlsx](../07_Corporate_Excel_Dashboards/06_People_Operations_Corporate_Dashboard.xlsx)
- [Manager_Portfolio_Dashboards.xlsx](../Manager_Portfolio_Dashboards.xlsx)

## Inspection scope

A read-only ZIP/XML inspection of all 13 workbooks found no stored error-type cells and no literal `#REF!` in formula text. Twelve contain formula cells with stored values. This does **not** establish formula correctness, fresh calculation, visual quality, or interactivity. No recalculation or visual rendering was performed in this upgrade, and workbook binaries were preserved.

See [inspection report](../evidence/workbook_inspection.json) for file-by-file observations. The source commit inspected is recorded in [validation notes](../VALIDATION.md).

## Review sequence

1. Open a disposable copy in the intended spreadsheet application.
2. Read the project data dictionary and confirm percentage units.
3. Trace an executive KPI to its source row and compare it with the original CSV.
4. Recalculate; investigate errors or stale values rather than suppressing them.
5. Change one representative input and confirm affected formulas, chart values and status colors respond.
6. Restore the input and compare the result with the source.
7. Review labels, chart scales, number formats, print layout, clipping and legibility.

Specific spot checks: retail NPS 67, wait 5.3, adherence 91%, task completion 95%; marketing W12 revenue return 228% from $419,840 and $128,000. If a workbook snapshot disagrees, use the original CSV as authority and reconcile before external presentation.

## Refresh limitations

The files are saved snapshots, not a connected production reporting system. Do not assume refresh-on-open, automatic CSV ingestion, dynamic table extension, or verified Excel-native recalculation. New worked cases are Markdown exercises and are not integrated into these legacy workbooks.

[Portfolio](../README.md) · [Data quality policy](../DATA_QUALITY_AND_EVIDENCE.md)
