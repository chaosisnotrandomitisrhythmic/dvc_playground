import argparse
import pandas as pd

from typing import Text

from src.utils.logs import get_logger
from src.utils.utils import load_config, ensure_dir


def subsample(config_path: Text) -> None:
    config = load_config(config_path)
    logger = get_logger("SUBSAMPLE", log_level=config["base"]["log_level"])

    train_df = pd.read_pickle(f'{config["data_load"]["save_path"]}train.pkl')
    test_df = pd.read_pickle(f'{config["data_load"]["save_path"]}test.pkl')

    train_df = train_df.sample(
        n=config["data_load"]["subsample_size"],
        random_state=config["base"]["random_state"],
    )
    test_df = test_df.sample(
        n=config["data_load"]["subsample_size"],
        random_state=config["base"]["random_state"],
    )

    save_dir = config["data_load"]["save_path"]
    ensure_dir(save_dir)
    logger.info(f"Save subsmaple training data with shape {train_df.shape}")
    train_df.to_pickle(f"{save_dir}/train_500.pkl")
    logger.info(f"Save subsample test data with shape {test_df.shape}")
    test_df.to_pickle(f"{save_dir}/test_500.pkl")


if __name__ == "__main__":
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument("--config", dest="config", required=True)
    args = args_parser.parse_args()

    subsample(config_path=args.config)
