# DATAFRUCTUS ALGORITHMICA — TEST RESULTS 12

**Species:** Datafructus algorithmica (The Data Fruit)
**Creator:** Wagg
**Owner:** Family Tree Trust
**Distributor:** CTW, LLC
**Test Date:** 2026-09-25
**Test Type:** Data Perturbation (Robustness)
**Document Type:** Full Technical Record

---

## Purpose of Test

Real-world data is never clean. Sensors fail. Readings drift.
Values spike. Data drops out. A species that only works on
perfect data is useless in a factory.

This test measures how well Datafructus recovers the underlying
pattern when the input is deliberately corrupted in six different
ways.

## Method

The same hidden pattern used in prior tests: two sine waves
combined (frequencies 0.05 and 0.115) over 1,000 data points.

Six perturbations were applied, one at a time. Each corrupted
version was passed through the same core loop — smoothing with
window 25, then correlation measured against the true pattern.

The baseline for comparison: the clean pattern plus mild noise
(std 0.3). That is the score the species gets when conditions
are good.

### The Six Perturbations

1. **Heavy noise** — Gaussian noise with std 2.5 added to every
   point (8x the baseline noise level).
2. **Missing data** — 30% of points randomly removed, then filled
   by linear interpolation before recovery.
3. **Outliers** — 5% of points replaced with random garbage at
   std 20 (extreme spikes).
4. **Stuck sensor** — 100 consecutive points frozen at a single
   value, simulating a sensor lock-up.
5. **Baseline drift** — a slow linear shift (0 to 3) added across
   the whole signal, simulating sensor calibration drift.
6. **Total corruption** — 100% random values, no underlying
   pattern. This is the control: the species should fail here.

## Actual Results

**Baseline (clean + mild noise): 0.9964**

| Perturbation | Recovery Score | Retention vs Baseline |
|--------------|----------------|-----------------------|
| Heavy noise (std 2.5) | 0.8519 | 85.5% |
| Missing data (30% gaps) | 0.9941 | 99.8% |
| Outliers (5% garbage) | 0.6286 | 63.1% |
| Stuck sensor (100 pts flat) | 0.9021 | 90.5% |
| Baseline drift | 0.4833 | 48.5% |
| Total corruption | -0.1644 | -16.5% |

**Tests survived (>0.5 recovery): 4 of 6**

## Verdict

**RESILIENT**

## Detailed Analysis

### What the Species Handles Well

**Missing data: 99.8% retention.** This is the strongest result.
Even with 30% of the data gone, the species recovers nearly the
same pattern as it does from clean input. For a sensor
deployment, this means data dropouts — a constant reality in
industrial settings — barely affect performance.

**Stuck sensor: 90.5% retention.** When 100 consecutive points
freeze on a single value, the species still finds the pattern.
A stuck sensor is one of the most common real-world failures;
the species is not fooled by it.

**Heavy noise: 85.5% retention.** Eight times the baseline noise
level, and the species still recovers 85% of the pattern. Noisy
environments do not break it.

### What the Species Struggles With

**Outliers: 63.1% retention.** When 5% of points become extreme
spikes, the species is dragged off the pattern. A single garbage
reading, amplified 20x, distorts the local average enough to
throw off the recovery. This is a real weakness.

**Baseline drift: 48.5% retention.** When the whole signal drifts
slowly upward, the species cannot tell the difference between
drift and pattern. It smooths the drift into the signal,
producing a distorted result. Real sensors drift; this is a
limitation that matters.

**Total corruption: -16.5% retention.** This is the control test.
With no pattern to find, the species returns noise. This is
correct behavior — the species does not hallucinate a pattern
that is not there.

## What This Proves

1. The species survives 4 of 6 real-world corruption types.
2. Missing data and stuck sensors — the two most common
   industrial failures — are handled nearly perfectly.
3. The species does not hallucinate patterns in random data.
4. Two specific weaknesses are identified: outlier spikes and
   baseline drift.

## Honest Boundary

This test measured the core loop only. The full eight-layer
pipeline includes the Resilience Core and the Learning Memory,
which could be tuned to address outliers and drift. But this test
did not exercise those layers — it tested the species as it
behaves out of the box.

The two weaknesses found here are actionable. A future version
could add outlier detection (flagging points that deviate too far
from local neighbors) and drift subtraction (removing slow
trends before pattern recovery). Those are the next evolutions.

## Real-World Implication

In a factory setting:
- A wire shorts out → data drops → species still works (99.8%)
- A sensor freezes → species still works (90.5%)
- A machine vibrates → noise increases → species still works (85.5%)
- A random voltage spike → species is confused (63.1%)
- A sensor slowly drifts out of calibration → species is confused (48.5%)

The species is deployable today for three of the five real-world
scenarios. The two weaknesses define the roadmap for v1.7.

## Comparison to Prior Tests

Test 06 measured real sensor data (UCI Air Quality) with mild
corruption — result 0.473. Test 12 is the first test that
systematically measures the species against specific corruption
types. Together they show the species is robust in real conditions
and identifies where it needs work.

## Output Artifact

Script: scripts/test_12_perturbation.py
Text results: results/test_12_perturbation.txt

## Signed

**Creator:** Wagg
**Owner:** Family Tree Trust
**Date:** 2026-09-25

(c) 2026 Family Tree Trust. All rights reserved.
Distributed by CTW, LLC.
