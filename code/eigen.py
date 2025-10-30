import numpy as np
from operator import build_operator, compute_eigenvalues
import pandas as pd

def save_eigenvalues(filename="data/eigenvalues.csv", N=500, k=50, W_func=None):
    """
    Build operator and save its eigenvalues to CSV
    """
    H, x = build_operator(N=N, W_func=W_func)
    eigenvals = compute_eigenvalues(H, k=k)
    df = pd.DataFrame({"eigenvalue": eigenvals})
    df.to_csv(filename, index=False)
    print(f"Saved {k} eigenvalues to {filename}")

if __name__ == "__main__":
    save_eigenvalues()
