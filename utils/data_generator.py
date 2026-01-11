import random

TRANSPORT_COST_RANGE = (50, 5000)
LEAD_TIME_RANGE = (2, 30)
INVENTORY_RANGE = (500, 5000)
DAILY_DEMAND_RANGE = (20, 300)

def generate_nodes():
    return {
        "Supplier_India": {"inventory": random.randint(3000, 8000), "capacity": 15000},
        "Supplier_Vietnam": {"inventory": random.randint(2000, 6000), "capacity": 12000},
        "Supplier_UAE": {"inventory": random.randint(1000, 4000), "capacity": 8000},

        "Port_JebelAli": {"inventory": 0, "capacity": 12000},
        "DC_UAE": {"inventory": random.randint(2000, 6000), "capacity": 10000},
        "Warehouse_Dubai": {"inventory": random.randint(1500, 4000), "capacity": 8000},

        "Retailer_1": {"inventory": random.randint(400, 1200), "capacity": 2000},
        "Retailer_2": {"inventory": random.randint(400, 1200), "capacity": 2000},
    }


def generate_edges():
    edges = []

    suppliers = ["Supplier_India", "Supplier_Vietnam", "Supplier_UAE"]

    for s in suppliers:
        edges.append({
            "from": s,
            "to": "Port_JebelAli",
            "lead_time": random.randint(3, 25),
            "cost": random.randint(500, 6000)
        })

    edges.extend([
        {"from": "Port_JebelAli", "to": "DC_UAE", "lead_time": random.randint(2, 7), "cost": random.randint(300, 1500)},
        {"from": "DC_UAE", "to": "Warehouse_Dubai", "lead_time": random.randint(1, 4), "cost": random.randint(200, 800)},
        {"from": "Warehouse_Dubai", "to": "Retailer_1", "lead_time": 1, "cost": 150},
        {"from": "Warehouse_Dubai", "to": "Retailer_2", "lead_time": 1, "cost": 150},
    ])

    return edges


def generate_demand():
    return {
        "Retailer_1": random.randint(*DAILY_DEMAND_RANGE),
        "Retailer_2": random.randint(*DAILY_DEMAND_RANGE),
    }
