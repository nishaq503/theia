"""Test the version number."""

import pathlib

from theia import __version__


def test_version() -> None:
    """Test the version number."""
    version_file = pathlib.Path(__file__).parent.parent.joinpath("VERSION")
    with version_file.open("r") as f:
        version = f.read().strip()

    assert __version__ == version, f"Version mismatch: {__version__} != {version}"
