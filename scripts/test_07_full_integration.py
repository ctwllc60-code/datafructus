"""
Datafructus algorithmica - Full Integration Test v1.0
All eight layers operating as one unified species.

Layers exercised:
  1. Absorption            - data enters
  2. Pattern Recognition   - adaptive kernel finds structure
  3. Compression           - keep only what matters
  4. Emission              - produce human-readable output
  5. Learning Memory       - improve with each exposure
  6. Dormancy State        - sleep when data is quiet
  7. Resilience Core       - break through plateaus
  8. Pattern Reconstruction - rebuild destroyed signal

Standalone test. Runs on real-world data. No dependency on prior tests.
"""

import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RESULTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "results")
os.makedirs(RESULTS_DIR, exist_ok=True)

np.random.seed(101)

# ============================================================
# LAYER 1 — ABSORPTION
# ============================================================
def absorb():
    """Take in raw data from a real source."""
    try:
        from ucimlrepo import fetch_ucirepo
        print("[1] ABSORPTION: Fetching UCI Air Quality dataset...")
        data = fetch_ucirepo(id=360)
        df = data.data.features
        signal = df["PT08.S1(CO)"].values.astype(float)
        signal = signal[signal > -100]
        signal = signal[:1000]
        print(f"    Absorbed {len(signal)} real sensor readings.")
        return signal, "UCI Air Quality (real)"
    except Exception as e:
        print(f"[1] ABSORPTION: Real dataset unavailable ({e}). Using synthetic.")
        x = np.linspace(0, 8 * np.pi, 1000)
        signal = np.sin(x) + 0.4 * np.sin(3.1 * x) + 0.2 * np.sin(7.7 * x)
        return signal, "synthetic"


# ============================================================
# LAYER 2 — PATTERN RECOGNITION (adaptive kernel)
# ============================================================
def adaptive_recover(raw):
    """Adaptive smoothing: kernel width responds to local variability."""
    n = len(raw)
    recovered = np.zeros(n)
    base_window = 15
    for i in range(n):
        lo = max(0, i - base_window)
        hi = min(n, i + base_window + 1)
        local = raw[lo:hi]
        local_var = np.var(local)
        global_var = np.var(raw) + 1e-9
        # If local is spiky, use a smaller effective window
        ratio = min(1.0, local_var / global_var)
        w = max(3, int(base_window * (1.0 - 0.6 * ratio)))
        lo2 = max(0, i - w)
        hi2 = min(n, i + w + 1)
        recovered[i] = np.mean(raw[lo2:hi2])
    return recovered


# ============================================================
# LAYER 3 — COMPRESSION
# ============================================================
def compress(signal, step=20):
    """Reduce data volume while preserving structure."""
    compressed = signal[::step]
    return compressed, step


# ============================================================
# LAYER 4 — EMISSION (handled at end via plot)


# ============================================================
# LAYER 5 — LEARNING MEMORY
# ============================================================
def learning_pass(raw, target, iterations=30):
    """Species improves across exposures. Tracks score history."""
    learned_weights = np.ones(9) / 9
    scores = []
    for it in range(iterations):
        recovered = np.convolve(raw, learned_weights, mode="same")
        score = np.corrcoef(recovered, target)[0, 1]
        scores.append(score)
        error = target - recovered
        correction = np.convolve(error, raw, mode="same")[:len(learned_weights)] * 0.0005
        learned_weights = 0.9 * learned_weights + 0.1 * (learned_weights + correction)
        learned_weights = np.abs(learned_weights)
        learned_weights = learned_weights / learned_weights.sum()
    return learned_weights, np.array(scores)


# ============================================================
# LAYER 6 — DORMANCY STATE
# ============================================================
def dormancy_check(local_intensity, threshold=0.15):
    """Return True if species should be dormant."""
    return local_intensity < threshold


# ============================================================
# LAYER 7 — RESILIENCE CORE
# ============================================================
def resilience_perturb(weights, strength=0.05):
    """Perturb weights when plateau detected."""
    perturbed = weights + np.random.normal(0, strength, len(weights))
    perturbed = np.abs(perturbed)
    return perturbed / perturbed.sum()


# ============================================================
# LAYER 8 — PATTERN RECONSTRUCTION
# ============================================================
def reconstruct(signal, mask):
    """Rebuild destroyed points from surviving neighbors."""
    known = ~mask
    n = len(signal)
    filled = np.interp(np.arange(n), np.arange(n)[known], signal[known])
    return filled


# ============================================================
# FULL PIPELINE
# ============================================================
def main():
    print("\n=== DATAFRUCTUS ALGORITHMICA - FULL INTEGRATION TEST v1.0 ===\n")

    # LAYER 1
    true_signal, source = absorb()

    # Introduce noise and destruction
    n = len(true_signal)
    noise = np.random.normal(0, np.std(true_signal) * 0.4, n)
    raw_noisy = true_signal + noise
    mask = np.random.rand(n) < 0.25
    destroyed = raw_noisy.copy()
    destroyed[mask] = np.nan

    # LAYER 8 (early — reconstruct destroyed before recognizing)
    reconstructed = reconstruct(destroyed, mask)
    print(f"[8] RECONSTRUCTION: Rebuilt {int(mask.sum())} destroyed points.")

    # LAYER 2
    recovered = adaptive_recover(reconstructed)
    corr_recover = np.corrcoef(recovered, true_signal)[0, 1]
    print(f"[2] PATTERN RECOGNITION: adaptive kernel -> corr = {corr_recover:.3f}")

    # LAYER 3
    compressed, step = compress(recovered, step=20)
    ratio = n / len(compressed)
    print(f"[3] COMPRESSION: {n} -> {len(compressed)} points ({ratio:.1f}:1)")

    # LAYER 5 — learning with dormancy + resilience
    print(f"[5] LEARNING MEMORY: running 30 exposures...")
    weights = np.ones(9) / 9
    scores = []
    dormant_count = 0
    resilience_activations = 0

    for it in range(30):
        # LAYER 6 — dormancy check (simulate varying intensity)
        intensity = 1.0 if it % 5 != 4 else 0.05
        if dormancy_check(intensity):
            dormant_count += 1
            scores.append(scores[-1] if scores else 0.0)
            continue

        recovered_it = np.convolve(reconstructed, weights, mode="same")
        score = np.corrcoef(recovered_it, true_signal)[0, 1]
        scores.append(score)

        # LAYER 7 — resilience: detect plateau
        if it > 10:
            recent = scores[-8:]
            if max(recent) - min(recent) < 0.003:
                weights = resilience_perturb(weights)
                resilience_activations += 1
                continue

        # Normal learning
        error = true_signal - recovered_it
        correction = np.convolve(error, reconstructed, mode="same")[:len(weights)] * 0.0005
        weights = 0.9 * weights + 0.1 * (weights + correction)
        weights = np.abs(weights)
        weights = weights / weights.sum()

    scores = np.array(scores)
    first_avg = scores[:5].mean()
    last_avg = scores[-5:].mean()
    improvement = last_avg - first_avg

    print(f"    Dormancy cycles:       {dormant_count}")
    print(f"    Resilience activations: {resilience_activations}")
    print(f"    First 5 avg score:     {first_avg:.3f}")
    print(f"    Last 5 avg score:      {last_avg:.3f}")
    print(f"    Total improvement:     +{improvement:.3f}")

    # LAYER 4 — EMISSION
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), sharex=False)

    ax1.plot(true_signal, color="black", linewidth=1.4, label="True signal")
    ax1.plot(raw_noisy, color="lightgray", linewidth=0.6, alpha=0.5, label="Raw (noisy)")
    ax1.plot(recovered, color="blue", linewidth=1.6, label="Recovered (adaptive)")
    ax1.plot(np.arange(0, n, step), compressed, "o", color="green", markersize=3, label="Compressed")
    ax1.set_title(f"Datafructus algorithmica - Full Integration ({source})")
    ax1.set_ylabel("Signal")
    ax1.legend(loc="upper right", fontsize=8)
    ax1.grid(True, alpha=0.3)

    ax2.plot(range(1, len(scores) + 1), scores, color="purple", linewidth=1.5)
    ax2.set_xlabel("Exposure")
    ax2.set_ylabel("Recovery score")
    ax2.set_title("Learning Memory (with dormancy and resilience events)")
    ax2.grid(True, alpha=0.3)

    plot_path = os.path.join(RESULTS_DIR, "test_07_full_integration.png")
    plt.tight_layout()
    plt.savefig(plot_path, dpi=120)
    plt.close()

    print(f"[4] EMISSION: Plot saved to {plot_path}")

    # SUMMARY
    print("\n--- INTEGRATION SUMMARY ---")
    print(f"Source:                  {source}")
    print(f"Recovery correlation:    {corr_recover:.3f}")
    print(f"Compression ratio:       {ratio:.1f}:1")
    print(f"Learning improvement:    +{improvement:.3f}")
    print(f"Dormancy cycles:         {dormant_count}")
    print(f"Resilience activations:  {resilience_activations}")
    print(f"All 8 layers executed.")


if __name__ == "__main__":
    main()
