"""
Given code -- you don't need to write this yourself.

An optional way to run your SQL through Python instead of `psql` directly.
Using this (or not) doesn't change what's graded: the SQL itself still has
to be real, correct, and yours -- this file just gives you a Python-side
way to run it and, if you want, chart the result with pandas/matplotlib.

pandas is for HOLDING and VISUALIZING a query's already-computed result --
not for doing the analysis instead of SQL. Using `.describe()`, `.groupby()`,
or a pandas merge to answer a business question instead of writing the
equivalent SQL query defeats the point of this project, even if the number
comes out right.

Setup (one-time):
    pip install psycopg2-binary pandas sqlalchemy

Set your connection info once:
    export DATABASE_URL="postgresql://user:password@host:port/dbname"

Usage:
    from starter.run_query import run_query
    df = run_query("SELECT * FROM communities LIMIT 5;")

    # or from the command line:
    python3 starter/run_query.py "SELECT * FROM communities LIMIT 5;"
"""
import os
import sys

import pandas as pd
from sqlalchemy import create_engine, text


def run_query(sql: str) -> pd.DataFrame:
    """Run one real SQL query and return the result as a DataFrame."""
    dsn = os.environ.get("DATABASE_URL")
    if not dsn:
        raise SystemExit(
            "Set DATABASE_URL first, e.g.:\n"
            '  export DATABASE_URL="postgresql://user:password@host:port/dbname"'
        )
    engine = create_engine(dsn)
    with engine.connect() as conn:
        return pd.read_sql(text(sql), conn)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python3 starter/run_query.py "SELECT ..."')
    result = run_query(sys.argv[1])
    print(result.to_string(index=False))
    print(f"\n{len(result)} row(s) returned.")
