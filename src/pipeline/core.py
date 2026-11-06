import pandas as pd
from .config import PipelineConfig
from .validators.customer_validators import VALIDATORS
from .cleaners.customer_cleaners import CLEANERS
from .transformers.customer_transformers import TRANSFORMERS
from .io.readers import read_csv
from .io.writers import write_csv

class Pipeline:
    def __init__(self, config: PipelineConfig):
        self.config = config

    def run(self):
        print(f"Loading data from {self.config.input_path}...")
        df = read_csv(self.config.input_path)
        initial_count = len(df)

        # 1. Cleaning
        print("Cleaning data...")
        for cleaner_key in self.config.cleaners:
            if cleaner_key in CLEANERS:
                df = CLEANERS[cleaner_key].clean(df)

        # 2. Transforming
        print("Transforming data...")
        for trans_key in self.config.transformers:
            if trans_key in TRANSFORMERS:
                df = TRANSFORMERS[trans_key].transform(df)

        # 3. Validating
        print("Validating data...")
        valid_mask = pd.Series([True] * len(df), index=df.index)
        for val_key in self.config.validators:
            if val_key in VALIDATORS:
                mask = VALIDATORS[val_key].validate(df)
                print(f"  Validator {val_key}: {mask.sum()} valid, { (~mask).sum() } invalid")
                valid_mask &= mask

        clean_df = df[valid_mask].copy()
        invalid_df = df[~valid_mask].copy()

        print(f"Pipeline complete: {len(clean_df)} valid, {len(invalid_df)} invalid (Total: {initial_count})")

        write_csv(clean_df, self.config.output_path)
        return clean_df, invalid_df
