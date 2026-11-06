import pytest
import pandas as pd
from src.pipeline.cleaners.customer_cleaners import TrimWhitespaceCleaner, CaseNormalizerCleaner

def test_trim_cleaner():
    cleaner = TrimWhitespaceCleaner()
    df = pd.DataFrame({'name': ['  John  ', 'Jane '], 'email': [' a@b.com ', 'b@c.com']})
    result = cleaner.clean(df)
    assert result['name'].tolist() == ['John', 'Jane']
    assert result['email'].tolist() == ['a@b.com', 'b@c.com']

def test_case_normalizer():
    cleaner = CaseNormalizerCleaner()
    df = pd.DataFrame({'name': ['JOHN DOE', 'jane smith'], 'email': ['JOHN@EXAMPLE.COM', 'Jane@Example.com']})
    result = cleaner.clean(df)
    assert result['name'].tolist() == ['John Doe', 'Jane Smith']
    assert result['email'].tolist() == ['john@example.com', 'jane@example.com']
