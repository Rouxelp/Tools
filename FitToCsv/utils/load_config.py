import yaml
from pydantic import ValidationError
from schemas import Config

def load_config(yaml_path: str) -> Config:
    """
    Load and validate the configuration from a YAML file.

    Args:
        yaml_path (str): Path to the YAML configuration file.

    Returns:
        Config: A validated configuration object.

    Raises:
        ValidationError: If the YAML configuration is invalid.
    """
    with open(yaml_path, 'r') as file:
        config_data = yaml.safe_load(file)
    
    # Validate configuration with Pydantic
    try:
        config = Config(**config_data)
    except ValidationError as e:
        print(f"Configuration error in load_config: {e}")
        raise e
    
    return config
