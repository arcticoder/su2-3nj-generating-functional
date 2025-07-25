# A Universal Generating Functional for SU(2) 3nj Symbols

**Author:** Arcticoder

## About this Repository

This repository contains a paper on a universal generating functional for SU(2) 3nj symbols.

## Mathematical Formulation

The master generating functional for Wigner 3nj recoupling coefficients is

$$
G(\{x_e\})
=\;\int \prod_{v=1}^n \frac{d^2w_v}{\pi}\,\exp\Bigl(-\sum_v\lVert w_v\rVert^2\Bigr)
\;\prod_{e=\langle i,j\rangle}\exp\bigl(x_e\,\epsilon(w_i,w_j)\bigr)
=\;\frac{1}{\sqrt{\det\!\bigl(I - K(\{x_e\})\bigr)}},
$$

where $K$ is the antisymmetric adjacency matrix of edge variables $x_e$.

#### 6-j Symbol Example
For the 6-j case ($n=4$) with two edge variables $x,y$,

$$
G(x,y)
=\;\frac{1}{\sqrt{\,(1 - x y - x - y)\,(1 + x y - x + y)\,(1 + x y + x - y)\,(1 - x y + x + y)\,}}.
$$

#### 9-j and 15-j Symbols
More generally,

$$
G(x,y,z)
=\;\frac{1}{\sqrt{\det\!\bigl(I_6 - K(x,y,z)\bigr)}},
\qquad
G(x_1,\dots,x_7)
=\;\frac{1}{\sqrt{\det\!\bigl(I_8 - K(x_1,\dots,x_7)\bigr)}}.
$$

## Included Scripts

This repository includes Python scripts that calculate and verify the mathematical results, as well as uncertainty‐quantification routines:

- [`compute_G_xy_series_coefficients.py`](scripts/compute_G_xy_series_coefficients.py): Computes series coefficients of the generating function for 6-j symbols.
- [`compute_hilbert_series_coefficients_n2_6.py`](scripts/compute_hilbert_series_coefficients_n2_6.py): Computes Hilbert series coefficients for \( n=2 \) to \( n=6 \).
- [`test_15j_generating_function.py`](scripts/test_15j_generating_function.py): Tests specific terms of the 15-j generating function.
- [`uq_determinant_stability.py`](scripts/uq_determinant_stability.py): Quantify numerical error in determinant evaluation of \(G(\{x_e\})\).
- [`uq_3nj_sensitivity.py`](scripts/uq_3nj_sensitivity.py): Local sensitivity analysis of the 6-j symbol under small spin perturbations.
- [`uq_compare_rational_vs_numeric.py`](scripts/uq_compare_rational_vs_numeric.py): Compare symbolic vs numeric evaluations of \(G(\{x_e\})\) for benchmark inputs.

## Data and Results

Results of running these scripts:

- [`series_coefficients_G_xy_up_to2.csv`](data/series_coefficients_G_xy_up_to2.csv)
- [`hilbert_series_coeffs_n2_6.csv`](data/hilbert_series_coeffs_n2_6.csv)
- [`15j_generating_function_tests.csv`](data/15j_generating_function_tests.csv)
- [`uq_determinant_stability.csv`](data/uq_determinant_stability.csv)
- [`uq_3nj_sensitivity.csv`](data/uq_3nj_sensitivity.csv)
- [`uq_compare_rational_vs_numeric.csv`](data/uq_compare_rational_vs_numeric.csv)