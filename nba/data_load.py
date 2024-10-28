import pandas as pd
from pathlib import Path
from nba.config import config


def load_csv(data_path: Path) -> pd.DataFrame:
    return pd.read_csv(data_path)


if __name__ == "__main__":
    df = load_csv(config.data.data_path)
    print(df.head())
