# Google Drive CSV Manager

Welcome to **Google Drive CSV Manager** – your all-in-one solution for managing CSV files directly from Google Drive. This project is built to streamline the process of uploading, downloading, and analyzing CSV files using the Google Drive API and the power of Python.

## ✨ Features

- **Seamless Google Drive Authentication**: Authenticate easily with Google Drive using `PyDrive2`.
- **Effortless File Management**: Upload, download, and list files directly from Google Drive.
- **Powerful CSV Manipulation**: Load CSV files into a `pandas` DataFrame for easy analysis, update them, and sync your changes back to Google Drive.

## 🚀 Installation

To get started, install the necessary Python libraries. Simply run:

```bash
pip install pydrive2 pandas
```

Make sure to configure your Google API credentials (`client_secrets.json`) properly for authentication.

## 💡 Getting Started

### GoogleDriveManager: Your Google Drive Toolbox
The `GoogleDriveManager` class makes it easy to interact with Google Drive. It handles everything from authentication to file operations, all in one place.

#### 🔧 Initialization

```python
from google_drive_manager import GoogleDriveManager

drive_manager = GoogleDriveManager(credentials_file='credentials.json', client_secrets_file='client_secrets.json')
```

#### 📂 Listing Files
List files by their MIME type, and even filter them by folder if needed:

```python
files = drive_manager.list_files(mime_type='text/csv')
print(files)
```

#### 📥 Downloading a File
Get the content of a Google Drive file using its file ID:

```python
file_content = drive_manager.download_file(file_id='your_file_id')
print(file_content)
```

#### 📤 Uploading a File
Easily upload new content to Google Drive:

```python
upload_info = drive_manager.upload_file(content='Sample content', title='sample_file.txt')
print(upload_info)
```

### DriveCSV: Manage CSV Files Like a Pro
The `DriveCSV` class is your go-to tool for handling CSV files stored on Google Drive. Load, update, and manipulate CSV data with ease using `pandas`.

#### 🔧 Initialization

```python
from drive_csv import DriveCSV

# Initialize with the file ID of the CSV and the instance of GoogleDriveManager
drive_csv = DriveCSV(file_id='your_csv_file_id', manager=drive_manager)
```

#### 📊 Load CSV into DataFrame
Load your CSV content into a `pandas` DataFrame for powerful data manipulation:

```python
drive_csv.load()
df = drive_csv.get_dataframe()
print(df)
```

#### ✏️ Update DataFrame
Make changes to your DataFrame and sync them back to Google Drive:

```python
df['new_column'] = df['existing_column'] * 2  # Example modification
drive_csv.update_dataframe(df)
```

#### 💾 Save as a New File
Save your modified DataFrame as a new file on Google Drive:

```python
drive_csv.save_as(title='new_file.csv')
```

## 🔐 Authentication Setup
To use this utility, set up your Google API credentials by following these steps:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project and enable the **Google Drive API**.
3. Generate credentials and download the `client_secrets.json` file.
4. Place the `client_secrets.json` in your project root directory.

When you run the script for the first time, a local web server will help you complete the OAuth process.

## 🤝 Contributing
We welcome all contributions! If you find a bug or have an idea for improvement, feel free to open an issue or submit a pull request.

## ⚠️ Disclaimer
This project is intended for educational and personal use. Always comply with Google API guidelines when using this code in production environments.

---

