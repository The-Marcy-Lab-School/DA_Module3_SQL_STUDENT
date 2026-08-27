# SQL & Relational Databases Project

Start with `PROJECT_OVERVIEW.md` for what you're building and why. This
file (`README.md`) is where the step-by-step setup lives.

**Due:** 7 days, run as a sprint. See `CHECKLIST_TIMELINE.md` for the
day-by-day pace, what "sprint"/"backlog" mean here, and the full
submission checklist.

This repo is a **GitHub template** — a starting point, not something you
edit directly on Marcy's copy of it.

## Getting started

### Step 1: Get your own copy

On this repo's GitHub page, click **"Use this template" → "Create a new
repository"** (not Fork — Fork keeps a visible link back to this template,
which isn't what you want for a portfolio project). Name it something like
`sql-relational-databases`, keep it **public**, and create it. See
`GETTING_STARTED.md` if you want the full explanation of why.

### Step 2: Clone your new repo locally

```bash
git clone <the URL of your own new repo>
cd <your-repo-name>
```

### Step 3: Install PostgreSQL and confirm `psql` works

See `GETTING_STARTED.md` — this is genuinely new software, not something
from an earlier module, so it gets its own dedicated setup walkthrough.

### Step 4: Confirm your environment — the basics are already set up

Unlike Module 3's own new tool (Postgres), git itself isn't being newly
tested this module — `.gitignore`, `LICENSE`, and a real git history are
already here:

```bash
ls -a          # should show .gitignore among the files
cat LICENSE    # should show the MIT License text
git log --oneline
```

**One real edit still needed:** open `LICENSE` and replace the placeholder
`[YOUR NAME]` on the copyright line with your actual name. Commit that
change (a real, descriptive commit message you write yourself) alongside
your other early commits.

## Your domain and data

See `SCENARIOS.md` and pick **one** of the 4 stakeholder domains. Each
domain's real data is already included at `data/<domain>/` — see
`data/SOURCE.md` for exactly what each file is, where it's really from, and
what's genuinely messy or worth knowing about it before you design your
schema. **Your domain's 7 business questions are given in `SCENARIOS.md`
too, not yours to write** — each one is deliberately built to require a
specific SQL technique (a join, a left join, `GROUP BY`/`HAVING`, a CTE, a
window function, `COALESCE`, and a materialized view answering two more
questions on top). Delete the other 3 domain folders from `data/` once
you've chosen.

## What to do

See `starter/` for the templates you'll actually fill in: a schema-design
worksheet (map your domain's 7 given questions to your schema **before**
any SQL, and normalize it to **at least 3NF**), a `queries.sql` stub with
one `-- TODO:` per required query, a query-performance check
(`query_performance.md` — a real `EXPLAIN ANALYZE` look at your own most
complex query), and the flawed-schema critique exercise.
`CHECKLIST_TIMELINE.md` has the suggested day-by-day pace and the full
sequenced checklist. Commit incrementally as you go — after your schema is
created, again after data is loaded, again after your queries pass
verification — not one commit at the very end.

**Running your SQL — `psql` or Python, your choice, but the SQL has to be
real:** run every query directly via `psql`, or, if you'd rather work in a
notebook/script, use the given `starter/run_query.py` helper to run a
query through Python and pull the result into a pandas `DataFrame` — either
is fine. What's **not** fine: using pandas to actually do the analysis
(`.describe()`, `.groupby()`, a pandas merge standing in for a join) instead
of writing the real SQL. Every one of the 7 required questions has to be
answered with genuine SQL, checked and correct — pandas' only legitimate
role here is holding a query's already-computed result and, optionally,
charting it.

**Where's the exact bar for "done," and what are the optional stretch
goals?** This repo (your own copy) doesn't include `MVP.md` (your **M**inimum **V**iable **P**roduct —
the required baseline) or `ABOVE_AND_BEYOND.md` on purpose — they're not something to keep sitting in
your portfolio repo. Ask your instructor for the link to this template's
`project-scope` branch (it'll look like `.../tree/project-scope` on the
*template's* GitHub page, not your own copy) to read them, or check the
checklist your instructor shares through the classroom, which covers the
same ground.
