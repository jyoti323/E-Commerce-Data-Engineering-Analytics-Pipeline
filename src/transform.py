
import pandas as pd

DATE_COLUMNS = {
    "orders": [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ],

    "reviews": [
        "review_creation_date",
        "review_answer_timestamp"
    ]
}

NUMERIC_COLUMNS = {
    "order_items": [
        "order_item_id",
        "price",
        "freight_value"
    ],

    "payments": [
        "payment_sequential",
        "payment_installments",
        "payment_value"
    ],

    "reviews": [
        "review_score"
    ],

    "products": [
        "product_weight_g",
        "product_length_cm",
        "product_height_cm",
        "product_width_cm"
    ]
}


def transform_data(data):

    print("\nTRANSFORMING DATA\n")

    transformed_data = {}

    for name, df in data.items():

        print("Cleaning:", name)

        # Work on a copy of the original dataset
        df = df.copy()

        # Remove completely empty rows
        df = df.dropna(how="all")

        # Remove exact duplicate records
        df = df.drop_duplicates()

        # Clean text columns
        for col in df.select_dtypes(include=["object"]).columns:

            df[col] = df[col].str.strip()

            df[col] = df[col].replace("", pd.NA)

        # Convert date columns
        for col in DATE_COLUMNS.get(name, []):

            if col in df.columns:

                df[col] = pd.to_datetime(
                    df[col],
                    errors="coerce"
                )

        # Convert numerical columns
        for col in NUMERIC_COLUMNS.get(name, []):

            if col in df.columns:

                df[col] = pd.to_numeric(
                    df[col],
                    errors="coerce"
                )

        # Save transformed DataFrame
        transformed_data[name] = df

        print("Cleaned rows:", len(df))
        print("Remaining columns:", len(df.columns))
        print("Transformation completed!")

    print("\nAll datasets transformed successfully!")

    return transformed_data


if __name__ == "__main__":

    from src.extract import extract_data

    data = extract_data()

    cleaned_data = transform_data(data)

    print("\nTotal transformed datasets:", len(cleaned_data))


