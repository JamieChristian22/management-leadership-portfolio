# Onboarding Pilot Evaluation and Decision

> **Simulated work sample:** All events, people, approvals, records, costs, and outcomes below are fictional portfolio exercises. They are not employer results or evidence of a live system implementation.

## Decision question

Should a prerequisite checklist and a named handoff owner be rolled out to every new customer? This standalone exercise uses two illustrative cohorts. It is independent of the original weekly aggregate series.

## Eligibility and measurement plan

Eligible: new small-business customers on the same plan, with contract signed and no custom integration. Exclude enterprise migrations, reactivations, and customers awaiting external procurement approval. Start time is contract signature; first value is first successful import plus first completed core workflow.

Use customers as the unit of analysis. Wait 14 days before evaluating activation and 30 days before evaluating retention risk. Customers without a mature observation window remain pending, not failures or successes.

## Worked cohort evidence

| Measure | Prior cohort | Checklist pilot |
|---|---:|---:|
| Eligible customers with 14 days of observation | 50 | 50 |
| Activated by day 14 | 30 | 39 |
| Activation rate | 60% | 78% |
| Escalated customers | 5 | 7 |
| Escalation rate | 10% | 14% |
| Survey responses | 20 | 25 |
| CSAT point total | 84 | 105 |
| Respondent CSAT | 4.2/5 | 4.2/5 |

Activation difference = 39/50 - 30/50 = **18 percentage points**; relative increase = 18/60 = **30%**. Escalations worsened by **4 percentage points**. Survey response rates differ (40% versus 50%); unchanged respondent CSAT does not prove unchanged customer experience.

An approximate unadjusted 95% interval for the activation difference is roughly **0.2 to 35.8 percentage points**, using a two-proportion normal approximation. The small sample and nonrandom before/after design make this exploratory. Customer mix, staffing, and seasonality could explain part of the change; no causal claim is justified.

## Decision and trade-off

**Decision: limited extension, not full rollout.** Activation is promising, but the escalation guardrail failed the pilot rule of no increase greater than 2 percentage points.

| Action | Owner | Due | Acceptance |
|---|---|---|---|
| Categorize all seven pilot escalations | CS Ops | D3 | Primary reason and ownership recorded |
| Simplify checklist language | Product Ops | D5 | Five-user comprehension exercise completed |
| Separate internal setup work from customer tasks | Implementation Lead | D5 | Customer effort measured rather than assumed |
| Run next pilot with concurrent allocation | Analytics Lead | Before next cohort | Predefined assignment, sample plan and observation windows |
| Review activation and escalations together | Product/CS owners | After mature cohort | Written scale, revise or stop decision |

A valid experiment would define a minimum detectable effect and adequate sample size before launch. Do not stop early merely because a weekly result looks favorable.

## Product feedback decision

Three fictional escalation themes: missing field explanations, import prerequisites, and unclear account ownership. Prioritize field explanations first because they affect every setup and are low effort; request instrumentation for import errors before proposing a larger build. Submit a problem statement, affected step, support evidence and success measure to the product backlog. Product leadership retains prioritization authority.

## Operational handoff

A complete handoff includes intended use, success event, customer owner, integration constraints, timeline, and open risks. CS accepts or returns the handoff with a reason within one business day. Escalate unowned blocked accounts after two business days. Track returned handoffs separately from completed handoffs to avoid inflating completeness.

## Interview reflection

Explain why a promising primary metric did not justify rollout, why cohort maturity matters, and how customer burden can worsen while activation improves. Distinguish the original modeled 87% activation endpoint from this independent 78% pilot example.
