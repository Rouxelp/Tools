import pytest
from ..utils.process_fit_file import process_fit_file

@pytest.fixture
def fit_file_path():
    return "test_data/sample.fit"  # Provide a valid .fit file path for testing

def test_process_fit_file(fit_file_path):
    modules_to_export = ["record", "device_info"]
    result = process_fit_file(fit_file_path, modules_to_export)
    
    assert "record" in result
    assert "device_info" in result
    assert isinstance(result["record"], list)
    assert isinstance(result["device_info"], list)
