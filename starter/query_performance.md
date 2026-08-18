# Query Performance Check

Pick your most complex query from `queries.sql` (Query 4, 5, or 7 are the
usual candidates — anything with a CTE, a window function, or a
materialized-view join). Run it with `EXPLAIN ANALYZE` in front of it:

```sql
EXPLAIN ANALYZE
SELECT ...  -- your actual query
```

This isn't the deep optimization work Module 7 covers later — that's a
real, separate module. This is a first, real look at what your query is
actually doing under the hood, and forming a genuine opinion about it.

## Which query did you check?

> TODO

## Paste the real `EXPLAIN ANALYZE` output here

```
TODO — paste your actual output, not a description of it
```

## Your assessment

- Is Postgres using a sequential scan or an index scan on your join/filter
  columns? Does that seem reasonable given how much data is in your
  tables, or does it surprise you?

  > TODO

- What's the single most expensive step in this plan (highest actual time)?

  > TODO

- If this query needed to run fast, repeatedly, on much more data than you
  have here, what's the first thing you'd look at changing — an index, a
  rewrite, something else? You don't need to actually build it (that's
  real optimization work, Module 7's job) — just name a specific, real
  next step and why.

  > TODO
