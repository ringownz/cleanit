from src.ChaosAutomation import chaos_automation
from src.CleanAutomation import clean_automation
import pytest


@pytest.fixture
def setup(tmp_path):
    path_to_clean = tmp_path / "Chaos Folder"
    path_to_send_files = tmp_path / "Organized Folder"
    path_to_clean.mkdir()
    path_to_send_files.mkdir()

    list_files = [
        "test_file.txt", "test_file.png", "test_file.jpg", "test_file.pdf",
        "test_file.dmg", "test_file.xlsx", "test_file.png", "test_file.zip",
        "test_file.mp4", "Screenshot test_file.png"
    ]

    for file in list_files:
        create_file = path_to_clean / file
        create_file.touch()

    return path_to_clean, path_to_send_files, list_files


def test_chaos_automation(setup, tmp_path):  # Reverse from Clean Automation
    # Setup
    path_to_clean, path_to_send_files, list_files = setup
    # Organize first in order to create CHAOS after
    clean_automation(path_to_clean.resolve().as_posix(), path_to_send_files.resolve().as_posix())
    assert len(list(path_to_send_files.iterdir())) == 4  # obtains direct children
    assert len(list(path_to_clean.iterdir())) == 0

    # Generate CHAOS

    chaos_automation(path_to_send_files.resolve().as_posix(), path_to_clean.resolve().as_posix())

    assert len(list(path_to_clean.iterdir())) == 9  # Not clean
    assert len(list(path_to_send_files.iterdir())) == 0  # Not organized
    # Chaos created
