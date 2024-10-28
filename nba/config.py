# %%
import yaml
from nba.training_models import Config
from pathlib import Path


config_dict = yaml.safe_load((Path(__file__).parent.parent / "config.yaml").read_text())

config = Config.model_validate(config_dict)

# %%
# print(config.model.model_name)

# %%
