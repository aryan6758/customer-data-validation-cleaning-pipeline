import pytest
import pandas as pd
from src.pipeline.transformers.customer_transformers import PhoneFormatterTransformer

def test_phone_formatter():
    transformer = PhoneFormatterTransformer()
    df = pd.DataFrame({'phone': ['+1 (123) 456-7890', '123-456-7890']})
    result = transformer.transform(df)
    assert result['phone'].tolist() == ['+11234567890', '1234567890']
