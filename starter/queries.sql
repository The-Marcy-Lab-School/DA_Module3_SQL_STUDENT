-- Your 5 graded business-question queries, run against your own schema.
-- Write the business questions themselves in business_questions_and_schema.md
-- first -- these should answer the exact same 5 questions, not new ones you
-- think of while writing SQL.
--
-- Run these via `psql`, or via Python using the given `starter/run_query.py`
-- helper -- either is fine. What's NOT fine: using pandas (.describe(),
-- .groupby(), a pandas merge) to do the actual analysis instead of writing
-- the real SQL below. Every query here has to be genuine, correct SQL --
-- pandas' only allowed role, if you use it at all, is holding/visualizing a
-- query's already-computed result.
--
-- Across these 5 queries, your query set as a whole needs to include:
--   - an inner join, with a row count you've actually checked is correct
--   - a left join, with a row count you've actually checked is correct
--     (and that's genuinely different from the inner join's count on your
--     data -- if it isn't, you haven't found a real left-join case yet)
--   - GROUP BY with HAVING, answering a real "which groups meet some
--     condition" question, not just a plain GROUP BY
--   - at least one CTE (WITH ... AS (...) ...), used because it makes a
--     multi-step question more readable, not just for its own sake
--   - a window function (e.g. RANK() OVER (...)), answering a real
--     ranking/"top N by category" question
--
-- Before you trust ANY of these against your full tables: hand-build a
-- tiny sample (3-5 rows) where you already know the right answer, run the
-- same query logic against it, and confirm it matches. Note in a comment
-- above each query that you did this, and what you checked.

-- Query 1 — business question:
-- TODO: your business question here
-- TODO: your SQL here

-- Query 2 — business question:
-- TODO: your business question here
-- TODO: your SQL here

-- Query 3 — business question:
-- TODO: your business question here
-- TODO: your SQL here

-- Query 4 — business question:
-- TODO: your business question here
-- TODO: your SQL here

-- Query 5 — business question (window function):
-- TODO: your business question here
-- TODO: your SQL here
