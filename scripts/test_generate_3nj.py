#!/usr/bin/env python3

import os, sys
# ensure the parent directory (repo root) is on Python’s import path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import csv
import json
import sympy as sp
from project.su2_3nj import generate_3nj

def test_generate_3nj_against_reference():
    # locate files relative to this script
    here     = os.path.dirname(__file__)
    ref_path = os.path.normpath(os.path.join(here, "../tests/reference_3nj.json"))
    out_csv  = os.path.normpath(os.path.join(here, "../data/generate_3nj_test_results.csv"))

    # load reference data
    with open(ref_path, "r") as f:
        ref = json.load(f)

    # prepare CSV
    with open(out_csv, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # header: j1,j2,...,result,expected,match
        first_key = next(iter(ref))
        njs = len(first_key.split(","))
        header = [f"j{i+1}" for i in range(njs)] + ["result", "expected", "match"]
        writer.writerow(header)

        # run each test
        for key, expected in ref.items():
            js = [sp.Rational(s) for s in key.split(",")]
            result = generate_3nj(*js)
            match = (str(sp.simplify(result)) == expected)
            writer.writerow(js + [str(result), expected, match])
            assert match, f"Mismatch for {key}: {result} != {expected}"

    print(f"✅ Wrote test results to {out_csv}")

if __name__ == "__main__":
    test_generate_3nj_against_reference()
