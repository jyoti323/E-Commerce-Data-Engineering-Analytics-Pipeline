import pandas as pd
from pathlib import Path

#main project folder
BASE_DIR=Path(__file__).resolve().parent.parent
RAW_DATA_DIR= BASE_DIR /"data"/"raw"

DATASET_FILES={
    'Customers':'olist_customers_dataset.csv',
    'Geolocation':'olist_geolocation_dataset.csv',
    'Order_Items':'olist_order_items_dataset.csv',
    'Payments':'olist_order_payments_dataset.csv',
    'Reviews':'olist_order_reviews_dataset.csv',
    'Orders':'olist_orders_dataset.csv',
    'Products':'olist_products_dataset.csv',
    'Sellers':'olist_sellers_dataset.csv',
    'Product_Category_Translation':'product_category_name_translation.csv'
}

def extract_data():
    print("EXTRACTING DATA")

    extracted_data={}
    if not RAW_DATA_DIR.exists():
        raise FileNotFoundError(
            f"Raw data folder not found: {RAW_DATA_DIR}"
        )

    for name, filename in DATASET_FILES.items():

        file_path = RAW_DATA_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"Missing dataset file: {filename}"
            )

        df = pd.read_csv(file_path)

        extracted_data[name] = df

        print(f"Loaded: {filename}")
        print(f"Rows: {len(df)}")
        print(f"Columns: {len(df.columns)}")


    print("\nAll datasets extracted successfully!")

    return extracted_data


if __name__ == "__main__":

    data = extract_data()

    print("\nTotal datasets:", len(data))
