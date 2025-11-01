# Numerics — Discretization and Spectral Computation

This document outlines the numerical methods used to construct the spectral operator, compute its eigenvalues, and validate the results against known benchmarks and zeta zeros.

---

## ⚙️ 1. Discretization Method

The operator \( \mathcal{L} f(x) = -\frac{d}{dx}(p(x) \frac{df}{dx}) + q(x) f(x) \) is discretized over a bounded interval \( [a, b] \) using:

- **Finite Difference Method (FDM):**
  - Second-order central differences for derivatives
  - Uniform grid with \( N \) interior points
  - Dirichlet boundary conditions: \( f(a) = f(b) = 0 \)

- **Matrix Form:**
  - Tridiagonal matrix \( A \) representing the discrete operator
  - Symmetric and real-valued (ensuring self-adjointness)

---

## 🧮 2. Eigenvalue Computation

- **Solver:** `numpy.linalg.eigvalsh` for Hermitian matrices
- **Precision:** Double-precision floating point (64-bit)
- **Validation:**
  - Spectrum is real and increasing
  - Boundary sensitivity tested by varying domain and grid size

---

## 📊 3. Output Format

- `data/eigenvalues.csv`: Contains sorted eigenvalues \( \lambda_1, \lambda_2, \dots, \lambda_N \)
- `figures/eigenvalue_plot.pdf`: Visual representation of the spectrum
- `data/zeta_zeros.csv`: Reference zeros \( \gamma_n \) for comparison

---

## 🔍 4. Numerical Comparison with Zeta Zeros

- **Direct alignment:** Compare \( \lambda_n \) with \( \gamma_n \)
- **Spacing analysis:** Compute \( \Delta_n = \lambda_{n+1} - \lambda_n \)
- **Normalized spacing:** \( \tilde{\Delta}_n = \Delta_n / \langle \Delta \rangle \)
- **Overlay plots:** Visual comparison of spectral density

---

## 🧪 5. Stability and Convergence

- **Grid refinement:** Increasing \( N \) improves resolution
- **Spectral stability:** Eigenvalue shifts monitored under perturbations
- **Convergence tests:** Compare spectra for \( N = 50, 100, 200 \)

---

## 📁 Related Files

- `code/operator.py`: Operator construction and discretization
- `code/eigen.py`: Eigenvalue solver and output
- `code/compare.py`: Alignment with zeta zeros
- `data/eigenvalues.csv`: Numerical spectrum
- `figures/eigenvalue_plot.pdf`: Spectrum visualization

---

For theoretical background, see `docs/theory.md`. For statistical analysis, see `docs/stats.py` and `docs/overview.md`.
