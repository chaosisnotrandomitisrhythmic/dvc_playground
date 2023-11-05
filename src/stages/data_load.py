from typing import Text
import yaml
from datasets import load_dataset, Image

from src.utils.logs import get_logger


def data_load(config_path: Text) -> None:
    """Load data from Hugging Face Hub.
    Args:
        config_path {Text}: path to config
    """

    with open(config_path) as conf_file:
        config = yaml.safe_load(conf_file)

    logger = get_logger()

    logger.info("Get dataset")

    # dowload mnist from huggingface hub
