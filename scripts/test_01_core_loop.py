"""
Datafructus algorithmica - Core Loop Test v0.1
Tests: Absorption, Pattern Recognition, Compression, Emission, Reconstruction
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

np.random.seed(42)

# --- 1. ABSORPTION: a noisy signal with a hidden pattern underneath ---
n = 1000
x = np.linspace(0, 4 * np.pi, n)
true_pattern = np.sin(x) + 0.5 * np.sin(2.3 * x)
noise = np.random.normal(0, 1.0, n)
raw_data = true_pattern + noise

# --- 2. PATTERN RECOGNITION: recover the structure from the noise ---
window = 25
kernel = np.ones(window) / window
recovered = np.convolve(raw_data, kernel, mode="same")

# --- 3. COMPRESSION: reduce to the essential points ---
step = 20
compressed = recovered[::step]
compressed_x = x[::step]

# --- 4. EMISSION: render the result ---
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(x, raw_data, color="lightgray", linewidth=0.7, label="Raw (noise)")
ax.plot(x, recovered, color="blue", linewidth=1.5, label="Recovered (pattern)")
ax.plot(x, true_pattern, color="red", linewidth=1.0, linestyle="--", label="True (hidden)")
ax.plot(compressed_x, compressed, "o", color="green", markersize=3, label="Compressed")
ax.legend()
ax.set_title("Datafructus algorithmica - Signal Recovery Test")
plot_path = os.path.join(RESULTS_DIR, "test_01_signal_recovery.png")
plt.tight_layout()
plt.savefig(plot_path, dpi=120)
plt.close()

# --- 5. RECONSTRUCTION: destroy 30% of the signal, rebuild it ---
masked = recovered.copy()
mask_idx = np.random.choice(n, size=int(n * 0.3), replace=False)
masked[mask_idx] = np.nan
known = ~np.isnan(masked)
reconstructed = np.interp(x, x[known], masked[known])

# --- METRICS ---
corr = np.corrcoef(recovered, true_pattern)[0, 1]
recon_corr = np.corrcoef(reconstructed, recovered)[0, 1]
compression_ratio = n / len(compressed)

print("=== DATAFRUCTUS ALGORITHMICA - CORE LOOP TEST v0.1 ===")
print(f"Input points:            {n}")
print(f"Compressed points:       {len(compressed)}")
print(f"Compression ratio:       {compression_ratio:.1f}:1")
print(f"Signal recovery corr:    {corr:.3f}  (1.0 = perfect)")
print(f"Reconstruction corr:     {recon_corr:.3f}  (1.0 = perfect)")
print(f"Plot saved to:           {plot_path}")
