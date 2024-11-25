import pytest
from ..utils.load_config import load_config
from pydantic import ValidationError

def test_load_config_valid():
    config = load_config("valid_config.yaml")  # Assume valid_config.yaml is correctly formatted
    assert config.modules_to_export == ["record", "device_info"]

def test_load_config_invalid():
    with pytest.raises(ValidationError):
        load_config("invalid_config.yaml")  # Assume invalid_config.yaml is incorrectly formatted
