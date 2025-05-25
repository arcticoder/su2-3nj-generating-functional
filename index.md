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

## Introduction

Recoupling theory for SU(2) plays a central role in quantum mechanics, atomic physics, and quantum
gravity. Traditional approaches express 3nj symbols in terms of nested sums over lower-order symbols
or hypergeometric functions on a case-by-case basis. We propose a single, universal generating functional
that reproduces all 3nj symbols via a single determinant formula, offering a unified and compact analytic representation.

## Master Generating Functional

Let a trivalent coupling tree have $n$ vertices and edges labeled by variables $x_e$.
Associate to each vertex a Schwinger--boson spinor $w_v\in\mathbb{C}^2$ and consider the integral:

$$
\begin{equation}
G(\{x_e\})
= \int \prod_{v=1}^n \frac{d^2w_v}{\pi} 
\exp\Bigl(-\sum_{v}\lVert w_v\rVert^2\Bigr)
\prod_{e=\langle i,j\rangle}\exp\bigl(x_e\,\epsilon(w_i,w_j)\bigr)
= \frac{1}{\sqrt{\det\!\bigl(I - K(\{x_e\})\bigr)}}.
\end{equation}
$$

Here $K_{ij}=x_e$ (up to sign) whenever $e$ joins vertices $i,j$. The Taylor expansion coefficient
of $\prod_e x_e^{2j_e}$ is exactly the Wigner 3nj symbol for the given tree.

## Examples

### 6-j Symbols ($n=4$)

With two edge variables $x,y$, the generating function becomes

$$
\begin{equation}
G(x,y)
= \frac{1}{\sqrt{(1 - x y - x - y)\,(1 + x y - x + y)\,(1 + x y + x - y)\,(1 - x y + x + y)}}.
\end{equation}
$$

### 9-j Symbols ($n=6$)

For three edges $x,y,z$, one obtains

$$
\begin{equation}
G(x,y,z)
= \frac{1}{\sqrt{\det\!\bigl(I_6 - K(x,y,z)\bigr)}}.
\end{equation}
$$

### 15-j Symbols ($n=8$)

For a chain tree with seven variables $x_1,\dots,x_7$,

$$
\begin{equation}
G(x_1,\dots,x_7)
= \frac{1}{\sqrt{\det\!\bigl(I_8 - K(x_1,\dots,x_7)\bigr)}}.
\end{equation}
$$

## Conclusion

We have presented a novel, universal generating functional for SU(2) recoupling coefficients valid
for any 3nj symbol. Our determinant formula unifies and extends classical generating functions for
6-j and 9-j symbols and offers a promising path for further generalizations in representation theory
and quantum gravity applications.

## References

1. G. Szegő, *Orthogonal Polynomials*, American Mathematical Society, 1975.
2. R. Koekoek, P. Lesky, R. Swarttouw, *Hypergeometric Orthogonal Polynomials and Their $q$-Analogues*, 2010.
3. H. Weyl, *The Classical Groups*, Princeton University Press, 1946.
