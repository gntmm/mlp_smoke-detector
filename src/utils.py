# Import the required libraries.
import yaml
import joblib
from datetime import datetime

config_dir = "config/config.yaml"

def time_stamp():
    # Return the current date and time.
    return datetime.now()

def load_config():
    # Try to load the yaml file.
    try:
        with open(config_dir, "r") as file:
            config = yaml.safe_load(file)
    except FileNotFoundError as fe:
        raise RuntimeError("Parameters file not found in path.")
    
    return config

def pickle_load(file_path):
    # Load and return pickle file.
    return joblib.load(file_path)

def pickle_dump(data, file_path):
    # Dump data into pickle file.
    joblib.dump(data, file_path)
    
params = load_config()
PRINT_DEBUG = params["print_debug"]

def print_debug(messages):
    # Check whether user wants to use print or not.
    if PRINT_DEBUG:
        print(time_stamp(), messages)