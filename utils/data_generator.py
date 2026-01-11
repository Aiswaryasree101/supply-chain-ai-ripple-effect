import random

TRANSPORT_COST_RANGE = (50, 5000)
LEAD_TIME_RANGE = (2, 30)
INVENTORY_RANGE = (500, 5000)
DAILY_DEMAND_RANGE = (20, 300)

def generate_nodes():
    return {
        "Supplier_India": {"inventory": random.randint(*INVENTORY_RANGE), "capacity": 10000},
        "Port_JebelAli": {"inventory": 0, "capacity": 8000},
        "DC_UAE": {"inventory": random.randint(*INVENTORY_RANGE), "capacity": 6000},
        "Warehouse_Dubai": {"inventory": random.randint(*INVENTORY_RANGE), "capacity": 5000},
        "Retailer_1": {"inventory": random.randint(200, 800), "capacity": 1500},
        "Retailer_2": {"inventory": random.randint(200, 800), "capacity": 1500},
    }

def generate_edges():
    return [
        {"from": "Supplier_India", "to": "Port_JebelAli",
         "lead_time": random.randint(*LEAD_TIME_RANGE),
         "cost": random.randint(*TRANSPORT_COST_RANGE)},

        {"from": "Port_JebelAli", "to": "DC_UAE",
         "lead_time": random.randint(*LEAD_TIME_RANGE),
         "cost": random.randint(*TRANSPORT_COST_RANGE)},

        {"from": "DC_UAE", "to": "Warehouse_Dubai",
         "lead_time": random.randint(*LEAD_TIME_RANGE),
         "cost": random.randint(*TRANSPORT_COST_RANGE)},

        {"from": "Warehouse_Dubai", "to": "Retailer_1",
         "lead_time": random.randint(1, 3),
         "cost": random.randint(100, 500)},

        {"from": "Warehouse_Dubai", "to": "Retailer_2",
         "lead_time": random.randint(1, 3),
         "cost": random.randint(100, 500)},
    ]

def generate_demand():
    return {
        "Retailer_1": random.randint(*DAILY_DEMAND_RANGE),
        "Retailer_2": random.randint(*DAILY_DEMAND_RANGE),
    }
