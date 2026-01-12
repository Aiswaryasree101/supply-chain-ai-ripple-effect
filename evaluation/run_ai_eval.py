import sys
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from utils.data_generator import generate_nodes, generate_edges, generate_demand
from env.rl_env import SupplyChainEnv
from rl.dqn_agent import DQNAgent


EPISODES = 10
DAYS = 30

def run_ai_episode(agent):
    nodes = generate_nodes()
    edges = generate_edges()
    demand = generate_demand()

    env = SupplyChainEnv(nodes, edges, demand)
    state = env.reset()

    for day in range(DAYS):
        if day == 5:
            env.sim.inject_disruption("Supplier_India", factor=0.3, duration=5)

        action = agent.act(state)
        state, reward, done = env.step(action)

    return env.sim.total_cost, env.sim.total_unmet_demand


nodes = generate_nodes()
edges = generate_edges()
demand = generate_demand()
env = SupplyChainEnv(nodes, edges, demand)

state_size = len(env.reset())
action_size = len(env.actions)
agent = DQNAgent(state_size, action_size)

print("Training agent quickly...")
for _ in range(20):
    s = env.reset()
    for _ in range(30):
        a = agent.act(s)
        s2, r, d = env.step(a)
        agent.remember(s, a, r, s2, d)
        agent.replay()
        s = s2

ai_results = []

for ep in range(EPISODES):
    cost, unmet = run_ai_episode(agent)
    ai_results.append((cost, unmet))
    print(f"AI Episode {ep+1}: Cost={cost}, Unmet={unmet}")

print("AI average:")
print("Cost:", sum(r[0] for r in ai_results)/EPISODES)
print("Unmet:", sum(r[1] for r in ai_results)/EPISODES)
