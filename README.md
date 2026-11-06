# Customer Data Validation & Cleaning Pipeline

A portfolio project demonstrating a production-ready data pipeline for cleaning and validating customer records.

## Features
- **Configurable Pipeline**: Define validators, cleaners, and transformers in `config.yaml`.
- **Modular Design**: Easy to add new validation or cleaning rules by extending base classes.
- **Data Quality**: Handles whitespace, case normalization, null values, and format validation.
- **Automated Testing**: Comprehensive unit and integration tests.

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the pipeline:
   ```bash
   python main.py
   ```

3. Run tests:
   ```bash
   pytest
   ```

## Project Structure
- `src/pipeline/`: Core logic
- `data/sample/`: Input datasets
- `data/output/`: Processed results
- `tests/`: Unit and integration tests
