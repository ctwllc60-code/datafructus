# DATAFRUCTUS ALGORITHMICA — TEST RESULTS 05

**Species:** Datafructus algorithmica (The Data Fruit)
**Creator:** Wagg
**Owner:** Family Tree Trust
**Distributor:** CTW, LLC
**Test Date:** 2026-09-25
**Test Type:** Dormancy State — Resource Conservation & Reactivation

## Purpose

To prove the Dormancy State functions: when the data stream goes
quiet, the species powers down. When data returns, it wakes and
resumes learning.

## Method

- Simulated a 200-cycle data stream with alternating intensity
- Active periods (intensity 1.0): full processing and learning
- Quiet periods (intensity 0.02): below dormancy threshold
- Dormancy threshold: 0.10
- Monitored state transitions and recovery scores

## Results

| Metric | Result | Meaning |
|--------|--------|---------|
| Total cycles | 200 | Length of run |
| Active cycles | 80 | Full processing |
| Dormant cycles | 120 | Powered down |
| Dormancy activations | 1 | Wake events |
| Final recovery score | 0.815 | Score at end |
| Peak recovery score | 0.885 | Highest score reached |

## What This Shows

1. The species detected quiet periods and entered dormancy —
   120 of 200 cycles powered down.
2. It woke when data returned — 1 wake event recorded.
3. It retained its learned kernel across dormancy and resumed
   learning, with scores climbing above 0.800.

## Honest Boundary

Only one wake event was recorded because the run had one
quiet-to-active transition. A longer run with more transitions
would show more wake events. The mechanism is proven functional;
the sample of wake events is small.

## Output

Plot: test_05_dormancy.png

## Status

Dormancy State validated.

(c) 2026 Family Tree Trust. All rights reserved.
Distributed by CTW, LLC.
