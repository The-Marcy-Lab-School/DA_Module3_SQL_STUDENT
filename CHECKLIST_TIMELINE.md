# Checklist & Timeline — 4 Days + Share-Out

This project runs as **one sprint**, 4 build days plus a share-out day.
Every item below is also the actual submission checklist — work through it
in order, top to bottom. This is your 4th rep of sprint pacing (Modules 1,
2, 3, now this one) — same rules as before: `MVP.md`'s bar is fixed once
you start, do a quick daily check-in (what did I finish, what am I doing
today, what's blocking me), and `ABOVE_AND_BEYOND.md` is this sprint's
backlog — real work, deliberately not in scope this week, not a list of
things you failed to do.

## Day 1 — Design, critique, build your real schema, load data

- [ ] Repo created from the template via **"Use this template"** (not
  Fork), cloned locally — see `README.md`.
- [ ] `DATABASE_URL` set and confirmed connecting for real — see
  `GETTING_STARTED.md`. Don't move on until `run_query("SELECT 1;")`
  actually returns a result.
- [ ] `.gitignore`/`LICENSE`/git history confirmed already present;
  `LICENSE`'s `[YOUR NAME]` placeholder replaced with your actual name,
  committed.
- [ ] One domain chosen from `SCENARIOS.md`; the other 3 folders deleted
  from your local `data/`; all 7 of your domain's given business
  questions read in full.
- [ ] `data/SOURCE.md` read for your domain — what's real, what's genuinely
  missing/messy, and what the real foreign-key relationship actually is
  (it may not be what you'd first assume).
- [ ] `starter/answers.md`'s schema sketch completed — your **3-table-
  minimum schema, normalized to at least 3NF**, sketched (PKs, FKs, at
  least one real constraint per table), every one of your 7 given
  questions walked through against it — before any `CREATE TABLE`.
- [ ] `starter/answers.md`'s schema-critique section completed — a real,
  specific flaw identified in `SCENARIOS.md`'s given flawed schema, not a
  style nitpick.
  > ⚠️ Common mistake: a schema with no foreign keys at all, so nothing
  > actually enforces the relationships between tables — this is exactly
  > what the critique exercise is designed to catch you noticing (or not).
- [ ] `starter/schema.sql` written and run for real (`python3 starter/db.py
  starter/schema.sql`) — your own 3+ tables created, **normalized to at
  least 3NF**, with real primary keys, real foreign keys, and at least one
  `NOT NULL`/`CHECK` constraint per table, each chosen on purpose and
  explained in `answers.md`.
  > ⚠️ Common mistake: skipping `NOT NULL`/`CHECK` constraints because the
  > data "looks clean" — a constraint is what catches bad data on *insert*,
  > not something you add after you've already found a problem.
- [ ] Your domain's real per-table CSVs loaded into your schema
  (`starter/db.py`'s `load_csv()`) — confirm row counts in Postgres
  actually match the source CSVs before moving on.
- [ ] Commit: a real, descriptive message you write yourself.

**Exit criterion:** at least 2 real commits pushed to GitHub by end of Day
1 — `git log --oneline` should already tell a real story.

**Daily check-in.**

## Day 2 — Questions 1-4

- [ ] Question 1 (join), Question 2 (left join), Question 3 (`GROUP BY`+
  `HAVING`), and Question 4 (CTE) answered in `starter/queries.sql`. Run
  the whole file via `python3 starter/db.py starter/queries.sql`.
- [ ] Every one of the 4 **spot-checked against a small, hand-built
  sample** where you already know the right answer — before trusting the
  full-table result.
  > ⚠️ Common mistake: trusting a query because the output "looks right"
  > without ever checking it against known values — and separately, a join
  > that silently produces duplicate rows because the join key isn't
  > actually unique on one side. Both are real risks with real joins, not
  > hypothetical.
- [ ] Commit: a real, descriptive message you write yourself.

**Daily check-in.**

## Day 3 — Questions 5-7 and the performance check

- [ ] Question 5 (window function) and Question 6 (`COALESCE`) answered
  and spot-checked.
  > ⚠️ Common mistake: reaching for pandas (`.describe()`, `.groupby()`) to
  > answer one of these instead of writing the real SQL — not allowed even
  > though everything runs through Python.
- [ ] Question 7 answered: `CREATE MATERIALIZED VIEW` for real, then the
  two follow-up queries your domain's Q7 asks, both run against the view
  (not recomputed from the base tables from scratch).
- [ ] The query-performance section at the end of `queries.sql` completed
  — a real `EXPLAIN ANALYZE` run (as a live statement in the file, not
  just described) against your own most complex query, with a genuine
  written assessment of the plan as SQL comments.
- [ ] Commit: a real, descriptive message you write yourself.

**Exit criterion:** at least 2 more real commits pushed to GitHub by end
of Day 3 — `git log --oneline` should already tell a real story.

**Daily check-in.**

## Day 4 — Role, tradeoffs, visuals, finish, submit

- [ ] A real read-only Postgres role created, granted, and verified
  (including confirming a write is actually rejected), written up with
  the real commands you used in `starter/answers.md`'s read-only-role
  section.
- [ ] The 3NF-vs-STAR schema design tradeoff section in
  `starter/answers.md` completed — reasoned against your own actual
  tables and queries, not a generic definition of either.
- [ ] `starter/visuals.py` completed — at least one real query result
  charted with pandas/matplotlib, exported into an `images/` folder at
  your repo root (create it if it doesn't exist).
- [ ] Final pass: `queries.sql` re-run clean via `starter/db.py` against
  the real schema, no leftover scratch queries or debugging output.
- [ ] **Replace `README.md`'s content with your own real project README**
  — write it for someone who's never seen this assignment:
  - **Business Questions** — the ones your schema was built to answer.
  - **Schema Design & Rationale** — your real 3NF-vs-star tradeoff call.
  - **Key Queries & Insights** — what Q1-Q7 actually revealed.
  - **Visualizations** — your chart(s) from `images/`, embedded with
    markdown, not just described.
  - **Recommendations** — what you'd tell a stakeholder to do next.
- [ ] Final self-check against this checklist before calling it done.
- [ ] **Delete `PROJECT_OVERVIEW.md`, `SCENARIOS.md`, `GETTING_STARTED.md`,
  and this file (`CHECKLIST_TIMELINE.md`)** — now that their content is
  captured in your real README, they're just "here's what you were asked
  to build" clutter that shouldn't sit in a real portfolio repo.
- [ ] Final push to GitHub — confirm the repo is actually **public** (open
  it in a private/incognito browser window to check).
- [ ] Commit(s) pushed — `git log --oneline` should show real, incremental
  history, not one giant final commit.

**Exit criterion:** everything above is done and pushed. That's the whole
sprint. Backlog items (`ABOVE_AND_BEYOND.md`) are exactly that — backlog.
Picking one up after Day 4, if you have real time, is a bonus sprint, not
a requirement of this one.

## Day 5 — Share-out

Your instructor schedules this once every submission is in — usually a
few days after Day 4, not necessarily the next calendar day. Real session,
not optional: in groups of 3, you'll review 2-3 anonymized classmates'
`schema.sql`, `queries.sql`, and `answers.md` as an analyst who'd
genuinely have to extend that database, filling in a shared doc on schema
design, constraints, join risk, and verification, then reporting patterns
back to the class. No extra prep needed — just have your repo pushed and
public — see your instructor for the exact date.

## Above & Beyond

Only the additional items — everything above still applies and isn't
repeated here. Details in `ABOVE_AND_BEYOND.md`.

- [ ] Extend your schema to 4-5 tables with a genuine additional
  relationship.
- [ ] Actually build the STAR schema from your tradeoff writeup and rewrite
  1-2 queries against it.
- [ ] Take your performance check one step further: add an index or
  rewrite, and show a real, measured improvement.
- [ ] Use DBeaver to generate and export a visual ERD of your own schema.
- [ ] Run the given-code `above_and_beyond/module4_preview.py` (Module 4
  preview) and write a short reflection on what it shows you.
