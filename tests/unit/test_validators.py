import pytest
import pandas as pd
from src.pipeline.validators.customer_validators import EmailValidator, PhoneValidator

def test_email_validator():
    val = EmailValidator()
    df = pd.DataFrame({'email': ['test@example.com', 'invalid-email', None]})
    result = val.validate(df)
    assert result.tolist() == [True, False, False]

def test_phone_validator():
    val = PhoneValidator()
    df = pd.DataFrame({'phone': ['+1234567890', '123', None]})
    result = val.validate(df)
    assert result.tolist() == [True, False, False]
