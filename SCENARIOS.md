# Scenarios

Pick **one** of the 4 domains below. Each one gives you a stakeholder, a
real business problem, and a folder of real (or clearly-labeled synthetic)
data under `data/<domain>/` — see `data/SOURCE.md` for exactly where each
file comes from and what's genuinely messy about it. Once you've chosen,
delete the other 3 folders from `data/` in your own repo.

Every domain gives you the **same kind of task**: design a normalized
schema, load the real data into it, and write SQL that answers your
stakeholder's actual question — the schema/query work is yours to design in
every domain, nobody hands you a data model.

## Finance & Insurance

> "We keep flood claims and flood policies in two separate systems, and
> nobody can tell me which communities are collecting the most in claims
> relative to what we're actually insuring there. I need real numbers, not
> a guess, before our next reinsurance renewal." — NFIP Program Analyst

**Business problem:** which South Carolina communities have claims activity
that looks disproportionate to their policy coverage, and what does the
overall claims picture look like — count, average payout, flagged
high-claim policies?

**Data:** `data/finance_insurance/` — real FEMA NFIP policy and claims data.

## Healthcare Operations

> "Leadership wants to know which of our facilities are seeing the most
> visit volume and where average length-of-stay is creeping up — especially
> for emergency and inpatient encounters. Right now that means someone
> manually cross-referencing spreadsheets." — Hospital Operations Analyst

**Business problem:** what does visit volume and average length-of-stay
look like by facility and by encounter type, and where are the outliers?

**Data:** `data/healthcare_operations/` — Synthea synthetic patient/
encounter/facility data (see `data/SOURCE.md` for why this domain uses
synthetic data specifically).

## Public Sector

> "We get thousands of 311 requests a day across a dozen agencies, and I
> need a real answer on which agencies are actually falling behind — not
> which ones get the most complaints, which ones are slow to close them
> out." — NYC Constituent Services Program Manager

**Business problem:** what does resolution time look like by agency, and
which agencies have the largest real backlog of still-open requests right
now?

**Data:** `data/public_sector/` — real, current NYC 311 service request
data.

## Professional Services

> "Every partner tracks utilization a little differently and I don't trust
> any of the numbers I'm getting. I want one real, queryable answer for
> revenue-per-client and utilization rate across our actual engagements."
> — Managing Partner

**Business problem:** what does utilization rate and revenue-per-client
look like across engagements and service types, and which clients or
engagements stand out?

**Data:** `data/professional_services/` — synthetic client/engagement/
time-entry data (see `data/SOURCE.md` — no real public dataset like this
exists, so this one's built, not sourced).
