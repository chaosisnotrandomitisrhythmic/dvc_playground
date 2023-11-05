from typing import Text, Dict
import yaml
import os


def load_config(config_path: Text) -> Dict:
    """Load configuration from YAML file.
    Args:
       config_path {Text}: path to config
    """
    with open(config_path) as conf_file:
        config = yaml.safe_load(conf_file)
    return config


def ensure_dir(file_path: Text) -> None:
    # Extract the directory from the file path
    directory = os.path.dirname(file_path)

    # Check if the directory exists, and create it if it doesn't
    if not os.path.exists(directory):
        os.makedirs(directory)
