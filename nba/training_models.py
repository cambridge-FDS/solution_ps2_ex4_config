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
    name: str
    type: str
    params: ParamConfig


class Config(BaseModel):
    data: DataConfig
    model: ModelConfig
