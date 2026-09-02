# SQL & Relational Databases Project

Start with [`PROJECT_OVERVIEW.md`](PROJECT_OVERVIEW.md) for what you're
building and why. This file (`README.md`) is where the step-by-step setup
lives.

**Due:** 4 days, run as a sprint, plus a required share-out session
scheduled after. See [`CHECKLIST_TIMELINE.md`](CHECKLIST_TIMELINE.md) for
the day-by-day pace, what "sprint"/"backlog" mean here, and the full
submission checklist.

This repo is a **GitHub template** — a starting point, not something you
edit directly on Marcy's copy of it.

## Getting started

### Step 1: Get your own copy

On this repo's GitHub page, click **"Use this template" → "Create a new
repository"** (not Fork — Fork keeps a visible link back to this template,
which isn't what you want for a portfolio project). Name it something like
`sql-relational-databases`, keep it **public**, and create it. See
[`GETTING_STARTED.md`](GETTING_STARTED.md) if you want the full
explanation of why.

### Step 2: Clone your new repo locally

```bash
git clone <the URL of your own new repo>
cd <your-repo-name>
```

### Step 3: Install PostgreSQL and confirm you can connect

See [`GETTING_STARTED.md`](GETTING_STARTED.md) — this is genuinely new
software, not something from an earlier module, so it gets its own
dedicated setup walkthrough. It also covers how you'll run SQL for this
project: **through Python, via the given [`starter/db.py`](starter/db.py)
— not the `psql` command-line tool.**

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

See [`SCENARIOS.md`](SCENARIOS.md) and pick **one** of the 4 stakeholder
domains. Each domain's real data is already included at `data/<domain>/`
— see [`data/SOURCE.md`](data/SOURCE.md) for exactly what each file is,
where it's really from, and what's genuinely messy or worth knowing about
it before you design your schema. **Your domain's 7 business questions are
given in `SCENARIOS.md` too, not yours to write** — each one is
deliberately built to require a specific SQL technique (a join, a left
join, `GROUP BY`/`HAVING`, a CTE, a window function, `COALESCE`, and a
materialized view answering two more questions on top). Delete the other 3
domain folders from `data/` once you've chosen.

## What to do

See [`starter/`](starter/) for the 4 files you'll actually fill in:

- [`starter/answers.md`](starter/answers.md) — your schema sketch (map
  your domain's 7 given questions to your schema **before** any SQL, and
  normalize to **at least 3NF**), the 3NF-vs-STAR tradeoff writeup, the
  flawed-schema critique, and the read-only-role writeup.
- [`starter/schema.sql`](starter/schema.sql) — your real `CREATE TABLE`
  statements, one `-- TODO:` per table.
- [`starter/queries.sql`](starter/queries.sql) — one `-- TODO:` per
  required query, plus a query-performance section (a real `EXPLAIN
  ANALYZE` check on your own most complex query) at the end.
- [`starter/visuals.py`](starter/visuals.py) — chart at least one query
  result with pandas/matplotlib, saved into `images/`.

[`CHECKLIST_TIMELINE.md`](CHECKLIST_TIMELINE.md) has the suggested
day-by-day pace and the full sequenced checklist. Commit incrementally as
you go — after your schema is created, again after data is loaded, again
after your queries pass verification — not one commit at the very end.

**Running your SQL — through Python, not `psql`:** every `.sql` file gets
run via [`starter/db.py`](starter/db.py) (given code, you don't write this
one yourself) — see [`GETTING_STARTED.md`](GETTING_STARTED.md) for the
exact commands. What's **not** fine, no matter how you run things: using
pandas to actually do the analysis (`.describe()`, `.groupby()`, a pandas
merge standing in for a join) instead of writing the real SQL. Every one
of the 7 required questions has to be answered with genuine SQL, checked
and correct — pandas' only legitimate role is in `visuals.py`, holding and
charting a query's already-computed result.

**Where's the exact bar for "done," and what are the optional stretch
goals?** This repo (your own copy) doesn't include `MVP.md` (your
**M**inimum **V**iable **P**roduct — the required baseline) or
`ABOVE_AND_BEYOND.md` on purpose — they're not something to keep sitting
in your portfolio repo. Ask your instructor for the link to this
template's `project-scope` branch (it'll look like
`.../tree/project-scope` on the *template's* GitHub page, not your own
copy) to read them, or check the checklist your instructor shares through
the classroom, which covers the same ground.
