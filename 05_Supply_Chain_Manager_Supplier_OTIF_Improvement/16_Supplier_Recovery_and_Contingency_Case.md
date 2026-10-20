# Supplier Recovery and Contingency Case

> **Simulated work sample:** All events, people, approvals, records, costs, and outcomes below are fictional portfolio exercises. They are not employer results or evidence of a live system implementation.

## Decision brief and source definition

OTIF means delivered on the promised date **and** in full, using the same eligible order population. Do not multiply on-time and in-full rates unless independence is justified.

The original source series ends at OTIF 95%, OTD 96%, and in-full 98%. The following 100-order example independently demonstrates a valid intersection; it is not the underlying source dataset.

| Delivery classification | Orders |
|---|---:|
| On time and in full | 95 |
| On time, not in full | 1 |
| Late, in full | 3 |
| Late, not in full | 1 |
| Total | 100 |

OTIF = 95%; OTD = (95+1)/100 = 96%; in-full = (95+3)/100 = 98%. Lock the original promised date for performance measurement; record revised commitments separately to prevent improving the score by moving due dates.

## Supplier S-01 recovery incident

Fictional critical component: four days of usable stock, demand 100 units/day, primary delivery delayed seven days. Gap = (7-4) × 100 = **300 units**, assuming demand and delivery timing hold. Confirm the actual inventory position, reservations and open orders before executing.

| Option | Assumptions | Incremental cost | Constraint |
|---|---|---:|---|
| Expedite primary stock | $2,400 freight | $2,400 | Arrival only confirmed in six days; two-day gap remains |
| Qualified alternate | 300 units × $4 premium + $300 freight | $1,500 | Delivery in three days; requires current quality qualification |
| Wait for normal delivery | $0 logistics | Unknown service loss | Three-day exposure; economic loss not estimated |
| Reallocate internal stock | 300 units available at other site | $600 freight | Moves stockout risk to another site unless demand reviewed |

**Recommendation:** use qualified alternate if qualification, stock, and delivery are confirmed; otherwise evaluate internal reallocation after both sites approve. Do not choose solely by purchase-price variance.

## Corrective action record CAPA-01

| Stage | Evidence / action | Owner | Due |
|---|---|---|---|
| Containment | Reserve 300 alternate units; monitor receipt daily | Buyer | D0 |
| Problem definition | Three-day potential supply gap; original promise retained | Planner | D0 |
| Root-cause hypothesis | Supplier capacity slot assigned to another customer | Supplier Manager | D2 |
| Verification | Review capacity plan, order acceptance and shipment records | Supplier Quality | D3 |
| Corrective action | Weekly capacity confirmation and commit-date exception alerts | Supplier | D5 |
| Effectiveness | Four consecutive eligible deliveries meet original promise and quantity | Supplier Quality | After fourth delivery |
| Closure | Buyer confirms continuity; quality lead verifies effectiveness | Procurement Lead | After evidence review |

Do not close a CAPA when an action is merely completed. Four delivery observations provide an initial check, not proof of permanent reliability.

## Escalation and decision rights

Red: stock cover shorter than confirmed replenishment lead time, unqualified substitute proposed, or repeat critical failure. Planner escalates same day to Procurement and Operations. Only authorized quality personnel release alternate materials; a cost saving does not override quality acceptance.

If demand rises to 140 units/day and existing stock remains 400 units, stock cover becomes 2.86 days. The assumed three-day alternate delivery is now marginal: seek earlier partial receipt or approved allocation immediately.

## Sustainment

Weekly scorecard pairs OTIF with defect rate, cost of expedites, and aged purchase orders. Monthly cost snapshots must not be summed across overlapping reporting windows. Procurement owns commercial follow-up; Planning owns coverage; Quality owns acceptance and CAPA effectiveness.
