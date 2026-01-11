from utils.data_generator import generate_nodes, generate_edges, generate_demand
from env.rl_env import SupplyChainEnv

nodes = generate_nodes()
edges = generate_edges()
demand = generate_demand()

env = SupplyChainEnv(nodes, edges, demand)

state = env.reset()
print("Initial state:", state)

for _ in range(5):
    action = 2  # fixed action
    next_state, reward, done = env.step(action)
    print("Next state:", next_state)
    print("Reward:", reward)
