import os
import pytest
from ..utils.save_module_to_csv import save_module_to_csv  

@pytest.fixture
def output_dir(tmp_path):
    # Crée un répertoire temporaire pour tester
    return tmp_path / "output"

def test_save_module_csv(output_dir):
    # Nom du module et enregistrements de test
    module_name = "test_module"
    records = [{"field1": "value1", "field2": "value2"}, {"field1": "value3", "field2": "value4"}]

    # Appelle la fonction pour sauvegarder
    save_module_to_csv(module_name, records, output_dir)
    
    # Vérifie que le répertoire et le fichier CSV sont créés
    module_dir = os.path.join(output_dir, module_name)
    csv_file = os.path.join(module_dir, f"{module_name}.csv")

    assert os.path.isdir(module_dir)
    assert os.path.isfile(csv_file)

    # Vérifie le contenu du fichier CSV
    with open(csv_file, 'r') as file:
        lines = file.readlines()
        assert len(lines) == 3  # En-têtes + 2 lignes de données
        assert lines[0].strip() == "field1,field2"  # En-tête
        assert lines[1].strip() == "value1,value2"
        assert lines[2].strip() == "value3,value4"
