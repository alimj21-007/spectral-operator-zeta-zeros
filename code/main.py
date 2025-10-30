from utils import load_params, ensure_directories
from operator import build_operator, compute_eigenvalues
from eigen import save_eigenvalues
from compare import load_data, compare_spacing, plot_spacing
from plots import plot_eigenvalues, overlay_zeta_comparison
from logger import load_logging_config, init_logger, log_params

def main():
    # Setup
    ensure_directories()
    load_logging_config()
    logger = init_logger()
    logger.info("Starting spectral pipeline for Paper 3")

    # Load parameters
    params = load_params()
    log_params()
    N = params["domain"]["N"]
    k = params["eigenvalues"]["count"]

    # Step 1: Build operator and compute eigenvalues
    logger.info("Building operator and computing eigenvalues")
    H, x = build_operator(N=N)
    eigenvals = compute_eigenvalues(H, k=k)

    # Step 2: Save eigenvalues
    logger.info("Saving eigenvalues to CSV")
    save_eigenvalues(N=N, k=k)

    # Step 3: Load zeta zeros and compare
    logger.info("Loading zeta zeros and comparing spacing")
    eigen, zeta = load_data()
    delta_eigen, delta_zeta = compare_spacing(eigen, zeta)
    plot_spacing(delta_eigen, delta_zeta)

    # Step 4: Plot spectrum and overlay
    logger.info("Plotting eigenvalue spectrum and overlay with zeta zeros")
    plot_eigenvalues()
    overlay_zeta_comparison()

    logger.info("Pipeline completed successfully.")

if __name__ == "__main__":
    main()
