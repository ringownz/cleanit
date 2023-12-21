import os
import shutil

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


def test_clean_automation_with_both_input(setup, tmp_path):
    path_to_clean, path_to_send_files, list_files = setup

    list_of_files_to_clean = list(path_to_clean.iterdir())
    list_of_files_send_to = list(path_to_send_files.iterdir())

    assert len(list_of_files_send_to) == 0
    assert len(list_of_files_to_clean) == 9
    clean_automation(path_to_clean.resolve().as_posix(), path_to_send_files.resolve().as_posix())

    list_of_files_to_clean = list(path_to_clean.iterdir())
    list_of_files_send_to = list(os.walk(path_to_send_files))  # Gets list with all the files and directory children
    count_files = 0  # count only files that belong to setup
    for root, dirs, files in list_of_files_send_to:
        for file in files:
            if file in list_files:
                count_files += 1

    assert len(list(path_to_send_files.iterdir())) == 4  # obtains direct childs
    assert count_files == 9
    assert len(list_of_files_to_clean) == 0


