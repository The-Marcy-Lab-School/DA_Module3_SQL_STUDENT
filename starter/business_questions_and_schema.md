# Schema Design

Fill this in **before you write any SQL** — design before code, same
discipline as every project so far. Your domain's 7 business questions are
given in `SCENARIOS.md` (not yours to write this time — see that file for
why) — read all 7 for your domain **before** sketching anything below, so
your schema actually supports every one of them, not just the first few.

## Your domain

Domain: _______________ (from `SCENARIOS.md`)

Stakeholder's business problem, in your own words:

> TODO

## Your schema sketch (paper or here — before any `CREATE TABLE`)

For each table (3 minimum): name, columns with real types, which column is
the primary key, which columns are foreign keys and what they reference,
and at least one other real constraint (`NOT NULL` or `CHECK`) you're
choosing on purpose and can explain why.

**Your schema needs to be normalized to at least Third Normal Form
(3NF)** — not just "split into a few tables." Concretely, for every table:
no repeating groups or multi-valued columns (1NF), every non-key column
depends on the *whole* primary key, not just part of it (2NF — only
matters if you have a composite key), and no non-key column depends on
*another non-key column* instead of the key itself (3NF — e.g. storing a
city's state alongside a zip code in a table keyed by something else,
where the state is really a fact about the zip code, not about that row).

```
TODO — table 1
TODO — table 2
TODO — table 3
```

Why did you choose this split into tables (not one flat table, not more
tables than this)? One or two real sentences — "because the assignment
says so" isn't a reason.

> TODO

## Walk through all 7 questions against your sketch

For each of your domain's 7 questions in `SCENARIOS.md`, name which
table(s) it touches and which column(s) it actually needs. If a question
needs a column your sketch doesn't have yet, that's exactly what this step
is for — fix it now, not after you've already run `CREATE TABLE`.

```
Q1: TODO
Q2: TODO
Q3: TODO
Q4: TODO
Q5: TODO
Q6: TODO
Q7: TODO
```

## Schema design tradeoffs: normalized (3NF) vs. STAR

Your schema above is a normalized, OLTP-style design — the right choice
for protecting write-integrity and avoiding update anomalies. A **STAR
schema** (a fact table of events/transactions, surrounded by dimension
tables of the entities involved) is the other common real answer,
optimized instead for fast, repeated aggregate reads — the kind a BI
dashboard does over and over against the same joins.

Answer, specifically, for **your own domain's data** — not in the
abstract:

- If you rebuilt this as a STAR schema instead, what would the fact table
  be (one row per what?), and what would the dimension tables be?

  > TODO

- What's the real tradeoff for *this* project — what does your 3NF design
  protect that a STAR schema wouldn't, and what would a STAR schema make
  faster/simpler that your 3NF design doesn't? Not a textbook definition —
  reason about your actual tables and your actual 7 queries.

  > TODO

- Which one actually fits this project's real use case (a one-time
  analyst answering 7 fixed business questions, not a live dashboard), and
  why?

  > TODO
