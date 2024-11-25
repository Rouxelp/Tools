import pytest
import os
import shutil
import yaml
from ..fit_to_csv import process_fit_to_csv
from pydantic import ValidationError

def test_valid_config():
    fit_path = "test_data/sample.fit"
    yaml_path = "config.yaml"
    output_dir = "test_output"
    
    # Exécute la fonction pour créer les fichiers de sortie
    process_fit_to_csv(fit_path, yaml_path, output_dir)
    
    # Assert that output directories and files exist
    assert os.path.isdir(output_dir)
    with open(yaml_path, 'r') as file:
        config_data = yaml.safe_load(file)
    for module in config_data["modules_to_export"]:
        module_dir = os.path.join(output_dir, module)
        csv_file = os.path.join(module_dir, f"{module}.csv")
        
        assert os.path.isdir(module_dir)
        assert os.path.isfile(csv_file)

    # Clean-up: supprimer le répertoire de sortie après le test
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)  # Supprime le dossier et tout son contenu

def test_invalid_config():
    with pytest.raises(ValidationError):
        process_fit_to_csv("sample.fit", "invalid_config.yaml", "test_output")
    
def test_nonexistent_fit_file():
    with pytest.raises(FileNotFoundError):
        process_fit_to_csv("nonexistent.fit", "config.yaml", "test_output")

def test_nonexistent_yaml_file():
    with pytest.raises(FileNotFoundError):
        process_fit_to_csv("sample.fit", "nonexistent.yaml", "test_output")
