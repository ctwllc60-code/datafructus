# DATAFRUCTUS ALGORITHMICA — TEST RESULTS 09

**Species:** Datafructus algorithmica (The Data Fruit)
**Creator:** Wagg
**Owner:** Family Tree Trust
**Distributor:** CTW, LLC
**Test Date:** 2026-09-25
**Test Type:** Reproducibility Audit

---

## Purpose of Test

To prove the species produces identical results on identical
inputs. A buyer must be able to trust that what they see is what
they get — not a one-time fluke.

## Method

Ran the core loop 10 times with the same random seed (42) and the
same input parameters. Measured the recovery correlation on each
run. If the species is deterministic, all 10 runs produce the
exact same number.

## Results

| Run | Recovery Correlation |
|-----|----------------------|
| 1 | 0.967803 |
| 2 | 0.967803 |
| 3 | 0.967803 |
| 4 | 0.967803 |
| 5 | 0.967803 |
| 6 | 0.967803 |
| 7 | 0.967803 |
| 8 | 0.967803 |
| 9 | 0.967803 |
| 10 | 0.967803 |

**Unique results across 10 runs: 1**

## Result

**PASS — perfectly reproducible.**

## What This Proves

1. The species is deterministic. Given the same input, it always
   produces the same output.
2. Results are not random or one-time flukes.
3. Anyone who runs this test will get the same numbers.

## Honest Boundary

This test proves reproducibility of the core loop with a fixed
seed. It does not prove reproducibility across different hardware
or operating systems. A future cross-platform test would confirm
the species behaves identically everywhere.

## Output Artifact

Results file: `test_09_reproducibility.txt`
Script: `scripts/test_09_reproducibility.py`

## Signed

**Creator:** Wagg
**Owner:** Family Tree Trust
**Date:** 2026-09-25

(c) 2026 Family Tree Trust. All rights reserved.
Distributed by CTW, LLC.
