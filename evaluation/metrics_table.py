import pandas as pd
from metrics import compute_metrics

# Load CSVs
baseline_df = pd.read_csv("evaluation/baseline_results.csv")
ai_df = pd.read_csv("evaluation/ai_results.csv")

# Extract values from column names
baseline_costs = [float(baseline_df.columns[0])]
baseline_unmet = [float(baseline_df.columns[1])]

ai_costs = [float(ai_df.columns[0])]
ai_unmet = [float(ai_df.columns[1])]

baseline_metrics = compute_metrics(baseline_costs, baseline_unmet)
ai_metrics = compute_metrics(ai_costs, ai_unmet)

table = pd.DataFrame({
    "Metric": baseline_metrics.keys(),
    "Baseline": baseline_metrics.values(),
    "AI": ai_metrics.values()
})

table.to_csv("evaluation/metrics_comparison.csv", index=False)

print("\nCombined Metrics Table:\n")
print(table)
print("\nSaved to evaluation/metrics_comparison.csv")
