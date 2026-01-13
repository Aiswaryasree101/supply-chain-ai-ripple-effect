import numpy as np

def compute_metrics(costs, unmet):
    costs = np.array(costs)
    unmet = np.array(unmet)

    metrics = {
        "avg_cost": float(np.mean(costs)),
        "avg_unmet": float(np.mean(unmet)),
        "var_unmet": float(np.var(unmet)),
        "max_unmet": float(np.max(unmet)),
        "min_unmet": float(np.min(unmet)),
        "avg_reward": float(np.mean(-0.1 * costs - 5 * unmet))
    }
    return metrics
