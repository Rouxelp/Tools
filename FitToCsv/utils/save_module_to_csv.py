import csv
import os
from pydantic import DirectoryPath
from typing import List, Dict


def save_module_to_csv(module_name: str, records: List[Dict[str, any]], base_dir: DirectoryPath) -> None:
    """
    Save records of a module as a CSV file in a specific directory.

    Args:
        module_name (str): The name of the module.
        records (List[Dict[str, any]]): List of records for the module.
        base_dir (DirectoryPath): The base directory where the CSV files will be saved.
    """

    try:
        # Define the path for the CSV file
        csv_file = os.path.join(base_dir, f"{module_name}.csv")

        if records:
            # Gather all unique keys from all records to handle variable fields dynamically
            all_fieldnames = set()
            for record in records:
                all_fieldnames.update(record.keys())
            headers = list(all_fieldnames)

            # Write the records to CSV, filtering out unknown fields
            with open(csv_file, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=headers, extrasaction='ignore')
                writer.writeheader()
                writer.writerows(records)
        
        print(f"Module '{module_name}' exported to {csv_file}")
    except Exception as e:
        print(f"Error exporting module '{module_name}': {e}")
        raise e