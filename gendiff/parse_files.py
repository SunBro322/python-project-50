import json
import yaml
from pathlib import Path


def get_info_from_file(path_file):
    file_ext = Path(path_file).suffix
    return open_file(path_file, file_ext)


def open_file(path_file, file_ext):
    """ Чтение Json """
    if file_ext.lower() == '.json':
        with open(Path(Path() / 'test' / 'fixtures' / path_file)) as f:
            return json.load(f)

    elif file_ext.lower() == '.yaml':
        with open(Path(Path() / 'test' / 'fixtures' / path_file)) as f:
            return yaml.safe_load(f)


