import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from utils.data_generator import generate_nodes, generate_edges, generate_demand
from env.simulator import SupplyChainSimulator



EPISODES = 10
DAYS = 30

def run_baseline_episode():
    nodes = generate_nodes()
    edges = generate_edges()
    demand = generate_demand()

    sim = SupplyChainSimulator(nodes, edges, demand)

    total_cost = 0
    total_unmet = 0

    for day in range(DAYS):
        if day == 5:
            sim.inject_disruption("Supplier_India", factor=0.3, duration=5)

        sim.custom_source = "Supplier_India"
        sim.custom_shipment_qty = 200

        sim.step()

    return sim.total_cost, sim.total_unmet_demand


baseline_results = []

for ep in range(EPISODES):
    cost, unmet = run_baseline_episode()
    baseline_results.append((cost, unmet))
    print(f"Baseline Episode {ep+1}: Cost={cost}, Unmet={unmet}")

print("Baseline average:")
print("Cost:", sum(r[0] for r in baseline_results)/EPISODES)
print("Unmet:", sum(r[1] for r in baseline_results)/EPISODES)

with open("evaluation/baseline_results.csv", "w") as f:
    for c, u in baseline_results:
        f.write(f"{c},{u}\n")
