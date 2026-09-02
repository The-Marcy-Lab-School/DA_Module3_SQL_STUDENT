"""
Given code -- you don't need to write this yourself.

This project doesn't use the `psql` command-line tool at all: you write
real SQL in real .sql files (schema.sql, queries.sql) in VSCode, and run
them through Python using the functions below. pandas is for HOLDING and
VISUALIZING a query's already-computed result -- not for doing the
analysis instead of SQL. Using `.describe()`, `.groupby()`, or a pandas
merge to answer a business question instead of writing the equivalent SQL
query defeats the point of this project, even if the number comes out
right.

Setup (one-time):
    pip install psycopg2-binary pandas sqlalchemy

Set your connection info once (see GETTING_STARTED.md for where this
comes from):
    export DATABASE_URL="postgresql://user:password@host:port/dbname"

Usage:
    from starter.db import run_sql_file, run_query, load_csv, execute

    # Run your whole schema.sql (CREATE TABLE, etc.) in one call:
    run_sql_file("starter/schema.sql")

    # Load a CSV's rows into an already-created table:
    load_csv("data/finance_insurance/communities.csv", "communities")

    # Run every statement in queries.sql and get back one DataFrame per
    # statement that returned rows (SELECT):
    results = run_sql_file("starter/queries.sql", fetch=True)

    # Run one SELECT at a time:
    df = run_query("SELECT * FROM communities LIMIT 5;")

    # Run one one-off statement that doesn't return rows (CREATE ROLE,
    # GRANT, etc. -- see the read-only-role exercise):
    execute("CREATE ROLE analyst_readonly WITH LOGIN PASSWORD '...';")

    # or from the command line:
    python3 starter/db.py starter/schema.sql
    python3 starter/db.py starter/queries.sql
"""
import os
import sys

import pandas as pd
import psycopg2
from sqlalchemy import create_engine, text


def _split_statements(sql_text: str) -> list:
    """
    Split a .sql file's text into individual statements on semicolons,
    ignoring semicolons inside `--` comments or single-quoted strings.
    Good enough for the CREATE TABLE / SELECT / CREATE MATERIALIZED VIEW
    statements this project uses -- not a general-purpose SQL parser.
    """
    lines = []
    for line in sql_text.splitlines():
        stripped = line
        in_quote = False
        for i, ch in enumerate(line):
            if ch == "'":
                in_quote = not in_quote
            if not in_quote and line[i : i + 2] == "--":
                stripped = line[:i]
                break
        lines.append(stripped)
    cleaned = "\n".join(lines)

    statements = []
    current = []
    in_quote = False
    for ch in cleaned:
        if ch == "'":
            in_quote = not in_quote
        if ch == ";" and not in_quote:
            stmt = "".join(current).strip()
            if stmt:
                statements.append(stmt)
            current = []
        else:
            current.append(ch)
    tail = "".join(current).strip()
    if tail:
        statements.append(tail)
    return statements


def _dsn() -> str:
    dsn = os.environ.get("DATABASE_URL")
    if not dsn:
        raise SystemExit(
            "Set DATABASE_URL first, e.g.:\n"
            '  export DATABASE_URL="postgresql://user:password@host:port/dbname"'
        )
    return dsn


def run_query(sql: str) -> pd.DataFrame:
    """Run one real SELECT and return the result as a DataFrame."""
    engine = create_engine(_dsn())
    with engine.connect() as conn:
        return pd.read_sql(text(sql), conn)


def execute(sql: str) -> None:
    """
    Run one real, one-off statement that doesn't return rows -- CREATE
    ROLE, GRANT, INSERT/UPDATE/DELETE, etc. (use run_query() instead for a
    SELECT). Useful for the read-only-role exercise, where you're trying
    commands one at a time rather than running a whole .sql file.
    """
    conn = psycopg2.connect(_dsn())
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
        conn.commit()
    finally:
        conn.close()


def run_sql_file(filepath: str, fetch: bool = False):
    """
    Execute every statement in a .sql file, in order, against DATABASE_URL.

    fetch=False (default): just runs everything -- use this for
    schema.sql-style DDL, where there's nothing to fetch back.

    fetch=True: returns a list of pandas DataFrames, one per statement
    that returned rows (e.g. SELECT) -- use this for queries.sql. DDL
    statements in the same file (like Query 7's CREATE MATERIALIZED VIEW)
    don't add anything to the returned list.
    """
    with open(filepath) as f:
        statements = _split_statements(f.read())

    results = []
    conn = psycopg2.connect(_dsn())
    try:
        with conn.cursor() as cur:
            for stmt in statements:
                cur.execute(stmt)
                if fetch and cur.description is not None:
                    cols = [c.name for c in cur.description]
                    rows = cur.fetchall()
                    results.append(pd.DataFrame(rows, columns=cols))
        conn.commit()
    finally:
        conn.close()
    return results


def load_csv(csv_path: str, table_name: str) -> int:
    """
    Load a CSV file's rows into an already-created table (run schema.sql
    first). The CSV's column names must match the table's column names.
    Returns the number of rows loaded.
    """
    df = pd.read_csv(csv_path)
    engine = create_engine(_dsn())
    df.to_sql(table_name, engine, if_exists="append", index=False)
    return len(df)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python3 starter/db.py <path/to/file.sql>")
    dfs = run_sql_file(sys.argv[1], fetch=True)
    if not dfs:
        print(f"Ran {sys.argv[1]} -- no rows returned (DDL executed).")
    for i, df in enumerate(dfs, 1):
        print(f"\n--- statement {i} result ---")
        print(df.to_string(index=False))
