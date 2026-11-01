import os

import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(os.environ["DATABASE_URL"])

with engine.connect() as connection:
    print("Successfully connected to the database!")

df = pd.read_csv(
    "data/raw/olist_orders_dataset.csv"
)

df.to_sql(
    "orders",
    engine,
    schema="raw",
    if_exists="replace",
    index=False
)

print("Orders loaded successfully!")
