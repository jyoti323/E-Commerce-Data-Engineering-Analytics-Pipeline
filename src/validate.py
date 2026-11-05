
import pandas as pd

REQUIRED_COLUMNS = {
    "orders": [
        "order_id",
        "customer_id",
        "order_status",
        "order_purchase_timestamp"
    ],

    "customers": [
        "customer_id",
        "customer_city",
        "customer_state"
    ],

    "products": [
        "product_id",
        "product_category_name"
    ],

    "order_items": [
        "order_id",
        "order_item_id",
        "product_id",
        "seller_id",
        "price"
    ],

    "payments": [
        "order_id",
        "payment_sequential",
        "payment_type",
        "payment_value"
    ],

    "reviews": [
        "review_id",
        "order_id",
        "review_score"
    ],

    "sellers": [
        "seller_id",
        "seller_city",
        "seller_state"
    ],

    "geolocation": [
        "geolocation_zip_code_prefix",
        "geolocation_lat",
        "geolocation_lng"
    ],

    "category_translation": [
        "product_category_name",
        "product_category_name_english"
    ]
}


def validate_data(data):

    print("\n VALIDATING DATA\n")

    report = {}

    for name, df in data.items():

        print(f"\nChecking dataset: {name}")
        missing_columns = [
            col for col in REQUIRED_COLUMNS[name]
            if col not in df.columns
        ]

        missing_values = int(df.isnull().sum().sum())
        duplicate_rows = int(df.duplicated().sum())
        empty_rows = int(df.isnull().all(axis=1).sum())

        report[name] = {
            "rows": len(df),
            "columns": len(df.columns),
            "missing_values": missing_values,
            "duplicate_rows": duplicate_rows,
            "empty_rows": empty_rows,
            "missing_columns": missing_columns
        }

        print("Rows:", len(df))
        print("Missing values:", missing_values)
        print("Duplicate rows:", duplicate_rows)
        print("Empty rows:", empty_rows)

        if missing_columns:
            print("ERROR: Missing required columns:", missing_columns)
        else:
            print("Required columns: PASS")

    print("\nValidation completed!")

    return report


if __name__ == "__main__":

    from src.extract import extract_data

    data = extract_data()

    report = validate_data(data)

    print("\nFINAL VALIDATION REPORT")

    for name, result in report.items():

        print(name, ":", result)
