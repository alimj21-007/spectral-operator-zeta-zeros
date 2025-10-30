import logging
import os
import yaml

def load_logging_config(config_path="config/logging.ini"):
    """
    Load logging configuration from INI file
    """
    if os.path.exists(config_path):
        logging.config.fileConfig(config_path)
    else:
        logging.basicConfig(level=logging.INFO)
        logging.warning(f"No logging.ini found at {config_path}, using default config.")

def init_logger(name="spectral_logger"):
    """
    Initialize and return a named logger
    """
    logger = logging.getLogger(name)
    return logger

def log_params(params_path="config/params.yaml", log_path="logs/params.log"):
    """
    Log current parameter settings to file
    """
    if not os.path.exists("logs"):
        os.makedirs("logs")
    with open(params_path, "r") as f:
        params = yaml.safe_load(f)
    with open(log_path, "w") as f:
        for section, values in params.items():
            f.write(f"[{section}]\n")
            for key, val in values.items():
                f.write(f"{key}: {val}\n")
            f.write("\n")
    logging.info(f"Parameters logged to {log_path}")
