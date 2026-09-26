"""
Datafructus algorithmica - Test 10 (Cross-Platform Validation)
Proves: the species produces identical results on any device.
Pure Python. No dependencies. Runs anywhere.
"""

import hashlib
import platform
import sys

def lcg(seed, count):
    """Simple deterministic pseudo-random generator. No libraries needed."""
    a, c, m = 1103515245, 12345, 2**31
    state = seed
    out = []
    for _ in range(count):
        state = (a * state + c) % m
        out.append((state / m) * 2 - 1)  # -1 to 1
    return out

def sine_wave(freq, count):
    """Pure-Python sine approximation using Taylor series."""
    import math
    out = []
    for i in range(count):
        x = freq * i
        out.append(math.sin(x))
    return out

def moving_average(signal, window):
    out = []
    half = window // 2
    for i in range(len(signal)):
        lo = max(0, i - half)
        hi = min(len(signal), i + half + 1)
        out.append(sum(signal[lo:hi]) / (hi - lo))
    return out

def correlation(a, b):
    n = len(a)
    mean_a = sum(a) / n
    mean_b = sum(b) / n
    num = sum((a[i] - mean_a) * (b[i] - mean_b) for i in range(n))
    den_a = sum((a[i] - mean_a) ** 2 for i in range(n)) ** 0.5
    den_b = sum((b[i] - mean_b) ** 2 for i in range(n)) ** 0.5
    return num / (den_a * den_b)

# --- CORE LOOP ---
N = 500
noise = lcg(seed=42, count=N)
signal_a = sine_wave(freq=0.05, count=N)
signal_b = sine_wave(freq=0.115, count=N)
true_pattern = [signal_a[i] + 0.5 * signal_b[i] for i in range(N)]
raw = [true_pattern[i] + noise[i] for i in range(N)]
recovered = moving_average(raw, window=25)
score = correlation(recovered, true_pattern)
score_rounded = round(score, 10)

# --- FINGERPRINT ---
fingerprint = hashlib.sha256(str(score_rounded).encode()).hexdigest()

print("=== DATAFRUCTUS - TEST 10 (CROSS-PLATFORM VALIDATION) ===")
print()
print(f"Python version:       {sys.version.split()[0]}")
print(f"Platform:             {platform.system()} {platform.machine()}")
print(f"Platform detail:      {platform.platform()}")
print()
print(f"Core loop result:     {score_rounded}")
print(f"Fingerprint (SHA256): {fingerprint}")
print()
print("Run this same script on any other device.")
print("If the fingerprint matches, portability is proven.")
