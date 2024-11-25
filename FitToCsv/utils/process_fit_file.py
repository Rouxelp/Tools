from fitparse import FitFile
from typing import List, Dict

def process_fit_file(fit_path: str, modules_to_export: List[str]) -> Dict[str, List[Dict[str, any]]]:
    """
    Load a .fit file and extract specific modules based on a list of module names.

    Args:
        fit_path (str): Path to the .fit file.
        modules_to_export (List[str]): List of modules to extract from the .fit file.

    Returns:
        Dict[str, List[Dict[str, any]]]: A dictionary with module names as keys and a list of records as values.
    """
    # Load FIT file
    fitfile = FitFile(fit_path)
    
    # Dictionary to store module data
    modules: Dict[str, List[Dict[str, any]]] = {}

    # Traverse all messages in the FIT file
    for message in fitfile.get_messages():
        module_name = message.name
        
        # Only process modules specified in the configuration
        if module_name not in modules_to_export:
            continue
        
        # Initialize module list if it doesn't exist
        if module_name not in modules:
            modules[module_name] = []
        
        # Extract field data from message
        data = {field.name: field.value for field in message.fields}
        modules[module_name].append(data)

    return modules
