import os
from typing import TypedDict
import yaml


class ButtonConfig(TypedDict):
    padding_x: int
    padding_y: int
    width: int
    height: int
    color: str
    background_color: str


class Config(TypedDict):
    grid_columns: int
    background_color: str
    button: ButtonConfig


def config_exists():
    return os.path.exists("config.yaml")


def load_config() -> Config | None:
    try:
        with open("config.yaml", "r", encoding="utf-8") as stream:
            return yaml.safe_load(stream)
    except (FileNotFoundError, yaml.YAMLError):
        return None


def _copy_file(src: str, dest: str):
    # Open the source file for reading
    with open(src, "rb") as source_file:
        # Open the destination file for writing
        with open(dest, "wb") as dest_file:
            # Read from the source and write to the destination
            dest_file.write(source_file.read())


def create_from_template():
    _copy_file("config.yaml.template", "config.yaml")


_config: Config | None = None


def _initalise():
    global _config  # pylint: disable=global-statement
    if _config is None:
        if not config_exists():
            create_from_template()
        _config = load_config()
        if _config is None:
            raise RuntimeError("Failed to load config")
    return _config


config = _initalise()
