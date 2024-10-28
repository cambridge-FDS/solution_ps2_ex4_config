from typing import List
from pydantic import BaseModel


class DataConfig(BaseModel):
    table: str
    data_path: str
    features_columns: List[str]


class ParamConfig(BaseModel):
    max_iter: int
    random_state: int


class ModelConfig(BaseModel):
    model_name: str
    model_type: str
    model_params: ParamConfig


class Config(BaseModel):
    data: DataConfig
    model: ModelConfig
