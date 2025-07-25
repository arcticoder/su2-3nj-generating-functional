import sympy as sp
from sympy.physics.wigner import wigner_6j

def generate_3nj(*js):
    """
    Compute the Wigner 3nj symbol for the list of spins in js.
    Supports:
      - 6-j (len(js)==6) via sympy.physics.wigner.wigner_6j
      - 9-j (len(js)==9) via sympy.physics.wigner.wigner_9j (if available)
    """
    js_rat = [sp.Rational(j) for j in js]

    if len(js_rat) == 6:
        j1,j2,j3,j4,j5,j6 = js_rat
        return wigner_6j(j1, j2, j3, j4, j5, j6)
    elif len(js_rat) == 9:
        try:
            from sympy.physics.wigner import wigner_9j
        except ImportError:
            raise NotImplementedError("9-j not implemented in this Sympy build.")
        j1,j2,j3,j4,j5,j6,j7,j8,j9 = js_rat
        return wigner_9j(j1,j2,j3, j4,j5,j6, j7,j8,j9)
    else:
        raise NotImplementedError(f"generate_3nj only supports 6-j and 9-j, not {len(js)}-j.")

def recursion_3nj(*js):
    """
    Compute the Wigner 3nj symbol via explicit Racah summation
    (independent of sympy.physics.wigner).
    Supports:
      - 6-j: using Racah's formula
      - 9-j: delegated to sympy.physics.wigner.wigner_9j if available
    """
    js_rat = [sp.Rational(j) for j in js]
    if len(js_rat) == 6:
        j1, j2, j3, j4, j5, j6 = js_rat

        # Triangle checks
        if any([
            j1 + j2 < j3, j1 + j3 < j2, j2 + j3 < j1,
            j1 + j5 < j6, j1 + j6 < j5, j5 + j6 < j1,
            j4 + j2 < j6, j4 + j6 < j2, j2 + j6 < j4,
            j4 + j5 < j3, j4 + j3 < j5, j5 + j3 < j4
        ]):
            return sp.Rational(0)

        # Δ coefficient
        def delta(a, b, c):
            return sp.sqrt(
                sp.factorial(a + b - c) *
                sp.factorial(a - b + c) *
                sp.factorial(-a + b + c) /
                sp.factorial(a + b + c + 1)
            )

        prefactor = (
            delta(j1, j2, j3) *
            delta(j1, j5, j6) *
            delta(j4, j2, j6) *
            delta(j4, j5, j3)
        )

        # Summation bounds
        zmin = max(
            int(j1 + j2 + j3),
            int(j1 + j5 + j6),
            int(j4 + j2 + j6),
            int(j4 + j5 + j3)
        )
        zmax = min(
            int(j1 + j2 + j4 + j5),
            int(j2 + j3 + j5 + j6),
            int(j1 + j3 + j4 + j6)
        )

        total = sp.Rational(0)
        for z in range(zmin, zmax + 1):
            num = (-1)**z * sp.factorial(z + 1)
            den = (
                sp.factorial(z - int(j1 + j2 + j3)) *
                sp.factorial(z - int(j1 + j5 + j6)) *
                sp.factorial(z - int(j4 + j2 + j6)) *
                sp.factorial(z - int(j4 + j5 + j3)) *
                sp.factorial(int(j1 + j2 + j4 + j5) - z) *
                sp.factorial(int(j2 + j3 + j5 + j6) - z) *
                sp.factorial(int(j1 + j3 + j4 + j6) - z)
            )
            total += num / den

        return prefactor * total

    elif len(js_rat) == 9:
        try:
            from sympy.physics.wigner import wigner_9j
        except ImportError:
            raise NotImplementedError("9-j not implemented in this Sympy build.")
        j1,j2,j3,j4,j5,j6,j7,j8,j9 = js_rat
        return wigner_9j(j1,j2,j3, j4,j5,j6, j7,j8,j9)

    else:
        raise NotImplementedError(f"recursion_3nj only supports 6-j and 9-j, not {len(js)}-j.")
