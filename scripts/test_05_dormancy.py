"""
Datafructus algorithmica - Dormancy State Test v0.1
Proves: the species conserves resources when data is quiet,
and reactivates when data returns.
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

np.random.seed(23)

n = 500
x = np.linspace(0, 6 * np.pi, n)
true_pattern = np.sin(x) + 0.4 * np.sin(3.1 * x)

learned_kernel = np.ones(5) / 5

# Simulate a data stream: intensity varies over 200 cycles
# Active period: high data volume. Quiet period: near-zero data.
def data_intensity(cycle):
    if cycle < 40:
        return 1.0            # active
    elif cycle < 100:
        return 0.02           # quiet - dormancy should trigger
    elif cycle < 140:
        return 1.0            # active again
    else:
        return 0.02           # quiet again

DORMANCY_THRESHOLD = 0.10
scores = []
intensities = []
states = []  # "ACTIVE" or "DORMANT"
activations = 0
dormant_cycles = 0
active_cycles = 0

for cycle in range(200):
    intensity = data_intensity(cycle)
    intensities.append(intensity)

    # Decide state based on data intensity
    if intensity < DORMANCY_THRESHOLD:
        state = "DORMANT"
        dormant_cycles += 1
        # Dormant: no processing, no learning. Just log a flat score.
        scores.append(scores[-1] if scores else 0.0)
    else:
        if (len(states) > 0 and states[-1] == "DORMANT"):
            activations += 1  # woke up from dormancy
        state = "ACTIVE"
        active_cycles += 1

        # Active: process data, learn
        noise = np.random.normal(0, 1.2, n)
        raw = true_pattern + noise
        recovered = np.convolve(raw, learned_kernel, mode="same")
        score = np.corrcoef(recovered, true_pattern)[0, 1]
        scores.append(score)

        error = true_pattern - recovered
        target = learned_kernel + 0.15 * np.convolve(error, raw, mode="same")[:len(learned_kernel)] * 0.001
        learned_kernel = 0.9 * learned_kernel + 0.1 * target
        learned_kernel = np.abs(learned_kernel)
        learned_kernel = learned_kernel / learned_kernel.sum()

    states.append(state)

scores = np.array(scores)
intensities = np.array(intensities)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 7), sharex=True)

ax1.plot(range(200), intensities, color="blue", linewidth=1.2)
ax1.axhline(DORMANCY_THRESHOLD, color="red", linestyle="--", label=f"Dormancy threshold ({DORMANCY_THRESHOLD})")
ax1.set_ylabel("Data intensity")
ax1.set_title("Datafructus algorithmica - Dormancy State Test")
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.plot(range(200), scores, color="purple", linewidth=1.5)
ax2.set_xlabel("Cycle number")
ax2.set_ylabel("Recovery correlation")
ax2.grid(True, alpha=0.3)

plot_path = os.path.join(RESULTS_DIR, "test_05_dormancy.png")
plt.tight_layout()
plt.savefig(plot_path, dpi=120)
plt.close()

print("=== DATAFRUCTUS ALGORITHMICA - DORMANCY STATE TEST v0.1 ===")
print(f"Total cycles:               200")
print(f"Active cycles:              {active_cycles}")
print(f"Dormant cycles:             {dormant_cycles}")
print(f"Dormancy activations:       {activations} (wake events)")
print(f"Final recovery score:       {scores[-1]:.3f}")
print(f"Peak recovery score:        {scores.max():.3f}")
print(f"Plot saved to:              {plot_path}")
