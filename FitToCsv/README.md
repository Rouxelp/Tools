# Garmin FIT to CSV Converter

This project is designed to convert Garmin `.fit` files into organized `.csv` files based on specific modules defined in a YAML configuration file. The process extracts data from the `.fit` file, structures it according to the specified modules, and saves each module's data as a `.csv` file in a separate directory. The output is organized under a main directory named after the original `.fit` file.

## Features
- **YAML Configuration**: Customize which modules to extract and convert to CSV through a flexible YAML file. To find out which modules are available and what data they contain, you can view a `.fit` file using this tool: [FIT File Viewer](https://www.fitfileviewer.com/).

- **Organized Export**: Each module is saved as a separate CSV file within its own folder, all located under a directory named after the `.fit` file.

## Prerequisites

- Python 3.12 or higher
- Python libraries listed in `requirements.txt`:
  - `fitparse`
  - `pydantic`
  - `pyyaml`
If testing is required, add: 
  - `pytest`

To install dependencies, run:
```bash
pip install -r requirements.txt
