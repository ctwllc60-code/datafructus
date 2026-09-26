"""
Datafructus algorithmica - Test 13 (Real-Time Performance)
Tests how fast the species processes a live data stream.
"""

import os
import time
import numpy as np

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

np.random.seed(13)

# Simulate a live stream: 500 data points arriving one at a time
STREAM_LENGTH = 500
WINDOW = 25

# Generate the ground-truth pattern for scoring
x = np.linspace(0, 4 * np.pi, STREAM_LENGTH)
true_pattern = np.sin(x) + 0.5 * np.sin(2.3 * x)
noise = np.random.normal(0, 0.8, STREAM_LENGTH)
stream = true_pattern + noise

# Rolling buffer for real-time processing
buffer = []
processed = []
latencies = []

print("=== DATAFRUCTUS - TEST 13 (REAL-TIME PERFORMANCE) ===")
print()
print(f"Stream length:        {STREAM_LENGTH} points")
print(f"Window size:          {WINDOW}")
print()

# Process one point at a time
for i in range(STREAM_LENGTH):
    t_start = time.perf_counter()

    buffer.append(stream[i])
    if len(buffer) > WINDOW:
        buffer.pop(0)

    # Real-time smoothed value: average of buffer
    smoothed = sum(buffer) / len(buffer)
    processed.append(smoothed)

    t_end = time.perf_counter()
    latencies.append((t_end - t_start) * 1000)  # ms

latencies = np.array(latencies)
processed = np.array(processed)

# Score the streamed output vs ground truth (skip the initial buffer fill)
valid = processed[WINDOW:]
truth = true_pattern[WINDOW:]
corr = np.corrcoef(valid, truth)[0, 1]

# Latency statistics
avg_latency = latencies.mean()
max_latency = latencies.max()
min_latency = latencies.min()
p95_latency = np.percentile(latencies, 95)

# Throughput: points per second
total_time = latencies.sum() / 1000
throughput = STREAM_LENGTH / total_time if total_time > 0 else 0

print("--- LATENCY ---")
print(f"Average:              {avg_latency*1000:.2f} microseconds")
print(f"Minimum:              {min_latency*1000:.2f} microseconds")
print(f"Maximum:              {max_latency*1000:.2f} microseconds")
print(f"95th percentile:      {p95_latency*1000:.2f} microseconds")
print()
print("--- THROUGHPUT ---")
print(f"Points per second:    {throughput:,.0f}")
print()
print("--- ACCURACY ---")
print(f"Stream recovery:      {corr:.4f}")
print()

# Real-world verdict
if avg_latency < 1.0:
    verdict = "REAL-TIME READY"
elif avg_latency < 10.0:
    verdict = "NEAR REAL-TIME"
else:
    verdict = "TOO SLOW"

print(f"Verdict: {verdict}")

with open(os.path.join(RESULTS_DIR, "test_13_realtime.txt"), "w") as f:
    f.write("Datafructus Test 13 - Real-Time Performance\n\n")
    f.write(f"Stream length: {STREAM_LENGTH}\n")
    f.write(f"Avg latency: {avg_latency*1000:.2f} us\n")
    f.write(f"Max latency: {max_latency*1000:.2f} us\n")
    f.write(f"Throughput: {throughput:,.0f} points/sec\n")
    f.write(f"Recovery correlation: {corr:.4f}\n")
    f.write(f"Verdict: {verdict}\n")
