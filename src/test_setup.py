import pandas as pd
import numpy as np

print("E-Commerce Data Engineering Pipeline Project")

data={
    "Product":["Mobiles","Headphones","Laptop"],
    "Price":[23000,340000,657888],
    "Quantity":[2,5,8]
}

df=pd.DataFrame(data)
df["Total"]= df["Price"]*df["Quantity"]
print(df)

print('/n Total_sales')
print(df["Total"].sum())