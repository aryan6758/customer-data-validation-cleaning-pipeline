import pandas as pd
import re
from .base import BaseValidator

class EmailValidator(BaseValidator):
    def validate(self, df: pd.DataFrame) -> pd.Series:
        # Simplified regex for better compatibility
        pattern = r'^[^@]+@[^@]+\.[^@]+$'
        return df['email'].astype(str).str.match(pattern)

class PhoneValidator(BaseValidator):
    def validate(self, df: pd.DataFrame) -> pd.Series:
        # Basic check for digits and length
        pattern = r'^\+?[\d\s\-()]{7,20}$'
        return df['phone'].astype(str).str.match(pattern)

class NameValidator(BaseValidator):
    def validate(self, df: pd.DataFrame) -> pd.Series:
        return df['name'].notnull() & (df['name'].astype(str).str.len() > 1)

VALIDATORS = {
    'email': EmailValidator(),
    'phone': PhoneValidator(),
    'name': NameValidator(),
}
