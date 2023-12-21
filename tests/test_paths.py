import pytest
from src.paths import get_paths
import tempfile


def test_paths(tmp_path):
    expectImages = (tmp_path / "Images").resolve().as_posix()
    expectVideos = (tmp_path / "Images" / "Videos").resolve().as_posix()
    expectScreenshots = (tmp_path / "Images" / "Screenshots").resolve().as_posix()
    expectCompressed = (tmp_path / "Compressed").resolve().as_posix()
    expectInstallers = (tmp_path / "Installers").resolve().as_posix()
    expectDocuments = (tmp_path / "Documents").resolve().as_posix()

    result = dict(get_paths(tmp_path))

    assert result["Images"] == expectImages
    assert result["Videos"] == expectVideos
    assert result["Compressed"] == expectCompressed
    assert result["Installers"] == expectInstallers
    assert result["Documents"] == expectDocuments
    assert result["Screenshots"] == expectScreenshots
