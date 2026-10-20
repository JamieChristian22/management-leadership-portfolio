# Marketing Investment and Experiment Decision

> **Simulated work sample:** All events, people, approvals, records, costs, and outcomes below are fictional portfolio exercises. They are not employer results or evidence of a live system implementation.

## Clarify the economics

The original series uses (attributed revenue - marketing spend) / marketing spend. At W12, ($419,840 - $128,000) / $128,000 = **228%** and revenue / spend = **3.28x**. This is a revenue-based return proxy. It excludes cost of goods, agency costs not in spend, refunds, and other operating costs; it is not profit ROI.

The dataset treats modeled marketing spend as the ROAS denominator. A real analysis must separate advertising spend from total marketing expense and use consistent attribution windows.

## Standalone channel allocation exercise

Assume a 60% contribution margin before advertising and matched 30-day attributed revenue. The figures below are independent of the weekly portfolio dataset.

| Channel | Spend | Attributed revenue | ROAS | Contribution after spend |
|---|---:|---:|---:|---:|
| Search | $40,000 | $140,000 | 3.50x | $44,000 |
| Social | $30,000 | $75,000 | 2.50x | $15,000 |
| Display | $20,000 | $30,000 | 1.50x | -$2,000 |
| Total | $90,000 | $245,000 | 2.72x | $57,000 |

Contribution after spend = revenue × 60% - spend. Aggregate ROAS = total revenue / total spend, not the simple mean of channel ROAS. Break-even ROAS = 1 / 60% = **1.67x**.

## Marginal allocation decision

Propose moving $10,000 from Display to Search. Historical average ROAS is not a marginal forecast.

| Sensitivity | Search marginal ROAS | Added revenue | Lost Display revenue at 1.5x | Net contribution change at 60% |
|---|---:|---:|---:|---:|
| Downside | 1.2x | $12,000 | $15,000 | -$1,800 |
| Base | 2.4x | $24,000 | $15,000 | +$5,400 |
| Upside | 3.0x | $30,000 | $15,000 | +$9,000 |

Total spend is unchanged. The incremental contribution formula is (added revenue - lost revenue) × margin. This deliberately exposes saturation risk.

**Recommendation:** move $5,000 initially and hold the remainder until a complete attribution window matures. Stop or revise if marginal ROAS falls below 1.67x or qualified-lead quality deteriorates.

## Completed creative test exercise

| Arm | Sessions | Leads | Conversion | Qualified leads | Qualified leads / sessions |
|---|---:|---:|---:|---:|---:|
| A — existing page | 1,000 | 50 | 5.0% | 30 | 3.0% |
| B — shorter form | 1,000 | 65 | 6.5% | 26 | 2.6% |

B increases raw conversion by 1.5 percentage points but reduces qualified-lead yield by 0.4 points. It would be misleading to declare B a winner on form submissions alone. This small synthetic sample does not establish statistical superiority for either arm.

**Simulated decision:** retain A pending a larger predefined test of qualified-lead yield; investigate whether removed form fields allowed low-fit submissions. Do not change success criteria after seeing results.

## Governance and executive readout

Marketing Ops owns attribution and deduplication; Sales Ops validates lead disposition; Finance reviews contribution assumptions. Freeze reporting at a consistent cutoff and restate late-arriving revenue transparently.

Weekly readout: spend, attributed revenue, contribution assumption, qualified pipeline, mature conversion, unresolved tracking issues, decision requested, owner and due date. Amber status applies while the attribution window is incomplete. Never present qualified pipeline as recognized revenue.
