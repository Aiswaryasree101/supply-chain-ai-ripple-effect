import pandas as pd

file_path = "data/real/delivery_history.csv"

df = pd.read_csv(file_path)

# Clean numeric columns
cost = pd.to_numeric(df["Freight Cost (USD)"], errors="coerce").dropna()
quantity = pd.to_numeric(df["Line Item Quantity"], errors="coerce").dropna()
weight = pd.to_numeric(df["Weight (Kilograms)"], errors="coerce").dropna()

print("=== Transport Cost (USD) ===")
print("Min:", cost.min())
print("Max:", cost.max())

print("\n=== Quantity ===")
print("Min:", quantity.min())
print("Max:", quantity.max())

print("\n=== Weight (kg) ===")
print("Min:", weight.min())
print("Max:", weight.max())

# Lead time calculation
df["PO Date"] = pd.to_datetime(df["PO Sent to Vendor Date"], errors="coerce")
df["Delivered Date"] = pd.to_datetime(df["Delivered to Client Date"], errors="coerce")

lead_time = (df["Delivered Date"] - df["PO Date"]).dt.days

# Keep only realistic lead times
lead_time = lead_time[(lead_time >= 1) & (lead_time <= 120)]

print("\n=== Lead Time (days, filtered) ===")
print("Min:", lead_time.min())
print("Max:", lead_time.max())

