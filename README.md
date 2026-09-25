# DATAFRUCTUS ALGORITHMICA
## The Data Fruit

**Creator:** Wagg
**Owner:** Family Tree Trust
**Distributor:** CTW, LLC
**Date:** 2026-09-25
**Version:** 1.0

---

## What This Is

A computational species that absorbs noisy data, recovers hidden
patterns, compresses them, learns across exposures, enters dormancy
when data is quiet, breaks through plateaus, and reconstructs
destroyed signal - all in one unified pipeline.

It is not a single algorithm. It is eight layers working together.

---

## Requirements

- Python 3.10 or higher
- pip
- A terminal (Linux, macOS, or Windows with WSL)

## Setup

    cd datafructus
    python3 -m venv venv
    source venv/bin/activate
    pip install numpy matplotlib pandas ucimlrepo

---

## Running the Tests

Each test is standalone in `scripts/`. Run them in order for the
full evolution story, or run any single one alone.

| Test | Command | Proves |
|------|---------|--------|
| 01 | `python3 scripts/test_01_core_loop.py` | Recovery, compression, reconstruction |
| 02 | `python3 scripts/test_02_learning_memory.py` | Improves with exposure |
| 03 | `python3 scripts/test_03_resilience_core.py` | Long-run improvement |
| 04 | `python3 scripts/test_04_resilience_forced.py` | Resilience Core fires |
| 05 | `python3 scripts/test_05_dormancy.py` | Sleeps when quiet, wakes |
| 06 | `python3 scripts/test_06_real_dataset.py` | Works on real data |
| 07 | `python3 scripts/test_07_full_integration.py` | All 8 layers together |
| 08 | `python3 scripts/test_08_benchmark.py` | Compares to PCA, zlib, MA |

---

## Output

Every test writes a plot to `results/`. Every test prints a metric
report to the terminal. Nothing is hidden.

---

## Folder Structure

    datafructus/
    ├── README.md          (this file)
    ├── scripts/           (all test scripts)
    ├── data/              (input data, if cached)
    └── results/           (plots + result documents)

---

## The Eight Layers

1. Absorption - takes in raw data from any source
2. Pattern Recognition - adaptive kernel finds hidden structure
3. Compression - keeps only what matters (20:1)
4. Emission - produces human-readable output
5. Learning Memory - improves with each exposure
6. Dormancy State - sleeps when data is quiet
7. Resilience Core - breaks through plateaus
8. Pattern Reconstruction - rebuilds destroyed signal

---

## Honest Boundaries

- Tests 01-05 use synthetic data (smooth sine waves)
- Tests 06-08 use the real UCI Air Quality dataset
- PCA outperforms Datafructus on raw recovery correlation
- Datafructus wins on capability breadth, not single-metric dominance
- All results were produced by the creator, not an independent party
- External verification (CODECHECK) is in progress

---

## Contact

Wagg
Family Tree Trust
Distributed by CTW, LLC
ctwllc60@gmail.com

---

(c) 2026 Family Tree Trust. All rights reserved.
Distributed by CTW, LLC.
