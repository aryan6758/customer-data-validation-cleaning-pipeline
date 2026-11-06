import sys
import os
from src.pipeline.config import load_config
from src.pipeline.core import Pipeline

def main():
    config_path = "config.yaml"
    if not os.path.exists(config_path):
        print(f"Error: Config file {config_path} not found.")
        sys.exit(1)

    config = load_config(config_path)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(config.output_path), exist_ok=True)

    pipeline = Pipeline(config)
    pipeline.run()
    print("Successfully processed customer data.")

if __name__ == "__main__":
    main()
