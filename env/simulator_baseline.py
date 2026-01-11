class SupplyChainSimulator:
    def __init__(self, nodes, edges, demand):
        self.nodes = nodes
        self.edges = edges
        self.demand = demand
        self.day = 0
        self.total_cost = 0
        self.total_unmet_demand = 0

    def ship_goods(self):
        for edge in self.edges:
            src = edge["from"]
            dst = edge["to"]

            available = self.nodes[src]["inventory"]
            ship_qty = min(available, 200)

            if ship_qty > 0:
                self.nodes[src]["inventory"] -= ship_qty
                self.nodes[dst]["inventory"] += ship_qty
                self.total_cost += edge["cost"]

    def satisfy_demand(self):
        for retailer, qty in self.demand.items():
            available = self.nodes[retailer]["inventory"]

            if available >= qty:
                self.nodes[retailer]["inventory"] -= qty
            else:
                unmet = qty - available
                self.total_unmet_demand += unmet
                self.nodes[retailer]["inventory"] = 0

    def step(self):
        self.day += 1
        self.ship_goods()
        self.satisfy_demand()
