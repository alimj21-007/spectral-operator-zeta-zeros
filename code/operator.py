import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

def potential(x, W_func=None):
    """
    Define the potential V(x) = x^2 + W(x)
    W_func: optional perturbation function W(x)
    """
    W = W_func(x) if W_func else np.zeros_like(x)
    return x**2 + W

def build_operator(a=0.1, b=10.0, N=500, W_func=None):
    """
    Construct the discrete operator H = -d²/dx² + V(x)
    with Dirichlet boundary conditions on (a, b)
    """
    x = np.linspace(a, b, N)
    h = x[1] - x[0]

    # Second derivative matrix (Dirichlet)
    main_diag = np.full(N, -2.0)
    off_diag = np.full(N - 1, 1.0)
    laplacian = diags([off_diag, main_diag, off_diag], [-1, 0, 1]) / h**2

    # Potential term
    V = potential(x, W_func)
    V_matrix = diags(V, 0)

    # Total operator
    H = -laplacian + V_matrix

    return H, x

def compute_eigenvalues(H, k=50):
    """
    Compute the lowest k eigenvalues of operator H
    """
    eigenvals = eigsh(H, k=k, which='SM', return_eigenvectors=False)
    return np.sort(eigenvals)
