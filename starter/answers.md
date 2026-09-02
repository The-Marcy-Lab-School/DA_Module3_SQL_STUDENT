# Business Questions, Schema Design & Written Answers

Fill this in as you go — the schema-design sections come **before** any
`CREATE TABLE` (design before code, same discipline as every project so
far); the rest comes as you finish each piece.

## Your domain

Domain: _______________ (from `SCENARIOS.md`)

Stakeholder's business problem, in your own words:

> TODO

## Your schema sketch (before any `CREATE TABLE`)

Read all 7 of your domain's business questions in `SCENARIOS.md` first, so
your schema actually supports every one of them, not just the first few.

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

*(Optional: if you sketch/export a real ERD image for your schema, add it
here — `![ERD](../images/erd.png)` — and reference it, but bullets/plain
text above are completely sufficient on their own.)*

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

## Schema critique

See `SCENARIOS.md`'s "Schema Critique Exercise" for the flawed schema —
this one isn't about your own domain.

**Identify at least one real, specific flaw in the schema itself** — not a
style nitpick, an actual structural problem that would cause a real issue
down the line. Name the table(s)/column(s) involved and explain the actual
risk (what breaks, or what silently goes wrong, and when).

> TODO

**Now look at the query.** Is `c.customer_name = o.customer_name` actually
a safe way to connect a customer to their orders? What would have to be
true about the data for this join to be reliable — and what happens to the
result the moment that's not true?

> TODO

**Your colleague trusted this query because "the output looked right."**
What should they have done instead, before trusting it — be specific, not
"they should have tested it more."

> TODO

**If you were rebuilding this schema for real, what would you change?**
Sketch the fix — new/changed columns, real keys, real constraints — in a
sentence or two, you don't need full `CREATE TABLE` syntax here.

> TODO

## Read-only role

Once your schema and data are loaded (see `CHECKLIST_TIMELINE.md` for
where this fits), create a real Postgres role and verify it's genuinely
read-only. **No template for this one** — start with the official
[Postgres `CREATE ROLE` documentation](https://www.postgresql.org/docs/current/sql-createrole.html);
the point is finding and applying the right commands yourself, not being
handed them. Run `CREATE ROLE`/`GRANT` commands via `starter/db.py`'s
`execute()` (not `run_query()` — those don't return rows).

You need to end up with:
- A new role (not the one you've been connecting as) that can genuinely
  `SELECT` from your schema's tables.
- Confirmed it **cannot** `INSERT`/`UPDATE`/`DELETE` — actually try one and
  confirm it's rejected, not just that you granted `SELECT` and assumed
  the rest follows.
- Confirmed connecting *as* this role and querying your tables actually
  works — a role you never connected as isn't a verified role. To
  actually connect as the new role: temporarily change your
  `DATABASE_URL`'s username/password to the new role's (same host/port/
  database), run your test queries, then switch it back.

Write up what you did below: the real commands you used (paste them, don't
reconstruct from memory), what you tested to confirm it's genuinely
read-only, and what happened when you tried a write as the new role.

> TODO
