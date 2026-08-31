# Checklist & Timeline — 7 Days

This project runs as **one sprint**, 7 days long. Every item below is also
the actual submission checklist — work through it in order, top to bottom.
This is your 3rd rep of sprint pacing (Module 1, Module 2, now this one) —
same rules as before: `MVP.md`'s bar is fixed once you start, do a quick
daily check-in (what did I finish, what am I doing today, what's blocking
me), and `ABOVE_AND_BEYOND.md` is this sprint's backlog — real work,
deliberately not in scope this week, not a list of things you failed to do.

## Day 1 — Setup + design, not SQL yet

- [ ] Repo created from the template via **"Use this template"** (not
  Fork), cloned locally — see `README.md`.
- [ ] PostgreSQL running and `psql` confirmed connecting for real — see
  `GETTING_STARTED.md`. Don't move on until you've actually seen a
  `postgres=#`-style prompt.
- [ ] `.gitignore`/`LICENSE`/git history confirmed already present;
  `LICENSE`'s `[YOUR NAME]` placeholder replaced with your actual name,
  committed.
- [ ] One domain chosen from `SCENARIOS.md`; the other 3 folders deleted
  from your local `data/`; all 7 of your domain's given business
  questions read in full.
- [ ] `data/SOURCE.md` read for your domain — what's real, what's genuinely
  missing/messy, and what the real foreign-key relationship actually is
  (it may not be what you'd first assume).
- [ ] `starter/business_questions_and_schema.md`: your **3-table-minimum
  schema, normalized to at least 3NF**, sketched — PKs, FKs, at least one
  real constraint per table — then every one of your 7 given questions
  walked through against it, before any `CREATE TABLE`.

## Day 2 — Schema critique, then build your real schema

- [ ] `starter/schema_critique.md` completed — a real, specific flaw
  identified in the given flawed schema, not a style nitpick.
  > ⚠️ Common mistake: a schema with no foreign keys at all, so nothing
  > actually enforces the relationships between tables — this is exactly
  > what the critique exercise is designed to catch you noticing (or not).
- [ ] `starter/schema.sql` written and run for real via `psql` — your own
  3+ tables created, **normalized to at least 3NF**, with real primary
  keys, real foreign keys, and at least one `NOT NULL`/`CHECK` constraint
  per table, each one chosen on purpose (not just copied in) and explained
  in `business_questions_and_schema.md` per that file's own prompt.
  > ⚠️ Common mistake: skipping `NOT NULL`/`CHECK` constraints because the
  > data "looks clean" — a constraint is what catches bad data on *insert*,
  > not something you add after you've already found a problem.
- [ ] Commit: a real, descriptive message you write yourself.

**Daily check-in.**

## Day 3 — Load your data, answer Q1 and Q2

- [ ] Your domain's real per-table CSVs loaded into your schema (`\copy` or
  `INSERT`) — confirm row counts in Postgres actually match the source
  CSVs before moving on.
- [ ] Question 1 (join) and Question 2 (left join) answered in
  `starter/queries.sql`. Run these via `psql` or via
  `starter/run_query.py` — your choice, but the SQL has to be real either
  way.
- [ ] Both **spot-checked against a small, hand-built sample** where you
  already know the right answer — before trusting the full-table result.
  > ⚠️ Common mistake: trusting a query because the output "looks right"
  > without ever checking it against known values — and separately, a join
  > that silently produces duplicate rows because the join key isn't
  > actually unique on one side. Both are real risks with real joins, not
  > hypothetical.
- [ ] Commit: a real, descriptive message you write yourself.

**Exit criterion:** at least 2 real commits pushed to GitHub by end of Day
3 — `git log --oneline` should already tell a real story.

**Daily check-in.**

## Day 4 — Answer Q3 and Q4

- [ ] Question 3 (`GROUP BY`+`HAVING`) and Question 4 (CTE) answered,
  spot-checked against a known-answer sample, same discipline as Day 3.
- [ ] Commit: a real, descriptive message you write yourself.

**Daily check-in.**

## Day 5 — Answer Q5 and Q6, then the read-only role

- [ ] Question 5 (window function) and Question 6 (`COALESCE`) answered
  and spot-checked.
  > ⚠️ Common mistake: reaching for pandas (`.describe()`, `.groupby()`) to
  > answer one of these instead of writing the real SQL — that's not
  > allowed even if you're running things through `starter/run_query.py`.
- [ ] `starter/role_setup.md` completed — a real read-only role created,
  granted, and verified (including confirming a write is actually
  rejected), written up with the real commands you used.
- [ ] Commit: a real, descriptive message you write yourself.

**Daily check-in.**

## Day 6 — Question 7 (materialized view) and the performance check

- [ ] Question 7 answered: `CREATE MATERIALIZED VIEW` for real, then the
  two follow-up queries your domain's Q7 asks, both run against the view
  (not recomputed from the base tables from scratch).
- [ ] `starter/query_performance.md` completed — a real `EXPLAIN ANALYZE`
  run against your own most complex query (Q4, Q5, or Q7 are the usual
  candidates), with a genuine written assessment of the plan.
- [ ] Commit: a real, descriptive message you write yourself.

**Daily check-in.**

## Day 7 — Schema tradeoffs, finish, verify, submit

- [ ] The 3NF-vs-STAR schema design tradeoff section in
  `starter/business_questions_and_schema.md` completed — reasoned against
  your own actual tables and queries, not a generic definition of either.
- [ ] Final pass: every query in `queries.sql` re-run clean against the
  real schema, no leftover scratch queries or debugging output.
- [ ] **Delete `PROJECT_OVERVIEW.md` and `SCENARIOS.md`** — they explain
  the assignment, not your project; a real portfolio repo shouldn't have
  "here's what you were asked to build" sitting in it.
- [ ] **Replace `README.md`'s content with your own real project README**
  — write it for someone who's never seen this assignment:
  - **Business Questions** — the ones your schema was built to answer.
  - **Schema Design & Rationale** — your real 3NF-vs-star tradeoff call.
  - **Key Queries & Insights** — what Q1-Q7 actually revealed.
  - **Recommendations** — what you'd tell a stakeholder to do next.
- [ ] Final push to GitHub — confirm the repo is actually **public** (open
  it in a private/incognito browser window to check).
- [ ] Final self-check against this checklist before calling it done.
- [ ] Commit(s) pushed — `git log --oneline` should show real, incremental
  history, not one giant final commit.

**Exit criterion:** everything above is done and pushed. That's the whole
sprint. Backlog items (`ABOVE_AND_BEYOND.md`) are exactly that — backlog.
Picking one up after Day 7, if you have real time, is a bonus sprint, not
a requirement of this one.

## Day 8 — Share-out

Your instructor schedules this once every submission is in — usually a
few days after Day 7, not necessarily the next calendar day. Real
session, not optional: in groups of 3, you'll review 2-3 anonymized
classmates' `schema.sql`, `queries.sql`, and
`business_questions_and_schema.md` as an analyst who'd genuinely have to
extend that database, filling in a shared doc on schema design,
constraints, join risk, and verification, then reporting patterns back to
the class. No extra prep needed — just have your repo pushed and public
— see your instructor for the exact date.

## Above & Beyond

Only the additional items — everything above still applies and isn't
repeated here. Details in `ABOVE_AND_BEYOND.md`.

- [ ] Extend your schema to 4-5 tables with a genuine additional
  relationship.
- [ ] Actually build the STAR schema from your tradeoff writeup and rewrite
  1-2 queries against it.
- [ ] Take `query_performance.md` one step further: add an index or
  rewrite, and show a real, measured improvement.
- [ ] Use DBeaver to generate and export a visual ERD of your own schema.
- [ ] Run the given-code `above_and_beyond/module4_preview.py` (Module 4
  preview) and write a short reflection on what it shows you.
