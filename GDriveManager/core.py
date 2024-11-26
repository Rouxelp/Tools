from pydrive2.auth import GoogleAuth 
from pydrive2.drive import GoogleDrive
import pandas as pd
import io
from typing import Optional, Dict, List


class GoogleDriveManager:
    def __init__(self, credentials_file: str = 'credentials.json', client_secrets_file: str = 'client_secrets.json') -> None:
        """
        Initializes the GoogleDriveManager.
        
        :param credentials_file: Path to the file to store credentials.
        :param client_secrets_file: Path to the client secrets file for Google API.
        """
        self.gauth = GoogleAuth()
        self.gauth.LoadClientConfigFile(client_secrets_file)
        self.gauth.LoadCredentialsFile(credentials_file)
        
        if not self.gauth.credentials or self.gauth.access_token_expired:
            self.gauth.LocalWebserverAuth()
            self.gauth.SaveCredentialsFile(credentials_file)
        
        self.drive = GoogleDrive(self.gauth)

    def list_files(self, mime_type: str, folder_id: Optional[str] = None) -> List[Dict[str, str]]:
        """
        Lists files of a specific MIME type in a folder or root directory.
        
        :param mime_type: MIME type of the files to list.
        :param folder_id: Google Drive folder ID (optional, default is root).
        :return: List of files with ID and title.
        """
        query = f"mimeType='{mime_type}'"
        if folder_id:
            query += f" and '{folder_id}' in parents"
        
        file_list = self.drive.ListFile({'q': query}).GetList()
        return [{"id": file['id'], "title": file['title']} for file in file_list]

    def download_file(self, file_id: str) -> str:
        """
        Downloads a file from Google Drive and returns its content as a string.
        
        :param file_id: ID of the file on Google Drive.
        :return: Content of the file as a string.
        """
        file = self.drive.CreateFile({'id': file_id})
        file.FetchMetadata()
        return file.GetContentString()

    def upload_file(self, content: str, title: str, folder_id: Optional[str] = None) -> Dict[str, str]:
        """
        Uploads content to Google Drive as a new file.
        
        :param content: File content as a string.
        :param title: Title of the file.
        :param folder_id: Google Drive folder ID to upload to (optional, default is root).
        :return: Metadata of the uploaded file (ID and title).
        """
        file_metadata = {"title": title}
        if folder_id:
            file_metadata["parents"] = [{"id": folder_id}]
        
        file = self.drive.CreateFile(file_metadata)
        file.SetContentString(content)
        file.Upload()
        return {"id": file['id'], "title": file['title']}


class DriveCSV:
    def __init__(self, file_id: str, manager: GoogleDriveManager) -> None:
        """
        Initializes a DriveCSV object for a specific file on Google Drive.
        
        :param file_id: ID of the CSV file on Google Drive.
        :param manager: Instance of GoogleDriveManager to handle file operations.
        """
        self.file_id = file_id
        self.manager = manager
        self._dataframe: Optional[pd.DataFrame] = None

    def load(self) -> None:
        """
        Loads the CSV content from Google Drive into a pandas DataFrame.
        """
        content = self.manager.download_file(self.file_id)
        self._dataframe = pd.read_csv(io.StringIO(content))

    def get_dataframe(self) -> pd.DataFrame:
        """
        Returns the pandas DataFrame representation of the CSV.
        If the DataFrame is not yet loaded, it loads it first.
        
        :return: pandas DataFrame.
        """
        if self._dataframe is None:
            self.load()
        return self._dataframe

    def update_dataframe(self, dataframe: pd.DataFrame) -> None:
        """
        Updates the internal DataFrame and syncs changes back to Google Drive.
        
        :param dataframe: The updated pandas DataFrame.
        """
        self._dataframe = dataframe
        self._sync_to_drive()

    def _sync_to_drive(self) -> None:
        """
        Syncs the current DataFrame content back to Google Drive as a CSV.
        """
        if self._dataframe is None:
            raise ValueError("No DataFrame loaded to sync.")
        
        csv_content = self._dataframe.to_csv(index=False)
        self.manager.upload_file(content=csv_content, title="updated_file.csv", folder_id=None)

    def reload(self) -> None:
        """
        Reloads the CSV content from Google Drive, discarding local changes.
        """
        self.load()

    def save_as(self, title: str, folder_id: Optional[str] = None) -> None:
        """
        Saves the current DataFrame to a new file on Google Drive.
        
        :param title: Title for the new file.
        :param folder_id: Google Drive folder ID to save to (optional, default is root).
        """
        if self._dataframe is None:
            raise ValueError("No DataFrame loaded to save.")
        
        csv_content = self._dataframe.to_csv(index=False)
        self.manager.upload_file(content=csv_content, title=title, folder_id=folder_id)

if __name__ == "__main__":
    pass