# Checklist & Timeline — 5 Days

This project runs as **one sprint**, 5 days long. Every item below is also
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
  from your local `data/`.
- [ ] `data/SOURCE.md` read for your domain — what's real, what's genuinely
  missing/messy, and what the real foreign-key relationship actually is
  (it may not be what you'd first assume).
- [ ] `starter/business_questions_and_schema.md`: your **5** business
  questions written down **first**, then your **3-table-minimum schema,
  normalized to at least 3NF**, sketched — PKs, FKs, at least one real
  constraint per table — on paper or in the file, before any
  `CREATE TABLE`.

## Day 2 — Schema critique, then build your real schema

- [ ] `starter/schema_critique.md` completed — a real, specific flaw
  identified in the given flawed schema, not a style nitpick.
  > ⚠️ Common mistake: a schema with no foreign keys at all, so nothing
  > actually enforces the relationships between tables — this is exactly
  > what the critique exercise is designed to catch you noticing (or not).
- [ ] `starter/schema.sql` written and run for real via `psql` — your own
  3+ tables created, **normalized to at least 3NF**, with real primary
  keys, real foreign keys, and at least one `NOT NULL`/`CHECK` constraint
  per table.
  > ⚠️ Common mistake: skipping `NOT NULL`/`CHECK` constraints because the
  > data "looks clean" — a constraint is what catches bad data on *insert*,
  > not something you add after you've already found a problem.
- [ ] Commit: a real, descriptive message you write yourself.

**Daily check-in.**

## Day 3 — Load your data, write and verify your first queries

- [ ] Your domain's real per-table CSVs loaded into your schema (`\copy` or
  `INSERT`) — confirm row counts in Postgres actually match the source
  CSVs before moving on.
- [ ] Inner join and left join queries written in `starter/queries.sql`,
  each answering one of your 5 business questions. Run these via `psql` or
  via `starter/run_query.py` — your choice, but the SQL has to be real
  either way.
- [ ] Both joins **spot-checked against a small, hand-built sample** where
  you already know the right answer — before trusting the full-table
  result.
  > ⚠️ Common mistake: trusting a query because the output "looks right"
  > without ever checking it against known values — and separately, a join
  > that silently produces duplicate rows because the join key isn't
  > actually unique on one side. Both are real risks with real joins, not
  > hypothetical.
- [ ] Commit: a real, descriptive message you write yourself.

**Exit criterion:** at least 2 real commits pushed to GitHub by end of Day
3 — `git log --oneline` should already tell a real story.

**Daily check-in.**

## Day 4 — GROUP BY/HAVING, a CTE, a window function, and the read-only role

- [ ] Remaining 3 queries in `starter/queries.sql` written: a `GROUP
  BY`/`HAVING` query answering a real "which groups meet some condition"
  question, a query restructured as a CTE because it genuinely makes a
  multi-step question more readable, and a window function query
  answering a real ranking/"top N by category" question.
  > ⚠️ Common mistake: reaching for pandas (`.describe()`, `.groupby()`) to
  > answer one of these instead of writing the real SQL — that's not
  > allowed even if you're running things through `starter/run_query.py`.
- [ ] All 5 queries spot-checked against a known-answer sample, same
  discipline as Day 3 — not just the two joins.
- [ ] `starter/role_setup.md` completed — a real read-only role created,
  granted, and verified (including confirming a write is actually
  rejected), written up with the real commands you used.
- [ ] Commit: a real, descriptive message you write yourself.

**Daily check-in.**

## Day 5 — Schema tradeoffs, finish, verify, submit

- [ ] The 3NF-vs-STAR schema design tradeoff section in
  `starter/business_questions_and_schema.md` completed — reasoned against
  your own actual tables and queries, not a generic definition of either.
- [ ] Final pass: every query in `queries.sql` re-run clean against the
  real schema, no leftover scratch queries or debugging output.
- [ ] `README.md` accurate; repo confirmed **public**.
- [ ] Final self-check against this checklist before calling it done.
- [ ] Commit(s) pushed — `git log --oneline` should show real, incremental
  history, not one giant final commit.

**Exit criterion:** everything above is done and pushed. That's the whole
sprint. Backlog items (`ABOVE_AND_BEYOND.md`) are exactly that — backlog.
Picking one up after Day 5, if you have real time, is a bonus sprint, not a
requirement of this one.

## After Day 5: peer schema & query review

Right after Day 5 (or in a separate session), your instructor will run an
anonymized peer review of schemas and query sets — reviewed as an analyst
who'd have to extend the database, not as a grader. No extra prep needed —
just have your repo pushed and public.

## Above & Beyond

Only the additional items — everything above still applies and isn't
repeated here. Details in `ABOVE_AND_BEYOND.md`.

- [ ] Extend your schema to 4-5 tables with a genuine additional
  relationship.
- [ ] Actually build the STAR schema from your tradeoff writeup and rewrite
  1-2 queries against it.
- [ ] Use DBeaver to generate and export a visual ERD of your own schema.
- [ ] Run the given-code `above_and_beyond/module4_preview.py` (Module 4
  preview) and write a short reflection on what it shows you.
