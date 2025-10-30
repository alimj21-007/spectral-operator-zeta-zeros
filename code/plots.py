import pandas as pd
import matplotlib.pyplot as plt

def plot_eigenvalues(filename="data/eigenvalues.csv", out="figures/eigenvalue_plot.pdf"):
    """
    Plot eigenvalues of operator H
    """
    df = pd.read_csv(filename)
    plt.figure(figsize=(8, 5))
    plt.plot(df["eigenvalue"], marker='o', linestyle='-', label="Eigenvalues")
    plt.title("Spectrum of Operator H")
    plt.xlabel("Index")
    plt.ylabel("Eigenvalue")
    plt.grid(True)
    plt.legend()
    plt.savefig(out)
    print(f"Saved eigenvalue plot to {out}")

def overlay_zeta_comparison(eigen_file="data/eigenvalues.csv", zeta_file="data/zeta_zeros.csv", out="figures/spectral_density_overlay.pdf"):
    """
    Overlay eigenvalue spectrum and zeta zero distribution
    """
    eigen = pd.read_csv(eigen_file)["eigenvalue"]
    zeta = pd.read_csv(zeta_file)["gamma"]

    plt.figure(figsize=(8, 5))
    plt.hist(eigen, bins=50, alpha=0.6, label="Eigenvalue Density")
    plt.hist(zeta, bins=50, alpha=0.6, label="Zeta Zero Density")
    plt.title("Spectral Density Overlay")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.savefig(out)
    print(f"Saved overlay plot to {out}")

if __name__ == "__main__":
    plot_eigenvalues()
    overlay_zeta_comparison()
