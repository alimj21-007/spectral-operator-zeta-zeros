# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Semantic Versioning](https://semver.org/), and this project adheres to reproducibility and transparency standards.

---

## [1.0.0] — 2025-11-01  
### 🎉 Initial Public Release

- Completed all 8 phases of the research pipeline
- Constructed self-adjoint spectral operator with Dirichlet boundary conditions
- Computed eigenvalues numerically and exported to `eigenvalues.csv`
- Compared spectrum with Riemann zeta zeros (`zeta_zeros.csv`)
- Implemented spacing statistics and normalized distribution analysis
- Added spectral autocorrelation module (`correlation.py`)
- Simulated GOE/GUE ensembles via `rmt.py`
- Introduced Tao-style pseudo-random model (`tao_model.py`)
- Generated all visual outputs in `figures/` (PDF format)
- Documented theory, numerics, and bilingual overview in `docs/`
- Added unit tests for core modules in `tests/`
- Repository structured for reproducibility and public presentation

---

## [0.9.0] — 2025-10-25  
### ✳️ Pre-release Milestone

- Finalized operator discretization and eigenvalue solver
- Validated numerical stability across grid sizes
- Drafted `README.md`, `overview.md`, and Persian translation
- Integrated CSV export and plotting utilities
- Began statistical modeling phase

---

## [0.8.0] — 2025-10-10  
### 🧪 Internal Testing Phase

- Built modular codebase: `operator.py`, `eigen.py`, `compare.py`
- Imported reference zeta zeros from OEIS and LMFDB
- Conducted initial spacing and alignment tests
- Designed output schema for `data/` and `figures/`

---

## [0.1.0] — 2025-09-15  
### 🚧 Project Initialization

- Defined research goals and 8-phase roadmap
- Created repository structure and config files
- Added logging, YAML config, and `.gitignore`
