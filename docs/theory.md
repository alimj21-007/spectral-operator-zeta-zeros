# Theory — Spectral Operators and Zeta Zeros

This document outlines the mathematical foundations of the spectral operator constructed in this project, its numerical properties, and its connection to the nontrivial zeros of the Riemann zeta function.

---

## 🧮 1. Operator Definition

We define a self-adjoint differential operator \( \mathcal{L} \) on a bounded interval \( [a, b] \) with Dirichlet boundary conditions:

\[
\mathcal{L} f(x) = -\frac{d}{dx} \left( p(x) \frac{df}{dx} \right) + q(x) f(x)
\]

where:
- \( p(x) \) is a positive weight function (e.g., constant or smooth)
- \( q(x) \) is a potential function (e.g., zero or tunable)
- \( f(a) = f(b) = 0 \)

This operator is discretized using finite differences or spectral methods to compute its eigenvalues numerically.

---

## 📈 2. Spectral Properties

The operator \( \mathcal{L} \) admits a discrete spectrum \( \{ \lambda_n \} \), which is:
- Real and positive (due to self-adjointness)
- Increasing with \( n \)
- Sensitive to boundary conditions and potential \( q(x) \)

These eigenvalues are compared with the imaginary parts \( \gamma_n \) of the nontrivial zeros of the Riemann zeta function:

\[
\zeta\left(\frac{1}{2} + i\gamma_n\right) = 0
\]

---

## 🔍 3. Numerical Comparison

We compute:
- Direct alignment between \( \lambda_n \) and \( \gamma_n \)
- Spacing statistics: \( \Delta_n = \lambda_{n+1} - \lambda_n \)
- Normalized spacing distributions
- Spectral autocorrelation functions

These comparisons reveal structural similarities and deviations between the operator spectrum and zeta zeros.

---

## 🎲 4. Statistical Modeling

To deepen the comparison, we implement:
- **Random Matrix Theory (RMT):** Simulations of GOE/GUE ensembles and their spectral distributions
- **Wigner Surmise:** Analytical form for normalized spacing distribution
- **Tao-style Pseudo-Random Model:** Linear spacing with Gaussian noise

These models help interpret the statistical behavior of both spectra and assess their compatibility.

---

## 📚 5. Theoretical Context

The project is inspired by:
- Hilbert–Pólya conjecture: Suggesting a self-adjoint operator whose spectrum matches zeta zeros
- Berry–Keating framework: Linking quantum chaos and zeta statistics
- Conrey–Tao–Keating results: On correlations and spacing of zeros

While no formal proof is claimed, the numerical and statistical evidence supports further exploration of spectral-zeta connections.

---

For implementation details, see `code/operator.py`, `code/eigen.py`, and `code/stats.py`. For visual outputs, see `figures/` directory.
