"""
Datafructus algorithmica - Test 11 (Resource Efficiency)
Measures CPU time, memory usage, and wall time during a core loop run.
"""

import os
import time
import tracemalloc
import resource
import numpy as np

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

np.random.seed(11)

# --- SETUP (before measurement) ---
n = 1000
x = np.linspace(0, 4 * np.pi, n)
true_pattern = np.sin(x) + 0.5 * np.sin(2.3 * x)
noise = np.random.normal(0, 1.0, n)
raw = true_pattern + noise

# --- START MEASUREMENT ---
tracemalloc.start()
cpu_start = time.process_time()
wall_start = time.perf_counter()

window = 25
kernel = np.ones(window) / window
recovered = np.convolve(raw, kernel, mode="same")
corr = np.corrcoef(recovered, true_pattern)[0, 1]

compressed = recovered[::20]

mask = np.random.rand(n) < 0.3
destroyed = recovered.copy()
destroyed[mask] = np.nan
known = ~np.isnan(destroyed)
reconstructed = np.interp(np.arange(n), np.arange(n)[known], destroyed[known])

wall_end = time.perf_counter()
cpu_end = time.process_time()
current_mem, peak_mem = tracemalloc.get_traced_memory()
tracemalloc.stop()
# --- END MEASUREMENT ---

wall_time = wall_end - wall_start
cpu_time = cpu_end - cpu_start
peak_mb = peak_mem / (1024 * 1024)
cpu_percent = (cpu_time / wall_time) * 100 if wall_time > 0 else 0

# System-level peak memory (RSS)
rss_kb = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

print("=== DATAFRUCTUS - TEST 11 (RESOURCE EFFICIENCY) ===")
print()
print(f"Input size:               {n} data points")
print(f"Recovery correlation:     {corr:.6f}")
print()
print("--- CPU ---")
print(f"Wall time:                {wall_time*1000:.2f} ms")
print(f"CPU time:                 {cpu_time*1000:.2f} ms")
print(f"CPU utilization:          {cpu_percent:.1f}%")
print()
print("--- MEMORY ---")
print(f"Python peak memory:       {peak_mb:.3f} MB")
print(f"System peak RSS:          {rss_kb/1024:.2f} MB")
print()
print("--- VERDICT ---")
if peak_mb < 50 and wall_time < 1.0:
    verdict = "EFFICIENT"
elif peak_mb < 200 and wall_time < 5.0:
    verdict = "ACCEPTABLE"
else:
    verdict = "HEAVY"
print(f"Result: {verdict}")
print()
print("Ready to run on any device with Python + NumPy.")

with open(os.path.join(RESULTS_DIR, "test_11_resource_efficiency.txt"), "w") as f:
    f.write("Datafructus Test 11 - Resource Efficiency\n\n")
    f.write(f"Input size: {n} data points\n")
    f.write(f"Recovery correlation: {corr:.6f}\n")
    f.write(f"Wall time: {wall_time*1000:.2f} ms\n")
    f.write(f"CPU time: {cpu_time*1000:.2f} ms\n")
    f.write(f"CPU utilization: {cpu_percent:.1f}%\n")
    f.write(f"Python peak memory: {peak_mb:.3f} MB\n")
    f.write(f"System peak RSS: {rss_kb/1024:.2f} MB\n")
    f.write(f"Result: {verdict}\n")
