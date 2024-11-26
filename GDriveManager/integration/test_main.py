import pytest
from unittest.mock import MagicMock
import pandas as pd
from GDriveManager.core import GoogleDriveManager, DriveCSV  

@pytest.fixture
def mocked_manager():
    manager = MagicMock(spec=GoogleDriveManager)
    return manager

@pytest.fixture
def drive_csv(mocked_manager):
    mocked_manager.download_file.return_value = "col1,col2\nval1,val2"
    return DriveCSV(file_id="1", manager=mocked_manager)

# --------------------------------------------------------------------------------
def test_download_file(mocked_manager):
    # Mock dowloaded file
    mocked_manager.download_file.return_value = "col1,col2\nval1,val2"

    content = mocked_manager.download_file("1")
    mocked_manager.download_file.assert_called_once_with("1")
    assert content == "col1,col2\nval1,val2"


def test_upload_file(mocked_manager):
    # Mock upload
    mocked_manager.upload_file.return_value = {"id": "123", "title": "uploaded.csv"}

    result = mocked_manager.upload_file(content="col1,col2\nval1,val2", title="uploaded.csv")
    mocked_manager.upload_file.assert_called_once_with(content="col1,col2\nval1,val2", title="uploaded.csv")
    assert result['id'] == "123"
    assert result['title'] == "uploaded.csv"

# --------------------------------------------------------------------------------

def test_load(drive_csv):
    drive_csv.load()
    drive_csv.manager.download_file.assert_called_once_with("1")
    assert isinstance(drive_csv._dataframe, pd.DataFrame)
    assert list(drive_csv._dataframe.columns) == ["col1", "col2"]


def test_get_dataframe(drive_csv):
    df = drive_csv.get_dataframe()
    assert isinstance(df, pd.DataFrame)
    assert df.iloc[0, 0] == "val1"  # Check first value


def test_reload(drive_csv):
    # Mock to simulate change in drive
    drive_csv.manager.download_file.return_value = "col1,col2\nnew_val1,new_val2"

    drive_csv.reload()
    df = drive_csv.get_dataframe()
    assert df.iloc[0, 0] == "new_val1"  # Vérifie la nouvelle valeur


