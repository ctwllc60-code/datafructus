"""
Datafructus algorithmica - Test 09 (Reproducibility Audit)
Proves: the species produces identical results on identical inputs.
"""

import os
import numpy as np

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

RUNS = 10

def run_once(seed):
    np.random.seed(seed)
    n = 1000
    x = np.linspace(0, 4 * np.pi, n)
    true_pattern = np.sin(x) + 0.5 * np.sin(2.3 * x)
    noise = np.random.normal(0, 1.0, n)
    raw = true_pattern + noise

    window = 25
    kernel = np.ones(window) / window
    recovered = np.convolve(raw, kernel, mode="same")

    corr = np.corrcoef(recovered, true_pattern)[0, 1]
    return round(corr, 6)

print("=== DATAFRUCTUS - TEST 09 (REPRODUCIBILITY AUDIT) ===")
print(f"Running {RUNS} identical trials...\n")

results = []
for i in range(RUNS):
    score = run_once(seed=42)
    results.append(score)
    print(f"Run {i+1:2d}: recovery correlation = {score:.6f}")

unique = set(results)
print()
print(f"Unique results across {RUNS} runs: {len(unique)}")
print(f"Expected: 1 (perfectly reproducible)")

if len(unique) == 1:
    print("\nResult: PASS - perfectly reproducible")
    result = "PASS"
else:
    print(f"\nResult: FAIL - {len(unique)} different results")
    result = "FAIL"

with open(os.path.join(RESULTS_DIR, "test_09_reproducibility.txt"), "w") as f:
    f.write("Datafructus Test 09 - Reproducibility Audit\n\n")
    for i, r in enumerate(results):
        f.write(f"Run {i+1}: {r}\n")
    f.write(f"\nUnique results: {len(unique)}\n")
    f.write(f"Result: {result}\n")
