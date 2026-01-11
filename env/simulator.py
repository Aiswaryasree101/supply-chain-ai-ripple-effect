class SupplyChainSimulator:
    def __init__(self, nodes, edges, demand):
        self.nodes = nodes
        self.edges = edges
        self.demand = demand

        self.day = 0
        self.total_cost = 0
        self.total_unmet_demand = 0

        # (arrival_day, destination, quantity)
        self.in_transit = []

        # disruptions: node -> {"factor": float, "days": int}
        self.disruptions = {}

        # RL controls
        self.custom_shipment_qty = 200
        self.custom_source = None

    # -------------------------
    # Shipping logic
    # -------------------------
    def ship_goods(self):
        for edge in self.edges:
            src = edge["from"]
            dst = edge["to"]

            # Agent-selected supplier
            selected_src = self.custom_source if self.custom_source else src
            if src != selected_src:
                continue

            # Disruption capacity factor
            if src in self.disruptions:
                factor = self.disruptions[src]["factor"]
            else:
                factor = 1.0

            available = self.nodes[src]["inventory"]

            max_ship = int(self.custom_shipment_qty * factor)
            ship_qty = min(available, max_ship)

            if ship_qty <= 0:
                continue

            self.nodes[src]["inventory"] -= ship_qty

            arrival_day = self.day + edge["lead_time"]
            self.in_transit.append((arrival_day, dst, ship_qty))

            self.total_cost += edge["cost"]

    # -------------------------
    # Shipment arrivals
    # -------------------------
    def process_arrivals(self):
        arrived = []

        for shipment in self.in_transit:
            arrival_day, dst, qty = shipment
            if arrival_day <= self.day:
                self.nodes[dst]["inventory"] += qty
                arrived.append(shipment)

        for s in arrived:
            self.in_transit.remove(s)

    # -------------------------
    # Demand fulfillment
    # -------------------------
    def satisfy_demand(self):
        for retailer, qty in self.demand.items():
            available = self.nodes[retailer]["inventory"]

            if available >= qty:
                self.nodes[retailer]["inventory"] -= qty
            else:
                unmet = qty - available
                self.total_unmet_demand += unmet
                self.nodes[retailer]["inventory"] = 0

    # -------------------------
    # Disruption handling
    # -------------------------
    def inject_disruption(self, node, factor=0.3, duration=5):
        """
        factor: remaining capacity (0.3 = 30%)
        duration: days
        """
        self.disruptions[node] = {"factor": factor, "days": duration}

    def update_disruptions(self):
        expired = []

        for node in self.disruptions:
            self.disruptions[node]["days"] -= 1
            if self.disruptions[node]["days"] <= 0:
                expired.append(node)

        for node in expired:
            del self.disruptions[node]

    # -------------------------
    # Simulation step
    # -------------------------
    def step(self):
        self.day += 1

        self.update_disruptions()
        self.process_arrivals()
        self.ship_goods()
        self.satisfy_demand()
