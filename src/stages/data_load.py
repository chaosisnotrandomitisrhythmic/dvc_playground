import argparse
from typing import Text
import yaml
from datasets import load_dataset
import pandas as pd

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

    dataset = load_dataset("imdb")
    train_df = pd.DataFrame(dataset["train"])
    test_df = pd.DataFrame(dataset["test"])

    logger.info("Save raw data")
    train_df.to_pickle(config["data_load"]["dataset_train"])
    test_df.to_pickle(config["data_load"]["testset_test"])


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--config", dest="config", required=True)
    args = args_parser.parse_args()

    data_load(config_path=args.config)
