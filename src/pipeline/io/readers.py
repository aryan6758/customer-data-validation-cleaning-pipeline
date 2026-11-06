import pandas as pd
from typing import Optional

def read_csv(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def write_csv(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)
