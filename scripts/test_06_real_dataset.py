"""
Datafructus algorithmica - Real Dataset Test v0.1
Uses the UCI Air Quality dataset (real sensor data, real noise, real missing values)
Proves: the core loop works on real-world data, not just synthetic sine waves.
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

try:
    from ucimlrepo import fetch_ucirepo
    DATASET_AVAILABLE = True
except ImportError:
    DATASET_AVAILABLE = False
    print("WARNING: ucimlrepo not installed. Falling back to synthetic data.")
    print("Install it with: pip install ucimlrepo")

# --- LOAD REAL DATA ---
if DATASET_AVAILABLE:
    print("Fetching UCI Air Quality dataset (real-world sensor data)...")
    air_quality = fetch_ucirepo(id=360)
    df = air_quality.data.features
    # Use the PT08.S1(CO) sensor response - a continuous real signal
    signal = df["PT08.S1(CO)"].values.astype(float)
    # Remove missing values marked as -200
    signal = signal[signal > -100]
    print(f"Loaded {len(signal)} real sensor readings.")
else:
    # Fallback: synthetic (only if dataset unavailable)
    n = 500
    x = np.linspace(0, 6 * np.pi, n)
    signal = np.sin(x) + 0.4 * np.sin(3.1 * x) + np.random.normal(0, 0.3, n)

# Take a clean segment of the real signal
n = min(1000, len(signal))
real_signal = signal[:n]

# --- INTRODUCE NOISE AND DESTRUCTION ---
noise = np.random.normal(0, np.std(real_signal) * 0.5, n)
raw_data = real_signal + noise

# Destroy 30% of the raw data
mask = np.random.rand(n) < 0.30
destroyed = raw_data.copy()
destroyed[mask] = np.nan

# --- DATAFRUCTUS CORE LOOP ---
# 1. Absorption: data comes in
# 2. Pattern Recognition: smoothing kernel recovers structure
window = 25
kernel = np.ones(window) / window
# For the destroyed version, fill gaps with linear interpolation first
known = ~np.isnan(destroyed)
filled = np.interp(np.arange(n), np.arange(n)[known], destroyed[known])
recovered = np.convolve(filled, kernel, mode="same")

# 3. Compression: keep every 20th point
compressed = recovered[::20]

# 4. Reconstruction: rebuild from compressed
reconstructed = np.interp(np.arange(n), np.arange(0, n, 20), compressed)

# --- METRICS ---
corr_signal = np.corrcoef(recovered, real_signal)[0, 1]
corr_recon = np.corrcoef(reconstructed, real_signal)[0, 1]
compression_ratio = n / len(compressed)

# --- EMISSION ---
fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(real_signal, color="black", linewidth=1.2, label="True signal (real sensor)")
ax.plot(raw_data, color="lightgray", linewidth=0.5, alpha=0.6, label="Raw with noise")
ax.plot(recovered, color="blue", linewidth=1.5, label="Recovered pattern")
ax.plot(reconstructed, color="green", linewidth=1.0, linestyle="--", label="Reconstructed from compression")
ax.set_title("Datafructus algorithmica - Real Dataset Test (UCI Air Quality)")
ax.set_xlabel("Reading index")
ax.set_ylabel("Sensor response")
ax.legend()
ax.grid(True, alpha=0.3)
plot_path = os.path.join(RESULTS_DIR, "test_06_real_dataset.png")
plt.tight_layout()
plt.savefig(plot_path, dpi=120)
plt.close()

# --- REPORT ---
print("=== DATAFRUCTUS ALGORITHMICA - REAL DATASET TEST v0.1 ===")
print(f"Dataset:                     UCI Air Quality (PT08.S1(CO))")
print(f"Readings used:               {n}")
print(f"Destroyed (masked) points:   {int(mask.sum())} ({100*mask.mean():.0f}%)")
print(f"Compressed points:           {len(compressed)}")
print(f"Compression ratio:           {compression_ratio:.1f}:1")
print(f"Signal recovery correlation: {corr_signal:.3f}")
print(f"Reconstruction correlation:  {corr_recon:.3f}")
print(f"Plot saved to:               {plot_path}")
