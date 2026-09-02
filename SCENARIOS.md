# Scenarios

Pick **one** of the 4 domains below. Each one gives you a stakeholder, a
real business problem, and a folder of real (or clearly-labeled synthetic)
data under `data/<domain>/` — see `data/SOURCE.md` for exactly where each
file comes from and what's genuinely messy about it. Once you've chosen,
delete the other 3 folders from `data/` in your own repo.

**The 7 business questions below are given, not yours to invent.** Every
domain's question set is deliberately engineered to require a specific SQL
technique — this is what makes sure every submission hits real difficulty,
regardless of which domain you pick. Your job is to design the schema and
write the SQL that answers these exact questions — that's real, substantial
work on its own; the questions themselves aren't up for revision.

## Finance & Insurance

> "We keep flood claims and flood policies in two separate systems, and
> nobody can tell me which communities are collecting the most in claims
> relative to what we're actually insuring there. I need real numbers, not
> a guess, before our next reinsurance renewal." — NFIP Program Analyst

**Data:** `data/finance_insurance/` — real FEMA NFIP policy and claims data.

1. **(Join)** For each community with at least one policy, what's the
   total insured building coverage and average policy cost?
2. **(Left join)** For every community with a policy, how many claims has
   it actually had — including communities with zero claims?
3. **(Group by + Having)** Among communities with at least 3 recorded
   claims, which have an average net building payment above $15,000?
4. **(CTE)** Which communities have claims activity that looks
   disproportionate to their policy coverage — total claims paid relative
   to total coverage insured?
5. **(Window function)** Which communities rank highest by raw claim
   volume?
6. **(`COALESCE`)** What's the total claims exposure — building damage
   plus contents damage combined — across all communities, treating any
   missing payment amount as $0?
7. **(Materialized view, multiple queries)** Build a materialized view
   summarizing total coverage and total claims paid per community. Using
   it: which 5 communities have the highest claims-to-coverage ratio, and
   for just those 5, which cause-of-damage codes show up most?

## Healthcare Operations

> "Leadership wants to know which of our facilities are seeing the most
> visit volume and where average length-of-stay is creeping up — especially
> for emergency and inpatient encounters. Right now that means someone
> manually cross-referencing spreadsheets." — Hospital Operations Analyst

**Data:** `data/healthcare_operations/` — Synthea synthetic patient/
encounter/facility data (see `data/SOURCE.md` for why this domain uses
synthetic data specifically).

1. **(Join)** For each facility, how many encounters have they had and
   what's the total claim cost, among facilities with at least one
   encounter?
2. **(Left join)** For every facility, how many total encounters vs. how
   many were emergency encounters — including facilities with zero
   emergency encounters?
3. **(Group by + Having)** Among facilities with at least 10 encounters,
   which have an average total claim cost above $5,000?
4. **(CTE)** Using average length-of-stay per facility and encounter
   class, which facility+class combinations have the longest average
   stays?
5. **(Window function)** Rank facilities by total encounter volume.
6. **(`COALESCE`)** For each patient, are they deceased or still living as
   of the most recent encounter date in the dataset — using `COALESCE` to
   substitute that reference date wherever `deathdate` is missing — and
   what's their age at that point?
7. **(Materialized view, multiple queries)** Build a materialized view of
   encounter counts, average cost, and average length-of-stay per facility
   per encounter class. Using it: what's each facility's single most
   common encounter class, and which facilities have the longest average
   length-of-stay specifically for **inpatient** encounters?

## Public Sector

> "We get thousands of 311 requests a day across a dozen agencies, and I
> need a real answer on which agencies are actually falling behind — not
> which ones get the most complaints, which ones are slow to close them
> out." — NYC Constituent Services Program Manager

**Data:** `data/public_sector/` — real, current NYC 311 service request
data.

1. **(Join)** For each agency, how many requests have they received and
   what's their average resolution time, among requests that have been
   closed?
2. **(Left join)** For every agency, how many total requests vs. how many
   are currently open — including any agency with zero open requests?
3. **(Group by + Having)** Among complaint types with at least 50
   requests, which have an average resolution time above 1 hour?
4. **(CTE)** Using total vs. open counts per agency, which agencies have a
   backlog (open requests) making up more than 25% of their total volume?
5. **(Window function)** Rank agencies by number of currently-open
   (backlog) requests.
6. **(`COALESCE`)** For requests that are still open, how many hours has
   each been open — using the most recent `created_date` in the dataset as
   a stand-in "now" wherever `closed_date` is missing?
7. **(Materialized view, multiple queries)** Build a materialized view of
   request counts per agency per complaint type. Using it: what's each
   agency's single most common complaint type, and which agency handles
   the widest variety (most distinct complaint types)?

## Professional Services

> "Every partner tracks utilization a little differently and I don't trust
> any of the numbers I'm getting. I want one real, queryable answer for
> revenue-per-client and utilization rate across our actual engagements."
> — Managing Partner

**Data:** `data/professional_services/` — synthetic client/engagement/
time-entry data (see `data/SOURCE.md` — no real public dataset like this
exists, so this one's built, not sourced).

1. **(Join)** For each client, what's the total billed hours and estimated
   revenue (hours × hourly rate) across all engagements, among clients
   with at least one engagement?
2. **(Left join)** For every client, how many engagements do they have —
   including clients with zero engagements?
3. **(Group by + Having)** Among service types with at least 20 time
   entries, which have average billed hours per entry above 7.1?
4. **(CTE)** Using total hours per engagement rolled up per client, which
   clients have engagements collectively exceeding 400 hours?
5. **(Window function)** Rank clients by total estimated revenue.
6. **(`COALESCE`)** What's the total billed hours per engagement, treating
   any missing hours entry as 0?
7. **(Materialized view, multiple queries)** Build a materialized view of
   estimated revenue per client per service type. Using it: what's each
   client's dominant service type by revenue, and which clients are
   engaged across the most distinct service types?

## Schema Critique Exercise

This one isn't about your own domain — it's a schema a (fictional)
colleague wrote for a coffee shop's ordering system. Read it and critique
it for real, in writing, in `answers.md`'s "Schema critique" section.

```sql
CREATE TABLE customers (
    customer_id INTEGER,
    customer_name TEXT,
    email TEXT
);

CREATE TABLE orders (
    order_id INTEGER,
    customer_name TEXT,
    order_date DATE,
    total_amount NUMERIC
);

CREATE TABLE order_items (
    order_id INTEGER,
    product_name TEXT,
    quantity INTEGER,
    unit_price NUMERIC
);
```

Your colleague also ran this query, saw output that looked plausible, and
moved on without checking it further:

```sql
SELECT c.customer_name, SUM(o.total_amount) AS lifetime_spend
FROM customers c
JOIN orders o ON c.customer_name = o.customer_name
GROUP BY c.customer_name;
```
