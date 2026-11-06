import pandas as pd
from .base import BaseCleaner

class TrimWhitespaceCleaner(BaseCleaner):
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        for col in df.columns:
            if df[col].dtype == 'object' or pd.api.types.is_string_dtype(df[col]):
                df[col] = df[col].astype(str).str.strip()
        return df

class NullHandlerCleaner(BaseCleaner):
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        return df.fillna("Unknown")

class CaseNormalizerCleaner(BaseCleaner):
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        if 'name' in df.columns:
            df['name'] = df['name'].astype(str).str.title()
        if 'email' in df.columns:
            df['email'] = df['email'].astype(str).str.lower()
        return df

CLEANERS = {
    'trim': TrimWhitespaceCleaner(),
    'nulls': NullHandlerCleaner(),
    'case': CaseNormalizerCleaner(),
}
