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
