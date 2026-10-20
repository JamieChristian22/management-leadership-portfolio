# CRM Delivery Control Pack

> **Simulated work sample:** All events, people, approvals, records, costs, and outcomes below are fictional portfolio exercises. They are not employer results or evidence of a live system implementation.

## Scope and decision rights

The source scenario covers 4,800 active records and a 10-week implementation. This pack adds a worked planning exercise; schedule estimates and costs are illustrative.

**In scope:** account/contact/opportunity workflow, stage criteria, deduplication, role permissions, migration reconciliation, user training, and support handoff.  
**Out of scope:** historical archive migration, custom mobile application, billing integration, and optional executive visualizations.

Sponsor approves scope and funding. Business Owner accepts business readiness. Technical Lead owns configuration and recovery. PM coordinates delivery, reports exceptions, and cannot waive security or business acceptance.

## Work breakdown and dependencies

| ID | Work package | Window | Predecessor | Responsible | Acceptance |
|---|---|---|---|---|---|
| W01 | Discovery and current-state review | W1 | None | BA | Signed exercise scope and pain-point inventory |
| W02 | Requirements and stage definitions | W2 | W01 | BA / Sales Ops | Prioritized requirements with acceptance criteria |
| W03 | Cleansing and mapping | W3–4 | W02 | Data Lead | Mandatory fields mapped; rejected records isolated |
| W04 | Configuration and access | W3–5 | W02 | Technical Lead | Role matrix and negative access checks |
| W05 | Trial migration and reconciliation | W5–6 | W03, W04 | Data Lead | Count, field and exception reconciliation |
| W06 | UAT and defect resolution | W7–8 | W05 | Business testers | Exit gates met and unresolved defects dispositioned |
| W07 | Training and cutover rehearsal | W8–9 | W06 starts | Training / Technical Lead | Attendance, readiness checks and recovery rehearsal |
| W08 | Readiness decision and release | W10 | W06, W07 | Sponsor / Business Owner | Go/no-go record and handoff |
| W09 | Hypercare | 30 days after release | W08 | Support Lead | Incident trend and ownership acceptance |

W05 → W06 → W08 is a release-sensitive dependency chain. This is a dependency assessment, not a mathematically calculated critical path; effort, resource calendars and detailed activity durations would be needed for that.

## Responsibility matrix

R = executes; A = accountable; C = consulted; I = informed. Each row has one A.

| Decision / deliverable | Sponsor | PM | Business Owner | Technical Lead | Data Lead | Support Lead |
|---|---|---|---|---|---|---|
| Scope and funding change | A | R | C | C | I | I |
| Business requirements | I | R | A | C | C | C |
| Migration reconciliation | I | C | C | A | R | I |
| Business UAT acceptance | I | R | A | C | C | C |
| Technical rollback readiness | I | C | C | A/R | C | C |
| Support handoff | I | R | C | C | I | A |

## Budget exercise

| Cost driver | Calculation | Budget |
|---|---|---:|
| PM / BA delivery | 120 hours × $65 | $7,800 |
| Configuration | 160 hours × $90 | $14,400 |
| Migration | 80 hours × $75 | $6,000 |
| Training | 40 hours × $50 | $2,000 |
| Pilot licenses | Fixed assumption | $3,000 |
| Base cost | Sum | $33,200 |
| Contingency | 15% of base | $4,980 |
| Authorized envelope | Base + contingency | $38,180 |

At W6, assumed actual cost is $20,100 and estimate to complete is $14,600. Forecast at completion = **$34,700**, leaving **$3,480** against the envelope. Do not confuse remaining budget ($18,080) with headroom after remaining work ($3,480). This is cost forecasting, not earned-value analysis.

## RAID and action ownership

| ID | Type / trigger | Impact | Owner | Response | Due / escalation |
|---|---|---|---|---|---|
| R01 | Risk: duplicate rate exceeds 3% after trial | Incorrect account ownership | Data Lead | Match rules and business exception review | W6; escalate unresolved high-value records |
| A01 | Assumption: managers release testers 4 hours/week | UAT capacity | Business Owner | Confirm named tester availability | W2; reduce scope or move date if unavailable |
| I01 | Issue: one permission check fails in exercise | Unauthorized visibility | Technical Lead | Block release; fix role inheritance; retest | Before readiness review |
| D01 | Dependency: field mapping approved | Trial migration cannot start | Sales Ops | Resolve field ownership | W4; PM escalates next business day |
| R02 | Risk: training completed but users cannot perform tasks | Adoption failure | Training Lead | Add task demonstration, not attendance alone | W9 |

## Worked change request CR-01

**Request:** add a custom executive dashboard during W7.  
**Estimate:** 24 configuration hours × $90 = $2,160 plus 8 test hours × $65 = $520; total **$2,680**.  
**Budget impact:** forecast rises to $37,380, leaving $800.  
**Schedule impact:** configuration and tester capacity conflict with UAT; potential three-working-day delay.  
**Alternatives:** accept and move date; replace an equal-effort feature after impact review; defer to post-hypercare backlog.  
**Simulated decision:** defer. Protect release acceptance and contingency; revisit after two weeks of stable support. No unstated approval is implied.

## Executive status — W8 exercise

**Overall amber:** release is conditional on permission retest and tester availability. Budget is within envelope. Three actions: Technical Lead closes I01 before readiness; Business Owner confirms testers within one day; PM documents CR-01 deferral in the decision log.

## Handoff and benefits

Support receives role matrix, known issues, escalation roster, backup/recovery steps, and ownership of data exceptions. At 30 days review active adoption, duplicate rates and ticket trends using consistent denominators. Business Owner owns benefits; PM closes the project only after handoff acceptance. The original 93% adoption and 97% UAT values remain modeled aggregates, not measurements produced by this pack.
