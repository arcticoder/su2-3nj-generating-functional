#!/usr/bin/env python3
# scripts/validate_biedenharn_elliott_identity.py

import os
import csv
import sympy as sp
from sympy.physics.wigner import wigner_6j

def validate_identity():
    # nine spins = 1
    a,b,c,d,e,f,p,q,r = [sp.Rational(1)]*9

    # admissible x-range
    x_min = max(abs(a-b), abs(c-d), abs(e-f))
    x_max = min(a+b,     c+d,     e+f)

    # build LHS
    J = a+b+c+d+e+f+p+q+r
    lhs = sp.Rational(0)
    for x in range(int(x_min), int(x_max)+1):
        xr = sp.Rational(x)
        phase = (-1)**(J + xr)
        lhs += phase*(2*xr+1) * (
            wigner_6j(a, b, xr, c, d, f)
          * wigner_6j(c, e, d, f, xr, q)
          * wigner_6j(e, b, f, a, xr, r)
        )

    # RHS: product of two 6-j’s
    rhs = (
        wigner_6j(p, e, q, a, r, d)
      * wigner_6j(p, f, q, b, r, c)
    )

    lhs_s = sp.simplify(lhs)
    rhs_s = sp.simplify(rhs)
    diff  = sp.simplify(lhs_s - rhs_s)

    # record to CSV
    out = os.path.join(os.path.dirname(__file__), "../data/biedenharn_elliott_identity.csv")
    with open(out, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["a","b","c","d","e","f","p","q","r","lhs","rhs","diff"])
        writer.writerow(
            list(map(str, (a,b,c,d,e,f,p,q,r)))
          + [str(lhs_s), str(rhs_s), str(diff)]
        )

    print(f"✅ Wrote result to {out}")
    assert diff == 0, f"Pentagon identity failed: LHS={lhs_s}, RHS={rhs_s}, diff={diff}"

if __name__ == "__main__":
    validate_identity()
