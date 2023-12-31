import argparse
from typing import Text
import yaml
from datasets import load_dataset
import pandas as pd
import os

from src.utils.logs import get_logger
from src.utils.utils import load_config, ensure_dir


def data_load(config_path: Text) -> None:
    """Load data from Hugging Face Hub.
    Args:
        config_path {Text}: path to config
    """
    config = load_config(config_path)
    logger = get_logger("DATA_LOAD", log_level=config["base"]["log_level"])

    logger.info("Get dataset")

    dataset = load_dataset("imdb")
    train_df = pd.DataFrame(dataset["train"])
    test_df = pd.DataFrame(dataset["test"])

    # Assuming `config` is your configuration dictionary
    save_dir = config["data_load"]["save_path"]
    ensure_dir(save_dir)
    logger.info("Save raw training data")
    train_df.to_pickle(f"{save_dir}/train.pkl")
    logger.info("Save raw test data")
    test_df.to_pickle(f"{save_dir}/test.pkl")


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--config", dest="config", required=True)
    args = args_parser.parse_args()

    data_load(config_path=args.config)
