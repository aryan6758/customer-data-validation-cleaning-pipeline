import pandas as pd
from src.pipeline.config import PipelineConfig
from src.pipeline.core import Pipeline

def debug():
    df = pd.read_csv("data/sample/customers.csv")
    print("Original:\n", df)

    config = PipelineConfig(
        input_path="data/sample/customers.csv",
        output_path="data/output/cleaned_customers.csv",
        validators=['email', 'phone', 'name'],
        cleaners=['trim', 'nulls', 'case'],
        transformers=['phone_format']
    )

    pipeline = Pipeline(config)
    # We can't easily step through without modifying core.py,
    # but let's see what happens if we just run it.
    clean_df, invalid_df = pipeline.run()
    print("\nCleaned DF:\n", clean_df)
    print("\nInvalid DF:\n", invalid_df)

if __name__ == "__main__":
    debug()
