import sys
from pathlib import Path

from flake8.options.config import configparser as flake8_configparser

if sys.version_info < (3, 11):
    import tomli as tomllib
else:
    import tomllib


class PyprojectRawConfigParser(flake8_configparser.RawConfigParser):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        pyproject = Path().cwd() / "pyproject.toml"
        if not pyproject.exists():
            return
        with pyproject.open("rb") as f:
            settings = tomllib.load(f)
        if "tool" not in settings or "flake8" not in settings["tool"]:
            return
        if not self.has_section("flake8"):
            self.add_section("flake8")
        for (key, value) in settings["tool"]["flake8"].items():
            self.set("flake8", key, str(value))
