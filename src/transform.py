import pandas as pd
def transform(df):
    df = df.drop_duplicates()

    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_customer_date"
    ]

    for col in date_columns:
        df[col] = pd.to_datetime(
            df[col],
            errors="coerce"
        )

    df = df.dropna(subset=["order_id"])

    return df


