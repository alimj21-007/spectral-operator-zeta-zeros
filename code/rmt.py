import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def generate_random_matrix(N=100, ensemble="GUE"):
    """
    Generate a random Hermitian matrix from specified ensemble
    """
    if ensemble == "GOE":
        A = np.random.randn(N, N)
        H = (A + A.T) / 2
    elif ensemble == "GUE":
        A = np.random.randn(N, N) + 1j * np.random.randn(N, N)
        H = (A + A.conj().T) / 2
    else:
        raise ValueError("Ensemble must be 'GOE' or 'GUE'")
    return H

def compute_spectrum(H):
    """
    Compute eigenvalues of Hermitian matrix
    """
    return np.linalg.eigvalsh(H)

def compare_with_zeta(zeta_file="data/zeta_zeros.csv", N=100, ensemble="GUE", out="figures/rmt_vs_zeta.pdf"):
    """
    Compare spectrum of random matrix with zeta zeros
    """
    H = generate_random_matrix(N=N, ensemble=ensemble)
    rmt_eigen = compute_spectrum(H)
    zeta = pd.read_csv(zeta_file)["gamma"].values[:N]

    plt.figure(figsize=(8, 5))
    plt.hist(rmt_eigen, bins=50, alpha=0.6, label=f"{ensemble} Spectrum")
    plt.hist(zeta, bins=50, alpha=0.6, label="Zeta Zeros")
    plt.title("RMT Spectrum vs Zeta Zeros")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.savefig(out)
    print(f"Saved RMT comparison plot to {out}")

if __name__ == "__main__":
    compare_with_zeta()
