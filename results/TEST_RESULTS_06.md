# DATAFRUCTUS ALGORITHMICA — TEST RESULTS 06

**Species:** Datafructus algorithmica (The Data Fruit)
**Creator:** Wagg
**Owner:** Family Tree Trust
**Distributor:** CTW, LLC
**Test Date:** 2026-09-25
**Test Type:** Real Dataset — UCI Air Quality Sensor Data

## Purpose

To determine whether the core loop functions on real-world data,
not just synthetic sine waves. This is the credibility test.

## Method

- Loaded the UCI Air Quality dataset (8,991 real sensor readings)
- Used the PT08.S1(CO) sensor response
- Took 1,000 readings
- Added Gaussian noise at 50% of signal std dev
- Destroyed 32% of the points
- Ran the core loop: Absorption, Pattern Recognition (fixed
  smoothing), Compression (20:1), Reconstruction (interpolation)
- Measured correlation between recovered and true signal

## Results

| Metric | Result | Meaning |
|--------|--------|---------|
| Dataset | UCI Air Quality | Real sensor data |
| Readings used | 1,000 | Sample size |
| Destroyed points | 316 (32%) | Missing data |
| Compression ratio | 20.0:1 | Kept 50 of 1,000 |
| Signal recovery correlation | 0.473 | Moderate recovery |
| Reconstruction correlation | 0.487 | Moderate rebuild |

## What This Shows

1. The core loop ran end-to-end on real sensor data without
   crashing or producing nonsense.
2. Recovery and reconstruction correlations were moderate —
   meaningfully above zero, far below synthetic results.
3. Real-world data is harder than synthetic data.

## Honest Boundary — Why the Numbers Dropped

The synthetic tests used a smooth sine-wave pattern that a simple
smoothing kernel can easily recover. Real sensor data is spiky,
non-stationary, and contains events that are not smooth. The
current kernel was tuned for smooth patterns. The drop from 0.968
to 0.473 is a result of using a smooth-pattern kernel on
non-smooth data.

This is a genuine finding. It tells the species what to evolve next.

## Output

Plot: test_06_real_dataset.png

## Status

Real-dataset test complete. Moderate recovery, honest limitation
identified. Next: adaptive kernel development.

(c) 2026 Family Tree Trust. All rights reserved.
Distributed by CTW, LLC.
