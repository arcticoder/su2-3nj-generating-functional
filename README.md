# A Universal Generating Functional for SU(2) 3nj Symbols

**Author:** Arcticoder

## About this Repository

This repository contains a paper on a universal generating functional for SU(2) 3nj symbols. The mathematical content is best viewed through GitHub Pages, where the LaTeX equations are properly rendered.

## View the Paper

### [Click here to view the paper with rendered equations](https://arcticoder.github.io/su2-3nj-generating-functional/)

## Contents

This repository includes:

- `index.html` - The main HTML page with MathJax for equation rendering
- `index.md` - A markdown version with proper equation syntax for GitHub Pages
- `_config.yml` - Configuration for GitHub Pages with Jekyll
- Original LaTeX source file and PDF

## Included Scripts

This repository includes Python scripts that calculate and verify the mathematical results:

- [`compute_G_xy_series_coefficients.py`](scripts/compute_G_xy_series_coefficients.py): Computes series coefficients of the generating function for 6-j symbols.
- [`compute_hilbert_series_coefficients_n2_6.py`](scripts/compute_hilbert_series_coefficients_n2_6.py): Computes Hilbert series coefficients for \( n=2 \) to \( n=6 \).
- [`test_15j_generating_function.py`](scripts/test_15j_generating_function.py): Tests specific terms of the 15-j generating function.

## Data and Results

Results of running these scripts:

- [`series_coefficients_G_xy_up_to2.csv`](data/series_coefficients_G_xy_up_to2.csv)
- [`hilbert_series_coeffs_n2_6.csv`](data/hilbert_series_coeffs_n2_6.csv)
- [`15j_generating_function_tests.csv`](data/15j_generating_function_tests.csv)