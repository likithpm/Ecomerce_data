import sqlite3
import pandas as pd
conn = sqlite3.connect("db/ecommerce.db")
cur = conn.cursor()

# create tables
with open("scripts/create_tables.sql","r") as f:
    cur.executescript(f.read())

# load csvs using pandas to_sql (replace existing data)
df_users = pd.read_csv("data/users.csv")
df_products = pd.read_csv("data/products.csv")
df_orders = pd.read_csv("data/orders.csv")
df_order_items = pd.read_csv("data/order_items.csv")
df_payments = pd.read_csv("data/payments.csv")

df_users.to_sql("users", conn, if_exists="replace", index=False)
df_products.to_sql("products", conn, if_exists="replace", index=False)
df_orders.to_sql("orders", conn, if_exists="replace", index=False)
df_order_items.to_sql("order_items", conn, if_exists="replace", index=False)
df_payments.to_sql("payments", conn, if_exists="replace", index=False)

conn.commit()
conn.close()
print("Data ingested into db/ecommerce.db")
