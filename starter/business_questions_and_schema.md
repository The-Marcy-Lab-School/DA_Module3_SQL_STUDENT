# Business Questions & Schema Design

Fill this in **before you write any SQL** — design before code, same
discipline as every project so far. A strong schema comes from knowing
exactly what questions it needs to answer; a schema designed first and
questions written after almost always ends up missing a column or a table
you actually needed.

## Your domain

Domain: _______________ (from `SCENARIOS.md`)

Stakeholder's business problem, in your own words:

> TODO

## Your 4 business questions

Write these first. Each one becomes a real, graded query later — so make
each one specific enough that you could recognize a right answer if you saw
one (that's what Day 3's "check it against a sample where you already know
the answer" step depends on).

1. TODO
2. TODO
3. TODO
4. TODO

At least one of these needs to be answerable with a join returning rows
that *don't* have a match on the other side (a real left-join case, not
just an inner join) — look at your domain's data in `data/<domain>/` before
you finalize your questions, and pick one that's genuinely true of your
data, not assumed.

## Your schema sketch (paper or here — before any `CREATE TABLE`)

For each table (3 minimum): name, columns with real types, which column is
the primary key, which columns are foreign keys and what they reference,
and at least one other real constraint (`NOT NULL` or `CHECK`) you're
choosing on purpose and can explain why.

```
TODO — table 1
TODO — table 2
TODO — table 3
```

Why did you choose this split into tables (not one flat table, not more
tables than this)? One or two real sentences — "because the assignment
says so" isn't a reason.

> TODO
