from setuptools import setup, find_packages

with open(r"C:\Users\polro\OneDrive\Bureau\Elise\Tools\GDriveManager\requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="gdrive_manager",                 # Nom du package
    version="0.1.0",                # Version initiale
    description="Transform ﬁtness tracker data to CSV.",
    author="Pol Rouxel",
    author_email="pol.rouxel@p1blue.com",
    packages=find_packages(),       # Inclut tous les modules dans my_tool/
    include_package_data=True,      # Inclut des fichiers comme .env dans le package
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "gdrive_manager=gdrive_manager.core:main",  # Commande CLI (optionnel)
        ],
    },
)
