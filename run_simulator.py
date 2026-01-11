from utils.data_generator import generate_nodes, generate_edges, generate_demand
from env.simulator import SupplyChainSimulator

nodes = generate_nodes()
edges = generate_edges()
demand = generate_demand()

sim = SupplyChainSimulator(nodes, edges, demand)

for day in range(15):

    # Inject disruption on day 5
    if day == 5:
        sim.inject_disruption("Port_JebelAli", duration=5)
        print("DISRUPTION: Port_JebelAli shut down for 5 days")

    sim.step()

    print(f"Day {day+1}")
    print("Inventories:", nodes)
    print("In transit:", len(sim.in_transit))
    print("Cost:", sim.total_cost)
    print("Unmet demand:", sim.total_unmet_demand)
    print("-" * 50)
