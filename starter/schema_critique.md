# Schema Critique

This one isn't about your own domain — it's a schema a (fictional)
colleague wrote for a coffee shop's ordering system. Read it and critique
it for real, in writing. No template for the critique itself; this is meant
to be independent.

```sql
CREATE TABLE customers (
    customer_id INTEGER,
    customer_name TEXT,
    email TEXT
);

CREATE TABLE orders (
    order_id INTEGER,
    customer_name TEXT,
    order_date DATE,
    total_amount NUMERIC
);

CREATE TABLE order_items (
    order_id INTEGER,
    product_name TEXT,
    quantity INTEGER,
    unit_price NUMERIC
);
```

Your colleague also ran this query, saw output that looked plausible, and
moved on without checking it further:

```sql
SELECT c.customer_name, SUM(o.total_amount) AS lifetime_spend
FROM customers c
JOIN orders o ON c.customer_name = o.customer_name
GROUP BY c.customer_name;
```

## Your critique

**Identify at least one real, specific flaw in the schema itself** — not a
style nitpick, an actual structural problem that would cause a real issue
down the line. Name the table(s)/column(s) involved and explain the actual
risk (what breaks, or what silently goes wrong, and when).

> TODO

**Now look at the query.** Is `c.customer_name = o.customer_name` actually
a safe way to connect a customer to their orders? What would have to be
true about the data for this join to be reliable — and what happens to the
result the moment that's not true? (Think about what two different real
customers might have in common.)

> TODO

**Your colleague trusted this query because "the output looked right."**
What should they have done instead, before trusting it — be specific, not
"they should have tested it more."

> TODO

**If you were rebuilding this schema for real, what would you change?**
Sketch the fix — new/changed columns, real keys, real constraints — in a
sentence or two, you don't need full `CREATE TABLE` syntax here.

> TODO
