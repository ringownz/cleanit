import pytest
from src.helpers import move_file, make_unique


def test_move_file(tmp_path):
    dest = tmp_path / "Destination"
    src = tmp_path / "Source"
    dest.mkdir()
    src.mkdir()
    p_src_file = src / "test.txt"
    p_src_file.write_text("test")

    assert len(list(dest.iterdir())) == 0
    assert len(list(src.iterdir())) == 1
    move_file(dest.resolve().as_posix(), src.resolve().as_posix(), "test.txt")
    assert len(list(dest.iterdir())) == 1
    assert len(list(src.iterdir())) == 0

def test_move_file_with_unique(tmp_path):
    dest = tmp_path / "Destination"
    src = tmp_path / "Source"
    dest.mkdir()
    p_dest_file_repetition = dest / "test.txt"  # Already exists file in Destination with same name
    p_dest_file_repetition.write_text("test")

    src.mkdir()
    p_src_file = src / "test.txt"
    p_src_file.write_text("test")

    assert len(list(dest.iterdir())) == 1
    assert len(list(src.iterdir())) == 1
    move_file(dest.resolve().as_posix(), src.resolve().as_posix(), "test.txt")
    assert len(list(dest.iterdir())) == 2
    assert len(list(src.iterdir())) == 0




def test_make_unique(tmp_path_factory):
    # Only apply this method when there's certain file with same name already exists

    # Create random directory and text file to verify uniqueness
    dest = tmp_path_factory.mktemp("Destination")
    test_file = dest / "test.txt"
    test_file.write_text("Hello")

    # Verifies if there's already a file with same name and creates new one
    new_name_file = make_unique(dest.resolve().as_posix(), "test.txt")

    assert len(list(dest.iterdir())) == 1
    assert new_name_file != "test.txt"
