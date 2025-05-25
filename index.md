---
layout: default
title: A Universal Generating Functional for SU(2) 3nj Symbols
---

# A Universal Generating Functional for SU(2) 3nj Symbols

**Arcticoder**

## Abstract

We introduce a master generating functional for Wigner 3nj recoupling coefficients based on
a Schwinger--boson Gaussian integral over spinors. For any trivalent coupling tree of SU(2) spins,
the generating function is given by

$$
G(\{x_e\})
\;=\;\int \prod_{v=1}^n \frac{d^2w_v}{\pi} \,\exp\bigl(-\sum_{v}\lVert w_v\rVert^2\bigr)
\;\prod_{e=\langle i,j\rangle}\exp\bigl(x_e\,\epsilon(w_i,w_j)\bigr)
\;=\;\frac{1}{\sqrt{\det\!\bigl(I - K(\{x_e\})\bigr)}},
$$

where $K$ is the antisymmetric adjacency matrix of edge--variables $x_e$. Expanding in powers of $x_e$
yields all 3nj coefficients. We demonstrate this construction explicitly for the 6-j, 9-j, and 15-j
symbols, providing a unified analytic framework that generalizes classical Poisson--kernel expansions.

## Included Scripts

This repository includes scripts that calculate and verify results:

- [compute_G_xy_series_coefficients.py](scripts/compute_G_xy_series_coefficients.py): Computes series coefficients of the generating function for 6-j symbols.
- [compute_hilbert_series_coefficients_n2_6.py](scripts/compute_hilbert_series_coefficients_n2_6.py): Computes Hilbert series coefficients for \( n=2 \) to \( n=6 \).
- [test_15j_generating_function.py](scripts/test_15j_generating_function.py): Tests specific terms of the 15-j generating function.

## Results

Results of running these scripts are available:

- [series_coefficients_G_xy_up_to2.csv](data/series_coefficients_G_xy_up_to2.csv)
- [hilbert_series_coeffs_n2_6.csv](data/hilbert_series_coeffs_n2_6.csv)
- [15j_generating_function_tests.csv](data/15j_generating_function_tests.csv)