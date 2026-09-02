-- Your domain's 7 graded business-question queries -- see SCENARIOS.md
-- for the exact questions (given, not yours to write this time) and
-- answers.md for how you mapped each one to your schema before writing
-- any SQL here.
--
-- Run this file via Python (see GETTING_STARTED.md and starter/db.py) --
-- not `psql`:
--   python3 starter/db.py starter/queries.sql
-- pandas may only hold/visualize an already-computed query result --
-- using it (.describe(), .groupby(), a merge) to do the actual analysis
-- instead of writing the real SQL below is not allowed.
--
-- Before you trust ANY of these against your full tables: hand-build a
-- tiny sample (3-5 rows) where you already know the right answer, run the
-- same query logic against it, and confirm it matches. Note in a comment
-- above each query that you did this, and what you checked.

-- Query 1 (join):
-- TODO: your SQL here

-- Query 2 (left join):
-- TODO: your SQL here

-- Query 3 (GROUP BY + HAVING):
-- TODO: your SQL here

-- Query 4 (CTE):
-- TODO: your SQL here

-- Query 5 (window function):
-- TODO: your SQL here

-- Query 6 (COALESCE):
-- TODO: your SQL here

-- Query 7 (materialized view -- this one is genuinely more than one
-- statement: CREATE MATERIALIZED VIEW first, then the 2 queries against
-- it that SCENARIOS.md's question 7 actually asks for):
-- TODO: CREATE MATERIALIZED VIEW ...
-- TODO: your first query against the view
-- TODO: your second query against the view


-- ============================================================
-- Query performance check (EXPLAIN)
-- ============================================================
-- Pick your most complex query above (Q4, Q5, or Q7 are the usual
-- candidates -- anything with a CTE, a window function, or a
-- materialized-view join), copy it below prefixed with EXPLAIN ANALYZE,
-- and run this file again -- this is a real, live statement, not just
-- described, so running it reproduces the real plan.
--
-- This isn't the deep optimization work Module 8 covers later -- that's a
-- real, separate module. This is a first, real look at what your query is
-- actually doing under the hood, and forming a genuine opinion about it.

-- TODO: EXPLAIN ANALYZE
-- TODO: <paste your chosen query here, ending in a semicolon>

-- Which query did you check? TODO
--
-- Paste the real EXPLAIN ANALYZE output below, as a comment block --
-- copy it from what actually printed when you ran the statement above,
-- not a description of it:
-- TODO
--
-- Your assessment, as comments:
-- - Is Postgres using a sequential scan or an index scan on your
--   join/filter columns? Does that seem reasonable given how much data is
--   in your tables, or does it surprise you?
--   TODO
-- - What's the single most expensive step in this plan (highest actual
--   time)?
--   TODO
-- - If this query needed to run fast, repeatedly, on much more data than
--   you have here, what's the first thing you'd look at changing -- an
--   index, a rewrite, something else? You don't need to actually build it
--   (that's real optimization work, Module 8's job) -- just name a
--   specific, real next step and why.
--   TODO
