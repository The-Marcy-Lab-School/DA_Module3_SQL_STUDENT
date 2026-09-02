# Getting Started

## "Use this template" vs. Fork vs. Clone

Three different buttons/commands that all sound like "get a copy," but do
different things:

- **"Use this template"** (on this repo's GitHub page) ← use this one. It
  creates a brand-new, independent repository under *your* GitHub account,
  with no visible link back to this template. That's what you want for
  something that becomes part of your portfolio.
- **"Fork"** — creates a copy that stays linked to this one (GitHub will
  show "forked from marcy-lab-school/..." on your repo forever). Fork is
  the right tool when you intend to contribute changes back to the original
  project — that's not this. Don't use Fork here.
- **`git clone`** — what you run *after* "Use this template" has created
  your own new repo, to get a working copy on your own machine.

## Installing PostgreSQL

This is genuinely new software — nothing earlier in the program has needed
a real installed database before. Two real options; pick whichever you're
more comfortable with:

### Option A (recommended): a free hosted instance

Create a free PostgreSQL project at **[Supabase](https://supabase.com)** or
**[Neon](https://neon.tech)** — both have a genuinely free tier meant for
exactly this kind of project. Either one gives you a connection string
(host, port, database name, username, password) after you create a project
— save it somewhere you can find it.

**Why this is the recommended default:** it skips local install friction
entirely — you're doing real SQL against a real, live Postgres database
either way, without a service that won't start or a forgotten local
password eating your project time.

### Option B: install it locally (macOS)

[Postgres.app](https://postgresapp.com) is the simplest route — download,
open, click "Initialize." Then get your connection info from the app's own
window (host `localhost`, default port `5432`, default database/user
`postgres`, no password needed for a fresh local install).

### Either way, confirm it works

You won't use the `psql` command-line tool for this project — every
statement you write gets run through Python instead (see below). Confirm
your database is actually reachable by setting `DATABASE_URL` and running
one real query through `starter/db.py`:

```bash
export DATABASE_URL="postgresql://user:password@host:port/dbname"
python3 -c "from starter.db import run_query; print(run_query('SELECT 1;'))"
```

If that doesn't print back a real result, fix your connection now, on Day
1 — don't start designing your schema against a database you haven't
actually confirmed you can reach.

## Running your SQL through Python

This project doesn't use `psql` at all. You write real SQL in real `.sql`
files in VSCode (`starter/schema.sql`, `starter/queries.sql`), and run them
through `starter/db.py` — given code, you don't write this file yourself:

```bash
pip install psycopg2-binary pandas sqlalchemy matplotlib
```

```bash
python3 starter/db.py starter/schema.sql    # creates your tables
python3 starter/db.py starter/queries.sql   # runs all 7 queries, prints each result
```

`starter/db.py` also has `load_csv()` (for loading your domain's data) and
`run_query()` (for running one query string at a time from a Python
session) — see that file's own docstring for the exact usage. The one rule
that applies no matter how you run things: **the analysis itself has to be
real SQL** — pandas may only hold/visualize an already-computed result
(`starter/visuals.py` is where that happens).

## What's next

Once `DATABASE_URL` connects for real, go to `README.md`'s "Your domain and
data" section and pick a domain from `SCENARIOS.md`.
