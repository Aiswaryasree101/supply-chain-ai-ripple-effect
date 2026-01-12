import matplotlib.pyplot as plt

baseline_cost = []
baseline_unmet = []
ai_cost = []
ai_unmet = []

with open("evaluation/baseline_results.csv") as f:
    for line in f:
        c,u = line.strip().split(",")
        baseline_cost.append(float(c))
        baseline_unmet.append(float(u))

with open("evaluation/ai_results.csv") as f:
    for line in f:
        c,u = line.strip().split(",")
        ai_cost.append(float(c))
        ai_unmet.append(float(u))

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
plt.plot(baseline_unmet, label="Baseline")
plt.plot(ai_unmet, label="AI")
plt.title("Unmet Demand")
plt.legend()

plt.subplot(1,2,2)
plt.plot(baseline_cost, label="Baseline")
plt.plot(ai_cost, label="AI")
plt.title("Cost")
plt.legend()

plt.tight_layout()
plt.show()
