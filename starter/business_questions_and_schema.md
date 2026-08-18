# Business Questions & Schema Design

Fill this in **before you write any SQL** — design before code, same
discipline as every project so far. A strong schema comes from knowing
exactly what questions it needs to answer; a schema designed first and
questions written after almost always ends up missing a column or a table
you actually needed.

## Your domain

Domain: _______________ (from `SCENARIOS.md`)

Stakeholder's business problem, in your own words:

> TODO

## Your 5 business questions

Write these first. Each one becomes a real, graded query later — so make
each one specific enough that you could recognize a right answer if you saw
one (that's what the later "check it against a sample where you already
know the answer" step depends on). Across your 5 questions, plan for one
that genuinely needs a left join (a real "rows that don't have a match on
the other side" case — look at your domain's data before finalizing this
one, don't assume) and one that's naturally a ranking/"top N by category"
question (that's the one you'll answer with a window function).

1. TODO
2. TODO
3. TODO
4. TODO
5. TODO

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
  reason about your actual tables and your actual 5 queries.

  > TODO

- Which one actually fits this project's real use case (a one-time
  analyst answering 5 business questions, not a live dashboard), and why?

  > TODO
