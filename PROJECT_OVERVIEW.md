# Project Overview: SQL & Relational Databases

## The objective

Pick one of 4 real stakeholder domains (`SCENARIOS.md`), then:

- **Design and build a real PostgreSQL database** for it — 3 tables
  minimum, normalized to **at least Third Normal Form (3NF)**, with
  primary keys, foreign keys, and at least one real constraint per table —
  your own design, not handed to you.
- **Load the real (or clearly-labeled synthetic) data** into it.
- **Write and verify SQL answering your domain's 7 given business
  questions** (see `SCENARIOS.md` — these are given, not yours to invent,
  and each one is built to require a specific real technique): a join, a
  left join, `GROUP BY`/`HAVING`, a CTE, a window function, `COALESCE`,
  and a materialized view that itself answers two more questions. Run it
  all through Python (`starter/db.py`, given code) — the analysis itself
  still has to be real SQL; pandas only holds/visualizes a query's result,
  in `starter/visuals.py`.
- **Independently create a read-only database role.**
- **Critique a deliberately flawed schema** someone else designed.
- **Run a real `EXPLAIN ANALYZE` check** on your own most complex query
  and think through how it could be optimized.
- **Write up the real tradeoffs** between the normalized schema you built
  and a STAR (dimensional) schema.

All real, graded pieces of this project, not optional extras.

## Why it matters

This is the first project in the program where you install and use a
genuinely new tool — PostgreSQL — and the first time the data you're
working with lives in more than one linked table instead of a single flat
file. Real business data almost never lives in one spreadsheet: a claim
references a policy, a visit references a patient and a facility, a request
references an agency. Structuring that correctly — and being able to ask a
real question across multiple tables with confidence in the answer — is
what this project is actually testing. It gets used immediately: **Module
4** connects to the exact database you build here from Python, and
**Module 8** builds a full analytics layer on top of it — including the
normalized-vs-STAR tradeoff you write up here, and the query-optimization
work your `EXPLAIN ANALYZE` check previews, both revisited for real.

## Deliverables at a glance

- A **public GitHub repo**, created from the template via "Use this
  template" (not Fork).
- One domain chosen from `SCENARIOS.md`.
- [`starter/schema.sql`](starter/schema.sql) — a PostgreSQL schema you
  designed yourself (3 tables minimum, normalized to **at least 3NF**),
  with correct primary keys, foreign keys, and at least one real
  constraint per table.
- The real per-table data for your domain loaded into your schema.
- [`starter/queries.sql`](starter/queries.sql) — your domain's 7 given
  business questions, each answered by real, verified SQL — a join, a
  left join, `GROUP BY`/`HAVING`, a CTE, a window function, `COALESCE`,
  and a materialized view answering two further questions on top — plus a
  real `EXPLAIN ANALYZE` check on your most complex query, with a genuine
  written assessment, at the end of the same file.
- Every query spot-checked against a small, hand-built sample where you
  already know the right answer, before trusting the full result.
- [`starter/visuals.py`](starter/visuals.py) — at least one query result
  charted with pandas/matplotlib, exported into `images/`.
- [`starter/answers.md`](starter/answers.md) — your schema sketch and 3NF
  reasoning, the 3NF-vs-STAR tradeoff writeup, your critique of a provided
  flawed schema, and your read-only-role writeup.
- A read-only PostgreSQL role you created and granted yourself, no
  template.
- A clean submission and real, incremental commits.

## Skills you'll practice

- **SQL** — writing real joins, aggregation, CTEs, window functions,
  `COALESCE`, and materialized views against live data, not toy examples.
- **Relational Databases** — understanding what primary keys, foreign
  keys, and normalization actually protect against, both by building your
  own schema and by finding real flaws in someone else's.
- **Database Administration** — creating a real PostgreSQL database and
  table structure, and managing access with a role you create yourself.
- **Data Modeling** — going from a plain-language business need to a
  correctly normalized (3NF) table design, and understanding when a
  different design (STAR) would be the better call instead.

## Timeline

4 days, run as a sprint, plus a required share-out session scheduled
after. See [`CHECKLIST_TIMELINE.md`](CHECKLIST_TIMELINE.md) for the
day-by-day sprint pace and the full submission checklist.

## Where to start

Go to [`README.md`](README.md), then
[`GETTING_STARTED.md`](GETTING_STARTED.md) — they walk through getting
your own copy of this repo and getting PostgreSQL running, step by step.
