
# Spectral Operators and Zeta Zeros — Numerical and Statistical Comparison

📊 This repository contains the full pipeline for constructing self-adjoint spectral operators, computing their eigenvalues, and comparing them numerically and statistically with the nontrivial zeros of the Riemann zeta function.

---

## 🔍 Overview

This project implements and analyzes a spectral operator defined over a bounded domain with Dirichlet boundary conditions. The eigenvalues of this operator are computed numerically and compared with the imaginary parts of the nontrivial zeros of the Riemann zeta function. The comparison includes:

- Direct numerical alignment
- Spacing statistics and normalized distributions
- Spectral autocorrelation
- Random matrix theory (RMT) simulations
- Pseudo-random modeling (Tao-style)

---

## 🧩 Structure

├── config/           # YAML and logging configuration ├── data/             # CSV files: eigenvalues, zeta zeros, spacing, correlation ├── figures/          # PDF plots: spacing, overlay, autocorrelation ├── code/             # Modular scripts: operator, eigen, stats, rmt, tao_model ├── notebooks/        # Interactive Jupyter notebooks ├── docs/             # Markdown documentation (overview, theory, FAQ, Persian) ├── tests/            # Unit tests for reproducibility
---

## ⚙️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/alimj21-007/riemann-operator-analysis.git
   cd riemann-operator-analysis

2.Install dependencies:

pip install -r requirements.txt

3.Run the pipeline:

python code/main.py

4.Generate statistical plots:

python code/stats.py
python code/rmt.py
python code/correlation.py
python code/tao_model.py

📁 Key Outputs

data/eigenvalues.csv: Computed eigenvalues of the operator

data/zeta_zeros.csv: Reference zeta zeros

figures/spacing_comparison.pdf: Histogram of normalized spacings

figures/spectral_density_overlay.pdf: Overlay of eigenvalues and zeta zeros

figures/correlation_plot.pdf: Spectral autocorrelation

figures/tao_model_vs_eigen.pdf: Comparison with pseudo-random model

📚 Documentation

docs/overview.md: Project summary and goals

docs/theory.md: Mathematical background and operator construction

docs/faq.md: Common questions and usage tips

docs/translation-fa.md: Persian-language summary and outreach

🧠 Author & Vision

This repository is part of a broader research program led by Ali, focused on connecting spectral operators to zeta zero statistics with full reproducibility, bilingual documentation, and public accessibility.

📜 License

MIT License — see LICENSE file for details.


