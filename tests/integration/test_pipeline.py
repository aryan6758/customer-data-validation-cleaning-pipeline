import pytest
import os
import pandas as pd
from src.pipeline.config import PipelineConfig
from src.pipeline.core import Pipeline

def test_full_pipeline(tmp_path):
    # Setup sample data
    input_csv = tmp_path / "input.csv"
    output_csv = tmp_path / "output.csv"
    df = pd.DataFrame({
        'name': [' John Doe ', 'Jane Smith', 'Invalid'],
        'email': ['JOHN@EXAMPLE.COM', 'jane@invalid', 'invalid'],
        'phone': ['+1 123-456-7890', '123', '456']
    })
    df.to_csv(input_csv, index=False)

    config = PipelineConfig(
        input_path=str(input_csv),
        output_path=str(output_csv),
        validators=['email', 'phone'],
        cleaners=['trim', 'case'],
        transformers=['phone_format']
    )

    pipeline = Pipeline(config)
    clean_df, invalid_df = pipeline.run()

    assert len(clean_df) == 1
    assert clean_df.iloc[0]['name'] == 'John Doe'
    assert clean_df.iloc[0]['email'] == 'john@example.com'
    assert clean_df.iloc[0]['phone'] == '+11234567890'
    assert os.path.exists(output_csv)
