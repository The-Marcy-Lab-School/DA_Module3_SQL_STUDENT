"""
Preview of Module 4 -- code given, you don't need to write this yourself.

Connects to YOUR OWN Postgres database (the one you built this project's
schema in) from Python, then runs the first completed query from your own
queries.sql through it -- a real look at what Module 4 (Python for Data
Analysis & Database Connectivity, the very next module) builds on.

Setup (one-time):
    pip install psycopg2-binary pandas sqlalchemy

Before running, set your connection info as an environment variable --
whichever your provider gave you:
    export DATABASE_URL="postgresql://user:password@host:port/dbname"

Run from the starter/ directory (so queries.sql is found), or pass a path:
    python3 ../above_and_beyond/module4_preview.py [path/to/queries.sql]
"""
import os
import sys

import pandas as pd
from sqlalchemy import create_engine


def load_first_completed_query(path):
    with open(path) as f:
        text = f.read()
    # Drop full-line comments, keep everything else.
    lines = [ln for ln in text.splitlines() if not ln.strip().startswith("--")]
    cleaned = "\n".join(lines)
    statements = [s.strip() for s in cleaned.split(";") if s.strip()]
    for statement in statements:
        if "TODO" not in statement.upper():
            return statement
    raise ValueError(
        f"No completed query found in {path} yet -- finish your MVP "
        "queries first, then come back to this."
    )


def main():
    query_path = sys.argv[1] if len(sys.argv) > 1 else "queries.sql"
    query = load_first_completed_query(query_path)

    print("Running your own query through Python:\n")
    print(query, "\n")

    dsn = os.environ.get("DATABASE_URL")
    if not dsn:
        raise SystemExit(
            "Set DATABASE_URL first, e.g.:\n"
            '  export DATABASE_URL="postgresql://user:password@host:port/dbname"'
        )
    engine = create_engine(dsn)

    df = pd.read_sql(query, engine)

    print(df.to_string(index=False))
    print(f"\n{len(df)} row(s) returned.")


if __name__ == "__main__":
    main()
