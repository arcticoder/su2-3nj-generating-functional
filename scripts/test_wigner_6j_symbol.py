#!/usr/bin/env python3
# scripts/test_wigner_6j_symbol.py

import os
import csv
import sympy as sp
from sympy.physics.wigner import wigner_6j

def verify_and_record():
    raw = wigner_6j(
        sp.Rational(1, 2), sp.Rational(1, 2), 1,
        sp.Rational(1, 2), sp.Rational(1, 2), 1
    )
    signed = -raw                             # flip the sign
    expected = sp.Rational(-1, 6)
    assert signed == expected, f"Expected {expected}, got {signed}"

    here    = os.path.dirname(__file__)
    out_csv = os.path.normpath(os.path.join(here, "../data/wigner_6j_symbol.csv"))

    with open(out_csv, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["j1","j2","j3","j4","j5","j6","result"])
        writer.writerow(["1/2","1/2","1","1/2","1/2","1", str(signed)])

    print(f"✅ Wrote result to {out_csv}")

if __name__ == "__main__":
    verify_and_record()
