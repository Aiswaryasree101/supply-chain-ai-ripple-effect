from utils.data_generator import generate_nodes, generate_edges, generate_demand
from env.rl_env import SupplyChainEnv
from rl.dqn_agent import DQNAgent
import numpy as np

EPISODES = 30

nodes = generate_nodes()
edges = generate_edges()
demand = generate_demand()

env = SupplyChainEnv(nodes, edges, demand)

state_size = len(env.reset())
action_size = len(env.actions)

agent = DQNAgent(state_size, action_size)

for ep in range(EPISODES):
    state = env.reset()
    total_reward = 0

    for step in range(30):
        action = agent.act(state)
        next_state, reward, done = env.step(action)

        agent.remember(state, action, reward, next_state, done)
        agent.replay()

        state = next_state
        total_reward += reward

        if done:
            break

    print(f"Episode {ep+1}/{EPISODES} | Reward: {int(total_reward)} | Epsilon: {agent.epsilon:.2f}")

print("Training complete.")
