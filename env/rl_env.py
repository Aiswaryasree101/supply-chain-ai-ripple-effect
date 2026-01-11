import numpy as np
import random
from .simulator import SupplyChainSimulator

class SupplyChainEnv:
    def __init__(self, nodes, edges, demand):
        self.sim = SupplyChainSimulator(nodes, edges, demand)

        # Action space: shipment size multiplier
        self.actions = [
            ("Supplier_India", 100),
            ("Supplier_India", 300),
            ("Supplier_Vietnam", 100),
            ("Supplier_Vietnam", 300),
            ("Supplier_UAE", 100),
            ("Supplier_UAE", 300),
        ]


    def reset(self):
        self.sim.day = 0
        self.sim.total_cost = 0
        self.sim.total_unmet_demand = 0
        self.sim.in_transit = []
        self.sim.disruptions = {}
        return self.get_state()

    def get_state(self):
        # State vector: inventories + pipeline size + unmet demand
        state = []

        for node in self.sim.nodes.values():
            state.append(node["inventory"])

        state.append(len(self.sim.in_transit))
        state.append(self.sim.total_unmet_demand)

        return np.array(state, dtype=np.float32)

    def step(self, action_index):
        supplier, qty = self.actions[action_index]
        self.sim.custom_source = supplier
        self.sim.custom_shipment_qty = qty

        for k in self.sim.demand:
            self.sim.demand[k] = max(10, self.sim.demand[k] + random.randint(-20, 20))

        self.sim.step()

        next_state = self.get_state()

        reward = - (self.sim.total_unmet_demand + 0.001 * self.sim.total_cost)

        done = self.sim.day >= 30

        return next_state, reward, done
