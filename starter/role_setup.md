# Read-Only Role

**No template for this one** — this is meant to be a real, independent
exercise, not a fill-in-the-blank. Postgres's own documentation (start at
`\h CREATE ROLE` inside `psql`, or the official docs) has everything you
need; the point is finding and applying the right commands yourself, not
being handed them.

## What you need to end up with

- A new Postgres role (not the one you've been connecting as) that can
  genuinely `SELECT` from your schema's tables.
- Confirmed that this role **cannot** `INSERT`, `UPDATE`, or `DELETE` —
  actually try one of those as the new role and confirm it's rejected, not
  just that you granted `SELECT` and assumed the rest follows.
- Confirmed that connecting *as* this new role and querying your tables
  actually works — a role you never connected as isn't a verified role.

## Write up what you did

In a few sentences below: what commands you used (real ones, from your
real terminal session — paste them, don't reconstruct from memory), what
you tested to confirm it's genuinely read-only, and what happened when you
tried a write as the new role.

> TODO
