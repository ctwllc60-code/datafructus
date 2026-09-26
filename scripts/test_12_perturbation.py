"""
Datafructus algorithmica - Test 12 (Data Perturbation)
Tests how well the species handles corrupted, incomplete, and noisy input.
"""

import os
import numpy as np

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

np.random.seed(12)

n = 1000
x = np.linspace(0, 4 * np.pi, n)
true_pattern = np.sin(x) + 0.5 * np.sin(2.3 * x)


def recover(signal, window=25):
    kernel = np.ones(window) / window
    return np.convolve(signal, kernel, mode="same")


def score(signal):
    return np.corrcoef(signal, true_pattern)[0, 1]


# --- BASELINE: clean signal + mild noise ---
clean = true_pattern + np.random.normal(0, 0.3, n)
baseline_score = score(recover(clean))

print("=== DATAFRUCTUS - TEST 12 (DATA PERTURBATION) ===")
print()
print(f"Baseline (clean + mild noise):  {baseline_score:.4f}")
print()

# --- PERTURBATION TESTS ---
results = {}

# 1. Heavy noise
heavy = true_pattern + np.random.normal(0, 2.5, n)
results["Heavy noise (std 2.5)"] = score(recover(heavy))

# 2. Missing data (30% gaps)
missing = clean.copy()
mask = np.random.rand(n) < 0.30
missing[mask] = np.nan
known = ~np.isnan(missing)
filled = np.interp(np.arange(n), np.arange(n)[known], missing[known])
results["Missing data (30% gaps)"] = score(recover(filled))

# 3. Extreme outliers (5% of points are garbage)
outlier = clean.copy()
out_idx = np.random.choice(n, size=int(n * 0.05), replace=False)
outlier[out_idx] = np.random.normal(0, 20, len(out_idx))
results["Outliers (5% garbage)"] = score(recover(outlier))

# 4. Stuck sensor (flatline segment)
stuck = clean.copy()
stuck[300:400] = stuck[300]
results["Stuck sensor (100 pts flat)"] = score(recover(stuck))

# 5. Drifting baseline (slow shift added)
drift = clean + np.linspace(0, 3, n)
results["Baseline drift"] = score(recover(drift))

# 6. Full corruption (everything wrong)
corrupt = np.random.normal(0, 1, n)
results["Total corruption"] = score(recover(corrupt))

print("Perturbation                 Recovery Score    Retention vs Baseline")
print("-" * 70)
for name, s in results.items():
    retention = (s / baseline_score) * 100 if baseline_score > 0 else 0
    print(f"{name:<28} {s:>8.4f}          {retention:>6.1f}%")

# --- VERDICT ---
survived = sum(1 for s in results.values() if s > 0.5)
print()
print(f"Tests survived (>0.5 recovery): {survived} of {len(results)}")

if survived >= 5:
    verdict = "ROBUST"
elif survived >= 3:
    verdict = "RESILIENT"
else:
    verdict = "FRAGILE"

print(f"Verdict: {verdict}")

with open(os.path.join(RESULTS_DIR, "test_12_perturbation.txt"), "w") as f:
    f.write("Datafructus Test 12 - Data Perturbation\n\n")
    f.write(f"Baseline: {baseline_score:.4f}\n\n")
    for name, s in results.items():
        f.write(f"{name}: {s:.4f}\n")
    f.write(f"\nVerdict: {verdict}\n")
