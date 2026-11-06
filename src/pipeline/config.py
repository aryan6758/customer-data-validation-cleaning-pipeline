from typing import List, Dict, Any, Optional
import yaml
from pydantic import BaseModel

class PipelineConfig(BaseModel):
    input_path: str
    output_path: str
    validators: List[str]
    cleaners: List[str]
    transformers: List[str]

def load_config(config_path: str) -> PipelineConfig:
    with open(config_path, 'r') as f:
        data = yaml.safe_load(f)
    return PipelineConfig(**data)
