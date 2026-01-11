import pandas as pd
file_path = "data/real/delivery_history.csv"
df = pd.read_csv(file_path)

print("========== COLUMNS ==========")
print(df.columns.tolist())

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

