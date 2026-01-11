class SupplyChainSimulator:
    def __init__(self, nodes, edges, demand):
        self.nodes = nodes
        self.edges = edges
        self.demand = demand

        self.day = 0
        self.total_cost = 0
        self.total_unmet_demand = 0

        # shipment pipeline: list of (arrival_day, src, dst, qty)
        self.in_transit = []

        # disruptions: node -> remaining days
        self.disruptions = {}

    def ship_goods(self):
        for edge in self.edges:
            src = edge["from"]
            dst = edge["to"]

            if src in self.disruptions:
                continue  # disrupted node cannot ship

            available = self.nodes[src]["inventory"]
            ship_qty = min(available, getattr(self, "custom_shipment_qty", 200))

            if ship_qty > 0:
                self.nodes[src]["inventory"] -= ship_qty

                arrival_day = self.day + edge["lead_time"]
                self.in_transit.append((arrival_day, dst, ship_qty))

                self.total_cost += edge["cost"]

    def process_arrivals(self):
        arrived = []

        for shipment in self.in_transit:
            arrival_day, dst, qty = shipment

            if arrival_day <= self.day:
                self.nodes[dst]["inventory"] += qty
                arrived.append(shipment)

        for s in arrived:
            self.in_transit.remove(s)

    def satisfy_demand(self):
        for retailer, qty in self.demand.items():
            available = self.nodes[retailer]["inventory"]

            if available >= qty:
                self.nodes[retailer]["inventory"] -= qty
            else:
                unmet = qty - available
                self.total_unmet_demand += unmet
                self.nodes[retailer]["inventory"] = 0

    def inject_disruption(self, node, duration):
        self.disruptions[node] = duration

    def update_disruptions(self):
        to_remove = []
        for node in self.disruptions:
            self.disruptions[node] -= 1
            if self.disruptions[node] <= 0:
                to_remove.append(node)

        for node in to_remove:
            del self.disruptions[node]

    def step(self):
        self.day += 1

        self.update_disruptions()
        self.process_arrivals()
        self.ship_goods()
        self.satisfy_demand()
