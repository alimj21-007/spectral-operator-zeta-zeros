import pandas as pd
import matplotlib.pyplot as plt

def load_data(eigen_file="data/eigenvalues.csv", zeta_file="data/zeta_zeros.csv"):
    """
    Load eigenvalues and zeta zeros from CSV
    """
    eigen = pd.read_csv(eigen_file)["eigenvalue"].values
    zeta = pd.read_csv(zeta_file)["gamma"].values
    return eigen, zeta

def compare_spacing(eigen, zeta):
    """
    Compare spacing statistics between eigenvalues and zeta zeros
    """
    delta_eigen = np.diff(eigen)
    delta_zeta = np.diff(zeta)
    return delta_eigen, delta_zeta

def plot_spacing(delta_eigen, delta_zeta, filename="figures/spacing_comparison.pdf"):
    """
    Plot spacing comparison
    """
    plt.figure(figsize=(8, 5))
    plt.plot(delta_eigen, label="Eigenvalue Spacing")
    plt.plot(delta_zeta, label="Zeta Zero Spacing")
    plt.legend()
    plt.title("Spacing Comparison")
    plt.xlabel("Index")
    plt.ylabel("Spacing")
    plt.savefig(filename)
    print(f"Saved spacing plot to {filename}")

if __name__ == "__main__":
    eigen, zeta = load_data()
    delta_eigen, delta_zeta = compare_spacing(eigen, zeta)
    plot_spacing(delta_eigen, delta_zeta)
