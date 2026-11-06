import pandas as pd
from .base import BaseTransformer

class PhoneFormatterTransformer(BaseTransformer):
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        if 'phone' in df.columns:
            df['phone'] = df['phone'].astype(str).str.replace(r'[\s\-\(\)]', '', regex=True)
        return df

TRANSFORMERS = {
    'phone_format': PhoneFormatterTransformer(),
}
