# Project Overview: SQL & Relational Databases

## The objective

Pick one of 4 real stakeholder domains (`SCENARIOS.md`), then design and
build a real, normalized PostgreSQL database for it: 3 tables minimum, with
primary keys, foreign keys, and at least one real constraint per table —
your own design, not handed to you. Load the real (or clearly-labeled
synthetic) data into it, then write and verify a set of SQL queries — joins,
`GROUP BY`/`HAVING`, and at least one CTE — that actually answer your
stakeholder's business problem, run entirely from the terminal via `psql`.
Along the way you'll also independently create a read-only database role
and critique a deliberately flawed schema someone else designed — both real,
graded pieces of this project, not optional extras.

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
**Module 7** builds a full analytics layer on top of it.

## Deliverables at a glance

- A **public GitHub repo**, created from the template via "Use this
  template" (not Fork).
- One domain chosen from `SCENARIOS.md`.
- A normalized PostgreSQL schema you designed yourself (3 tables minimum),
  created via `psql` with correct primary keys, foreign keys, and at least
  one real constraint per table.
- The real per-table data for your domain loaded into your schema.
- 4 business questions, written down before you started designing, each
  answered by a real, verified SQL query — the required set includes an
  inner join, a left join, `GROUP BY`/`HAVING`, and at least one CTE.
- Every query spot-checked against a small, hand-built sample where you
  already know the right answer, before trusting the full result.
- A read-only PostgreSQL role you created and granted yourself, no
  template.
- A short written critique of a provided, deliberately flawed schema.
- A clean submission and real, incremental commits.

## Skills you'll practice

- **SQL** — writing real joins, aggregation, and CTEs against live data,
  not toy examples.
- **Relational Databases** — understanding what primary keys, foreign
  keys, and normalization actually protect against, both by building your
  own schema and by finding real flaws in someone else's.
- **Database Administration** — creating a real PostgreSQL database and
  table structure, and managing access with a role you create yourself.
- **Data Modeling** — going from a plain-language business need to a
  correctly normalized table design.

## Timeline

See `CHECKLIST_TIMELINE.md` for the day-by-day sprint pace and the full
submission checklist.

## Where to start

New here? Go to `README.md`, then `GETTING_STARTED.md` — they walk through
getting your own copy of this repo and getting PostgreSQL running, step by
step.
