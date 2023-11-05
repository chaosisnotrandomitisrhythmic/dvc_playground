from typing import Text, Dict
import yaml


def load_config(config_path: Text) -> Dict:
    """Load configuration from YAML file.
    Args:
       config_path {Text}: path to config
    """
    with open(config_path) as conf_file:
        config = yaml.safe_load(conf_file)
    return config
