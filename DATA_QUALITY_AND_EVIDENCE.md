# Data Quality and Evidence Guide

## Source precedence

1. Original project CSVs define the original weekly scenario values.
2. The machine-readable [metric register](evidence/metric_register.json) records selected source fields, units, baselines and endpoints.
3. Executive briefs and README summaries must agree with those sources.
4. New worked decision cases use separately stated assumptions and populations. They are independent exercises, not evidence that generated the original endpoints.
5. Existing workbooks and the PDF guide are supplementary snapshots. Resolve disagreements against the CSV and document the correction before using a number externally.

## Evidence classes

| Class | Meaning | Present here |
|---|---|---|
| Original illustrative series | Manually modeled weekly trajectory | Six CSVs |
| Worked analytical exercise | Explicit assumptions, calculations and decision | New project cases |
| Tabletop execution record | Fictional observations and approvals | CRM UAT and leadership examples |
| Automated repository check | Script verifies specific numeric/file relationships | Validation script and workflow |
| Real operational evidence | Actual system execution, measured outcomes, independently approved delivery | Not supplied |

The word “completed” refers to an authored work sample, never to a real implementation.

## Units and reporting windows

| Dataset | Percentage storage | Reporting interpretation |
|---|---|---|
| Retail | Percentage points: 18.9 means 18.9% | Weekly scenario snapshots |
| CRM | Percentage points: 93 means 93% | Rollout snapshots; early zeros may mean activity not started |
| Onboarding | Fractions: 0.87 means 87% | Weekly snapshots with different eligibility windows |
| Marketing | Fractions: 2.28 means 228% return | Weekly spend and attributed revenue under simplified common-window assumptions |
| Supply chain | Fractions: 0.95 means 95% | Weekly snapshots; monthly costs/incidents are monthly run-rate snapshots |
| People operations | Fractions: 0.95 means 95% | Current-start activity plus mature earlier-cohort outcomes |

Do not sum overlapping monthly snapshots. Do not average percentage rates across cohorts without matching numerator/denominator counts. Do not infer exact headcounts from rounded modeled percentages.

## Metric limitations

- **NPS:** a score from -100 to 100; not a percent satisfied. Source survey counts are unavailable.
- **Marketing return:** revenue less marketing spend divided by marketing spend; excludes product costs. ROAS assumes the spend column represents ad spend in this simplified scenario.
- **OTIF:** joint on-time-and-in-full proportion on the same order population. Confirm the promised-date rule and denominator.
- **Lead-time variance:** the source dictionary uses absolute deviation in days, not statistical variance in squared days.
- **CSAT:** respondent average; no survey response denominators are supplied in the original series.
- **Retention / readiness:** 90-day measures require matured cohorts. The current week's new hires are not automatically the denominator.
- **Zero values:** CRM pre-testing/pre-launch zeros are placeholders in the original model. In a real reporting system, distinguish not applicable, missing, and measured zero.

## Corrections in this upgrade

Retail README aligned to W12: NPS 67, wait 5.3 minutes, schedule adherence 91%, task completion 95%. Marketing executive brief aligned to W12 revenue return 228%.

The original smooth trajectories were preserved rather than retroactively presented as noisy observations. Independent exercises now include absences, capacity constraints, failed access checks, increased escalations, and unattractive downside economics.

## Refresh and review procedure

1. Identify source, period, population and unit before changing values.
2. Preserve the original file history and describe why a source changes.
3. Update the metric register and explanatory summaries together.
4. Run the validation command; investigate failures.
5. Reconcile workbook outputs, recalculate in the intended engine, and review visual presentation before distributing an updated workbook.
6. Record what was verified and what remains unverified.

## Responsible claims

File counts, formulas and badges do not establish capability by themselves. A reviewer should be able to follow an assumption, reproduce a calculation, challenge a decision, and hear a clear explanation of uncertainty.
