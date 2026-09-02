"""
Chart at least one of your queries.sql results -- pandas/matplotlib only
chart an already-computed query result here, they never do the analysis
itself. The SQL in queries.sql has to already be the real, correct answer;
this file just visualizes it.

Run:
    python3 starter/visuals.py
"""
import matplotlib.pyplot as plt

from db import run_query

# TODO: paste one of your real, working queries from queries.sql here --
# a ranking/aggregate query (Q3, Q5, or Q7 are natural fits for a bar
# chart) usually makes the clearest chart.
SQL = """
-- TODO: your query here
"""

df = run_query(SQL)
print(df.to_string(index=False))

# TODO: build a real chart from `df` -- a horizontal bar chart of a
# ranking, e.g.:
#   fig, ax = plt.subplots(figsize=(8, 5))
#   ax.barh(df["some_label_column"], df["some_value_column"])
#   ax.set_xlabel("...")
#   ax.set_title("...")
#   plt.tight_layout()

# TODO: save it into images/ (create the folder if it doesn't exist yet),
# not the repo root:
#   plt.savefig("../images/your_chart_name.png", dpi=120)
#   print("Saved images/your_chart_name.png")
