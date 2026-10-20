# CRM UAT and Release Evidence Exercise

> **Simulated work sample:** All events, people, approvals, records, costs, and outcomes below are fictional portfolio exercises. They are not employer results or evidence of a live system implementation.

## What this proves and what it does not

This is a completed **tabletop test-record exercise**. The observed results below are authored scenario observations; no CRM application was executed. These eight examples illustrate traceability, defects and release judgment. They do not substantiate the separate 97% modeled aggregate UAT rate.

## Requirement-to-test traceability

| Requirement | Acceptance criterion | Test ID |
|---|---|---|
| R01 — account deduplication | Identical normalized email is flagged for review, not silently merged | T01, T02 |
| R02 — stage governance | Opportunity cannot advance without mandatory fields | T03 |
| R03 — least-privilege access | User cannot view restricted region accounts by UI or direct link | T04, T05 |
| R04 — migration integrity | Imported + rejected records reconcile to submitted records | T06 |
| R05 — reporting freshness | Dashboard identifies refresh timestamp and reconciles totals | T07 |
| R06 — support routing | User submits a ticket with category, owner and escalation route | T08 |

## Recorded exercise execution

| ID | Preconditions and steps | Expected | Simulated initial observation | Initial result |
|---|---|---|---|---|
| T01 | Existing account; import same email in different case | Duplicate review item | One review item created | Pass |
| T02 | Two unrelated customers share organization name but have different identifiers | Preserve both; no automatic merge | Both retained | Pass |
| T03 | Leave next-step date blank; advance to proposal | Validation blocks stage change | Stage blocked with field message | Pass |
| T04 | Restricted-region user opens account search | Restricted account absent | Account not returned | Pass |
| T05 | Same user opens restricted account by direct ID | Access denied; no data disclosed | Account name visible through inherited role | Fail — DEF-01 |
| T06 | Submit 100 fixture records, including two invalid emails | 98 imported + 2 rejected = 100; rejected IDs logged | Counts reconciled; reject reasons recorded | Pass |
| T07 | Compare report total with five known opportunity amounts | Total 15,000 and refresh timestamp | 15,000 shown with timestamp | Pass |
| T08 | Submit a migration issue and trigger priority routing | Named support queue and escalation | Correct queue and reference ID | Pass |

T07 fixture amounts are 1,000, 2,000, 3,000, 4,000 and 5,000. These fixtures are independent of the 4,800-record source scenario.

Initial sample pass rate = 7/8 = **87.5%**. This rate cannot be generalized to the full implementation.

## Defect DEF-01

- Severity: **Sev-1 release blocker** in this exercise because restricted data is exposed.
- Reproduction: test user with inherited cross-region role opens a known restricted account URL.
- Hypothesis: inherited role grants read access beyond the intended region boundary.
- Owner: Technical Lead; fix removes conflicting inheritance and checks peer roles.
- Simulated retest: T05 denies access; rerun T04 and an allowed-region positive check to detect overrestriction.
- Retest disposition: closed in the tabletop record only; real release would require stored execution evidence and independent business/security review.

Final sample: eight of eight defined cases pass after simulated remediation. Additional positive regression check passes. This is not an actual test run or a claim of overall production readiness.

## Go/no-go gates

| Gate | Evidence required in real delivery | Exercise disposition |
|---|---|---|
| Critical workflows covered | Traceability and completed execution evidence | Eight examples provided; full suite still required |
| No open Sev-1 | Defect register and independently reviewed retest | DEF-01 closed in fiction only |
| Overall UAT >=95% | Complete test inventory with denominator and exclusions | Not independently verified by this sample |
| Migration reconciliation | Full count, field and exception reconciliation | 100-record example only |
| Business acceptance | Named approver and dated acceptance | No real sign-off claimed |
| Recovery readiness | Timed restore/rehearsal and validated recovery point | Not executed |
| Support readiness | Roster, known issues, access, escalation | Defined in delivery pack |

**Recommendation:** a real production release would remain **no-go until missing execution and approval evidence is provided**, regardless of a headline 97% pass rate.

## Cutover tabletop

T-24h: freeze approved configuration; confirm backup and stop criteria. T-2h: validate user access and support roster. T0: migrate approved scope. T+1h: reconcile counts and perform critical smoke checks. Stop for unreconciled material records, restricted-data exposure, or failed critical workflows. Technical Lead executes the approved recovery plan; Business Owner decides business acceptance; PM records timestamps and communications.

No actual recovery time objective is claimed. Set an RTO/RPO with system owners and verify it through rehearsal before committing to a release window.
