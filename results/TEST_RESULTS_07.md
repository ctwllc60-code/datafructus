# DATAFRUCTUS ALGORITHMICA — TEST RESULTS 07

**Species:** Datafructus algorithmica (The Data Fruit)
**Creator:** Wagg
**Owner:** Family Tree Trust
**Distributor:** CTW, LLC
**Test Date:** 2026-09-25
**Test Type:** Full Integration — All Eight Layers, Standalone

## Purpose

To prove the species functions as one unified system. Every
previous test exercised one or two layers. Test 07 runs all eight
layers in a single pipeline on real-world data, with no dependency
on any prior test.

## Method

- All eight layers run in sequence on the UCI Air Quality dataset
- Data: 1,000 real sensor readings
- 25% of points destroyed and rebuilt (Layer 8)
- Adaptive kernel used for pattern recognition (Layer 2)
- 30 exposures for learning memory (Layer 5)
- Dormancy check every 5th cycle (Layer 6)
- Plateau detection for resilience (Layer 7)

## Results

| Metric | Result | Meaning |
|--------|--------|---------|
| Source | UCI Air Quality (real) | Real sensor data |
| Recovery correlation | 0.608 | Pattern recovered from real data |
| Compression ratio | 20.0:1 | 1,000 to 50 points |
| Learning improvement | +0.024 | Score climbed across exposures |
| Dormancy cycles | 6 | Powered down when quiet |
| Resilience activations | 1 | Plateau broken |
| Layers executed | 8 of 8 | Full pipeline functional |

## What This Shows

1. All eight layers ran in one pipeline on real data.
2. Adaptive kernel improved real-data recovery: Test 06 used a
   fixed kernel and got 0.473; Test 07 used adaptive and got
   0.608 — a 28% relative improvement on the same dataset.
3. The species learned during the run: 0.782 to 0.806.
4. Dormancy and Resilience both activated inside the pipeline.
5. Reconstruction worked at scale: 265 destroyed points rebuilt.

## Honest Boundary

0.608 recovery is real but not high. A production-grade pattern
recognizer on this dataset would likely reach 0.80 or above. The
gap is the adaptive kernel — it responds to local variability but
does not yet learn structure across scales.

## Comparison Across Tests

| Test | Data | Recovery | Notes |
|------|------|----------|-------|
| 01 | Synthetic | 0.968 | Fixed kernel, smooth signal |
| 06 | Real | 0.473 | Fixed kernel, real signal |
| 07 | Real | 0.608 | Adaptive kernel, real signal |

The evolution from 06 to 07 is the species evolving to handle
real-world data.

## Output

Plot: test_07_full_integration.png

## Status

Full integration validated. The species functions as one system.

(c) 2026 Family Tree Trust. All rights reserved.
Distributed by CTW, LLC.
