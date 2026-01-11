import numpy as np
from .simulator import SupplyChainSimulator

class SupplyChainEnv:
    def __init__(self, nodes, edges, demand):
        self.sim = SupplyChainSimulator(nodes, edges, demand)

        # Action space: shipment size multiplier
        self.actions = [50, 100, 200, 300]

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
        shipment_qty = self.actions[action_index]

        # override shipment size
        self.sim.custom_shipment_qty = shipment_qty

        self.sim.step()

        next_state = self.get_state()

        reward = - (self.sim.total_unmet_demand + 0.001 * self.sim.total_cost)

        done = self.sim.day >= 30

        return next_state, reward, done
