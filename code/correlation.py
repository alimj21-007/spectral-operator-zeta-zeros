import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def load_sequence(file, column="eigenvalue", N=None):
    """
    Load numerical sequence from CSV
    """
    data = pd.read_csv(file)[column].values
    return data[:N] if N else data

def autocorrelation(x, max_lag=50):
    """
    Compute autocorrelation for lags up to max_lag
    """
    x = (x - np.mean(x)) / np.std(x)
    N = len(x)
    result = np.array([
        np.correlate(x[:N - lag], x[lag:])[0] / (N - lag)
        for lag in range(1, max_lag + 1)
    ])
    return result

def plot_autocorrelation(corr, out="figures/correlation_plot.pdf", label="Autocorrelation"):
    """
    Plot autocorrelation function
    """
    plt.figure(figsize=(8, 5))
    plt.plot(range(1, len(corr) + 1), corr, marker='o', linestyle='-', label=label)
    plt.title("Spectral Autocorrelation")
    plt.xlabel("Lag")
    plt.ylabel("Correlation")
    plt.grid(True)
    plt.legend()
    plt.savefig(out)
    print(f"Saved autocorrelation plot to {out}")

def save_autocorrelation(corr, filename="data/correlation.csv"):
    """
    Save autocorrelation values to CSV
    """
    df = pd.DataFrame({"lag": range(1, len(corr) + 1), "correlation": corr})
    df.to_csv(filename, index=False)
    print(f"Saved autocorrelation data to {filename}")

if __name__ == "__main__":
    spectrum = load_sequence("data/eigenvalues.csv")
    corr = autocorrelation(spectrum)
    save_autocorrelation(corr)
    plot_autocorrelation(corr)
