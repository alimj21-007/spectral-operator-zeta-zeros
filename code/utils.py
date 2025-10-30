import yaml
import pandas as pd
import numpy as np
import os

def load_params(config_path="config/params.yaml"):
    """
    Load numerical and structural parameters from YAML config
    """
    with open(config_path, "r") as f:
        params = yaml.safe_load(f)
    return params

def ensure_directories(paths=["data", "figures", "logs"]):
    """
    Create required directories if they don't exist
    """
    for path in paths:
        os.makedirs(path, exist_ok=True)

def load_csv_column(filepath, column):
    """
    Load a single column from a CSV file as NumPy array
    """
    df = pd.read_csv(filepath)
    return df[column].values

def normalize_array(arr):
    """
    Normalize array to zero mean and unit variance
    """
    return (arr - np.mean(arr)) / np.std(arr)

def spacing(arr):
    """
    Compute spacing between consecutive elements
    """
    return np.diff(np.sort(arr))

def relative_error(a, b):
    """
    Compute relative error between two arrays
    """
    return np.abs(a - b) / (np.abs(b) + 1e-12)

def save_array(arr, filename, label="value"):
    """
    Save 1D array to CSV
    """
    df = pd.DataFrame({label: arr})
    df.to_csv(filename, index=False)
    print(f"Saved array to {filename}")
