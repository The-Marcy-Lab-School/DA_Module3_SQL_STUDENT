# MVP — Minimum Bar

One line per requirement. Full grading detail lives in `rubric.md` (ask
your instructor) — this is the scannable bar, not the explanation.

- [ ] One domain chosen from `SCENARIOS.md`; all 7 of that domain's given
  business questions read before any schema design.
- [ ] A schema you designed yourself: **3 tables minimum, normalized to at
  least 3NF** (not just "split into tables" — see `answers.md`), every
  table has a real primary key, every real relationship is expressed as an
  actual foreign key, and every table has at least one `NOT NULL`/`CHECK`
  constraint chosen on purpose.
- [ ] `answers.md`'s "walk through all 7 questions" section completed —
  each question mapped to the table(s)/column(s) it actually needs, before
  `CREATE TABLE`.
- [ ] Schema created for real via `starter/db.py` (not just sketched).
- [ ] Your domain's real data loaded into your schema (`db.py`'s
  `load_csv()`), with row counts confirmed to match the source CSVs.
- [ ] All 7 of your domain's given questions in `queries.sql` answered with
  real, verified SQL: a join, a left join, `GROUP BY`+`HAVING`, a CTE, a
  window function, `COALESCE`, and a materialized view that itself answers
  the two follow-up questions your domain's Q7 asks.
- [ ] Every query is genuine SQL — run through `starter/db.py`, but pandas
  may only hold/visualize a result (in `visuals.py`), never substitute for
  the SQL itself (no `.describe()`/`.groupby()` doing the actual analysis).
- [ ] Every query spot-checked against a small, hand-built known-answer
  sample before being trusted against the full tables — and that check is
  actually documented, not just done silently.
- [ ] A read-only Postgres role independently created, granted, and
  verified (including confirming a write is rejected) — no template used,
  written up in `answers.md`.
- [ ] `answers.md`'s schema-critique section completed with a real,
  specific flaw identified in `SCENARIOS.md`'s given flawed schema.
- [ ] The query-performance section at the end of `queries.sql` completed
  — a real `EXPLAIN ANALYZE` run against your own most complex query, with
  a genuine written assessment (not a description of what you'd expect to
  see).
- [ ] The 3NF-vs-STAR schema tradeoff section in `answers.md` completed,
  reasoned against your own actual tables and queries — not a generic
  textbook answer.
- [ ] `visuals.py` completed — at least one real query result charted with
  pandas/matplotlib, exported to `images/`.
- [ ] Public GitHub repo, real incremental commits (not one at the end),
  accurate `README.md`.

**Don't soften this bar** — but don't add to it either. Everything past
this line is `ABOVE_AND_BEYOND.md`, not part of MVP.
