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
  your own new repo, to get a working copy on your own machine. Cloning
  this template directly (instead of your own copy of it) means you'd be
  pushing back to Marcy's repo, which you don't have access to and don't
  want anyway.

## Installing PostgreSQL

This is genuinely new software — nothing earlier in the program has needed
a real installed database before. You have two real options; pick whichever
you're more comfortable with, but read the reasoning before you choose,
since it affects how much of your 5-day sprint gets eaten by setup:

### Option A (recommended): a free hosted instance

Create a free PostgreSQL project at **[Supabase](https://supabase.com)** or
**[Neon](https://neon.tech)** — both have a genuinely free tier meant for
exactly this kind of project. Either one gives you a connection string
(host, port, database name, username, password) after you create a project
— save it somewhere you can find it, you'll need it every time you connect.

**Why this is the recommended default:** installing Postgres locally is a
different process on every operating system (Homebrew on macOS, an
installer on Windows, `apt`/`dnf` on Linux), and getting it wrong (a
service that won't start, a `PATH` that doesn't include `psql`, a password
you forgot you set) is exactly the kind of setup friction that eats real
project time without teaching you any of this project's actual graded
skills. A hosted instance skips all of that — you're doing real SQL against
a real, live Postgres database either way.

### Option B: install it locally

- **macOS:** [Postgres.app](https://postgresapp.com) is the simplest
  route — download, open, click "Initialize." It adds `psql` to your
  terminal once you follow its own "Configure your `$PATH`" step (the app
  shows you exactly what to add — the app's own instructions are the ones
  to follow here, not something to guess at).
- **Windows/Linux:** use the official installer at
  [postgresql.org/download](https://www.postgresql.org/download/) for your
  OS — pick the current stable major version.

### Either way, confirm it works

```bash
psql --version
```

Then connect for real (hosted: use the connection string your provider
gave you; local: `psql postgres` usually works out of the box) and confirm
you get a `postgres=#` (or similar) prompt. If you can't connect, fix that
now, on Day 1 — don't start designing your schema against a database you
haven't actually confirmed you can reach.

## What's next

Once `psql` connects for real, go back to `README.md`'s "Your domain and
data" section and pick a domain from `SCENARIOS.md`.
