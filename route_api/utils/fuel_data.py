import pandas as pd
import os

# Go up 3 levels to reach project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

file_path = os.path.join(BASE_DIR, "fuel_data.csv")

df = pd.read_csv(file_path)

df.columns = df.columns.str.strip()

df["full_address"] = df["Address"] + ", " + df["City"] + ", " + df["State"]

df = df.sort_values("Retail Price").drop_duplicates(
    subset=["Address", "City", "State"],
    keep="first"
)

df = df[["Truckstop Name", "City", "State", "Retail Price"]]