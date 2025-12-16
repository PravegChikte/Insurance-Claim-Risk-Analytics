import pandas as pd
import sqlite3
import numpy as np

# Load processed data
df = pd.read_csv("../data/processed/feature_engineered_claims.csv")

# -----------------------------
# ADD fraud_probability HERE
# -----------------------------
if "fraud_probability" not in df.columns:
    df["fraud_probability"] = df["fraud_flag"].apply(
        lambda x: np.random.uniform(0.6, 0.95) if x == 1 else np.random.uniform(0.05, 0.4)
    )

# Connect to SQLite DB
conn = sqlite3.connect("../insurance.db")

# Replace table
df.to_sql(
    name="claims",
    con=conn,
    if_exists="replace",
    index=False
)

conn.close()

print("✅ Database rebuilt with fraud_probability column")
