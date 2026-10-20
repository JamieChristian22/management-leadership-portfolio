# Retail Resource and Service Decision Case

> **Simulated work sample:** All events, people, approvals, records, costs, and outcomes below are fictional portfolio exercises. They are not employer results or evidence of a live system implementation.

## Decision brief

**Decision owner:** Store Manager. **Exercise period:** a standalone two-week staffing pilot, separate from the original 12-week CSV. **Question:** Can we remove low-demand overlap without creating queues at peak times?

The original source series ends at labor cost 16.7%, NPS 67, wait 5.3 minutes, shrink 2.5%, schedule adherence 91%, and task completion 95%. This exercise explores how a manager could make a staffing decision; it does not explain or reproduce those improvements.

## Options and economics

Assumptions: weekly sales $200,000; current weekly labor 1,500 hours; loaded cost $25/hour; hours are transferable within approved schedules. These are exercise inputs, not source CSV values.

| Option | Weekly hours | Weekly labor cost | Labor / sales | Change from base | Service implication |
|---|---:|---:|---:|---:|---|
| A — retain current plan | 1,500 | $37,500 | 18.75% | $0 | Known peak gaps remain |
| B — remove 60 low-demand hours and move 40 existing hours to peaks | 1,440 | $36,000 | 18.00% | $1,500 saving | Requires cross-trained staff and breaks coverage |
| C — remove 120 hours broadly | 1,380 | $34,500 | 17.25% | $3,000 saving | Highest queue and workload risk |

Moving 40 hours changes timing, not total hours. Option B is preferred because it retains more capacity than C while testing the hypothesized scheduling problem. Savings are gross labor savings before pilot/training costs.

**Pilot investment:** 12 training hours × $25 = $300. Two full weeks at the B run rate produce $3,000 gross savings and $2,700 net of training. This assumes no overtime, no lost sales, and no additional cost.

## Sensitivity and break-even

| Scenario | Calculation | Result |
|---|---|---:|
| Sales fall 10% | $36,000 / $180,000 | 20.00% labor ratio despite lower cost |
| 20 overtime hours at $37.50 | $1,500 - $750 | $750 weekly net saving before training |
| Lost gross profit from service deterioration | $1,500 / 30% gross margin | $5,000 lost weekly sales eliminates gross labor saving |

A falling labor ratio is not the only success criterion. Track conversion, queue time, break compliance, and staff feedback; investigate changes before claiming net benefit.

## Pilot plan and acceptance

| Step | Owner | Deadline | Acceptance evidence |
|---|---|---|---|
| Analyze traffic by half-hour and day | Analyst | Pilot D-5 | Matched traffic, transactions, and staffing coverage |
| Confirm skills and availability | Front End Lead | D-4 | Two trained backup operators per peak period |
| Publish schedule and explain changes | Store Manager | D-3 | Staff acknowledgment and unresolved constraints log |
| Observe six peak intervals daily | Shift Lead | Each pilot day | Queue count, wait estimate, trigger time, response |
| Review service and cost together | Store Manager | D5 and D10 | Written continue/adjust/stop decision |

Trial thresholds: average observed peak wait <=6 minutes; no individual observed wait >12 minutes without incident review; no missed scheduled breaks; overtime <=10 hours/week. These are local pilot thresholds, distinct from the original 5.5-minute overall wait target.

## Worked exception and recovery

On pilot D3, two absences reduce planned peak coverage. The simulated observation log shows a 9-minute average peak wait across six intervals and 16 extra overtime hours forecast for the week.

1. Shift Lead activates backup staff immediately and logs the coverage gap.
2. Store Manager suspends further reductions for the next two shifts.
3. Analyst separates absence effects from schedule-design effects; does not average away the breach.
4. Revised plan restores 10 hours for $250/week and retains 50 hours of reduction, worth $1,250/week gross.
5. D5 decision: extend the pilot one week; do not scale while coverage is unstable.

## Handoff and learning

BAU owner is the Front End Lead; the Store Manager remains accountable for service/cost trade-offs. Review weekly for four weeks. Reopen the decision for two threshold breaches, sustained overtime, or deteriorating employee feedback.

**Lesson:** a manager can choose a smaller saving when the larger saving depends on unacceptable service risk. The exercise's recovery cost is explicit; the original scenario endpoints remain unchanged.
