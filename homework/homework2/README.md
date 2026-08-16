# Retail Investor Awareness of Major Fund Holdings

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Institutional fund holdings are disclosed publicly every quarter — a free, rich signal of where large, sophisticated funds are positioned. Yet most retail investors never consult them. This project investigates how widely major fund holdings are actually tracked among retail investors, and whether low awareness represents a missed opportunity.

## Stakeholder & User
The primary stakeholder is the product team at a retail-investing platform deciding whether to build a fund-holdings tracking feature. The users of the output are the product managers and analysts who will act on the finding. 

## Useful Answer & Decision
**Descriptive.** The useful answer is a reliable estimate of the percentage of the target investor population that tracks major fund holdings, broken down by segment (experience level, portfolio size). **Metric:** percentage share of retail investors who track major fund holdings. 
**Artifact to deliver:** a short analysis with that headline metric plus the segment breakdown, so we can decide whether the feature is worth building.

## Assumptions & Constraints
- Data on investor behavior is available via survey or platform usage logs.
- Sample is representative of the target retail-investor population.
- Analysis capacity is a single student over the project timeline.
- No real-time latency requirement; a one-time descriptive analysis is sufficient.
- Any user data used complies with privacy expectations and platform terms.

## Known Unknowns / Risks
- Self-reported "tracking" may not match actual behavior; may need a proxy.
- How to validate the estimate without a ground-truth benchmark.

## Lifecycle Mapping
Goal → Stage → Deliverable
- Define the problem and who it serves → Problem Framing & Scoping (Stage 01) → This scoping paragraph + README
- Communicate framing to stakeholder → Problem Framing & Scoping (Stage 01) → Stakeholder memo in docs/
- Establish repo structure for later stages → Problem Framing & Scoping (Stage 01) → data/, src/, notebooks/, docs/ folder tree

## Repo Plan
data/, src/, notebooks/, docs/ ; cadence for updates