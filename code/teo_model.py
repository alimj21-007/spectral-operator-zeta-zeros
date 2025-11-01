import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def generate_tao_model(N=100, base_spacing=np.pi, noise_level=0.2, seed=42):
    """
    Generate pseudo-random model for zeta zeros:
    gamma_n ≈ n * base_spacing + noise
    """
    np.random.seed(seed)
    n = np.arange(1, N + 1)
    noise = np.random.normal(loc=0.0, scale=noise_level, size=N)
    gamma_model = n * base_spacing + noise
    return np.sort(gamma_model)

def compare_with_eigen(eigen_file="data/eigenvalues.csv", N=100, out="figures/tao_model_vs_eigen.pdf"):
    """
    Compare Tao-style model with computed eigenvalues
    """
    eigen = pd.read_csv(eigen_file)["eigenvalue"].values[:N]
    tao_model = generate_tao_model(N=N)

    plt.figure(figsize=(8, 5))
    plt.plot(eigen, label="Eigenvalues", marker='o')
    plt.plot(tao_model, label="Tao Model", marker='x')
    plt.title("Eigenvalues vs Tao Pseudo-Random Model")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)
    plt.savefig(out)
    print(f"Saved Tao model comparison plot to {out}")

def save_model(gamma_model, filename="data/tao_model.csv"):
    """
    Save generated Tao model to CSV
    """
    df = pd.DataFrame({"gamma_model": gamma_model})
    df.to_csv(filename, index=False)
    print(f"Saved Tao model data to {filename}")

if __name__ == "__main__":
    model = generate_tao_model(N=100)
    save_model(model)
    compare_with_eigen()
