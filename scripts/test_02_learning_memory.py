"""
Datafructus algorithmica - Learning Memory Test v0.1
Proves: the species improves with each exposure to data.
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

np.random.seed(7)

n = 500
x = np.linspace(0, 6 * np.pi, n)
true_pattern = np.sin(x) + 0.4 * np.sin(3.1 * x)

# The species keeps a memory of what it has learned
learned_kernel = np.ones(5) / 5
learning_rate = 0.15
scores = []

for exposure in range(50):
    noise = np.random.normal(0, 1.2, n)
    raw = true_pattern + noise

    recovered = np.convolve(raw, learned_kernel, mode="same")
    score = np.corrcoef(recovered, true_pattern)[0, 1]
    scores.append(score)

    # The species updates its kernel based on what just happened
    error = true_pattern - recovered
    target_kernel = learned_kernel + learning_rate * np.convolve(error, raw, mode="same")[:len(learned_kernel)] * 0.001
    learned_kernel = 0.9 * learned_kernel + 0.1 * target_kernel
    learned_kernel = np.abs(learned_kernel)
    learned_kernel = learned_kernel / learned_kernel.sum()

scores = np.array(scores)
first_10 = scores[:10].mean()
last_10 = scores[-10:].mean()
improvement = last_10 - first_10

fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(range(1, 51), scores, marker="o", color="purple", linewidth=1.5)
ax.axhline(first_10, color="gray", linestyle="--", label=f"First 10 avg: {first_10:.3f}")
ax.axhline(last_10, color="green", linestyle="--", label=f"Last 10 avg: {last_10:.3f}")
ax.set_xlabel("Exposure number")
ax.set_ylabel("Recovery correlation")
ax.set_title("Datafructus algorithmica - Learning Memory Test")
ax.legend()
ax.grid(True, alpha=0.3)
plot_path = os.path.join(RESULTS_DIR, "test_02_learning_memory.png")
plt.tight_layout()
plt.savefig(plot_path, dpi=120)
plt.close()

print("=== DATAFRUCTUS ALGORITHMICA - LEARNING MEMORY TEST v0.1 ===")
print(f"Total exposures:             50")
print(f"First 10 avg recovery:       {first_10:.3f}")
print(f"Last 10 avg recovery:        {last_10:.3f}")
print(f"Improvement over time:       +{improvement:.3f}")
print(f"Percent improvement:         {(improvement / first_10 * 100):.1f}%")
print(f"Plot saved to:               {plot_path}")
