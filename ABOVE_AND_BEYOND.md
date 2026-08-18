# Above & Beyond — Backlog

Only the additional items — everything in `MVP.md` still applies and isn't
repeated here. Pick these up only after MVP is genuinely done and pushed;
this is a bonus sprint, not part of this one.

- [ ] **Extend your schema to 4-5 tables** with a genuine additional real
  relationship (not a table added just to hit a number). This previews
  Module 7's schema-layering work directly — Module 7's dbt project
  explicitly builds on top of this module's database, and richer table
  design now is real preparation for that.

- [ ] **Actually build the STAR schema you described in
  `business_questions_and_schema.md`'s tradeoff writeup** — a real fact
  table plus real dimension tables, created via `psql` (a second schema,
  e.g. in its own Postgres database), populated from the same source data,
  with 1-2 of your original 7 queries rewritten against it. Compare: is the
  STAR version's query actually simpler/faster to write for those
  questions? This turns your tradeoff writeup from "explain" into "prove,"
  and previews Module 7's dbt/data-modeling work directly.

- [ ] **Go one step past `query_performance.md`: actually optimize it.**
  MVP only asks you to look at and assess an `EXPLAIN ANALYZE` plan — this
  is the real next step: add an index (or rewrite the query) targeting the
  most expensive operation you found, re-run `EXPLAIN ANALYZE`, and show a
  real, measured improvement (lower cost/actual time, not just "it feels
  faster"). This is close to exactly what Module 7 formally grades under
  `query-optimization` — a genuine head start, not busywork.

- [ ] **Use DBeaver** (already in your `tools` list, optional) to connect
  to your own database and export a visual ERD of your schema. Module 7
  requires tracing column-level lineage through a real lineage graph —
  getting comfortable reading a schema visually now is real preparation
  for that, not just a nice picture.

- [ ] **Preview of Module 4 — code given, you don't need to write this
  yourself.** Run `above_and_beyond/module4_preview.py`, a short given
  script that connects to *your own* database from Python and runs one of
  *your own* queries from `queries.sql` through it. Module 4 (the very
  next module) is "Python for Data Analysis & Database Connectivity" —
  this is a real, working look at exactly what that module builds on, using
  your own real data. Write a short reflection: what was different about
  getting the result through Python vs. `psql` directly, and what would
  you want to be able to do with that connection that plain `psql` doesn't
  give you?
