import json
import yaml
from pathlib import Path


def get_info_from_file(path_file):
    file_ext = Path(path_file).suffix
    return open_file(path_file, file_ext)


def open_file(path_file, file_ext):
    """ Чтение Json и Yaml """
    if file_ext.lower() == '.json':
        with open(Path(Path() / 'tests' / 'fixtures' / path_file)) as f:
            return json.load(f)

    elif file_ext.lower() == '.yaml' or file_ext.lower() == '.yml':
        with open(Path(Path() / 'tests' / 'fixtures' / path_file)) as f:
            return yaml.safe_load(f)
