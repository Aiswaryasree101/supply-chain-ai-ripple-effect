from utils.data_generator import generate_nodes, generate_edges, generate_demand
from env.simulator import SupplyChainSimulator

nodes = generate_nodes()
edges = generate_edges()
demand = generate_demand()

sim = SupplyChainSimulator(nodes, edges, demand)

for day in range(5):
    sim.step()
    print(f"Day {day+1}")
    print(nodes)
    print("Cost:", sim.total_cost)
    print("Unmet demand:", sim.total_unmet_demand)
    print("-" * 40)

