import pandas as pd
import os

data_path="data/raw"

for file in os.listdir(data_path):
    if file.endswith(".csv"):
        df=pd.read_csv(
            os.path.join(data_path, file)
        )

        print("\nfile:",file)
        print("rows:",len(df))
        print("columns:",df.columns.tolist())
        print(df.head())
