from gendiff.create_tree import build_diff
from gendiff.formatters import format_diff
from gendiff.parse_files import parse_data
import os


def get_file_format(file_path):
    _, extension = os.path.splitext(file_path)
    return extension[1:]


def read_and_parse_file(file_path):
    format_file = get_file_format(file_path)
    with open(file_path) as f:
        content = f.read()
        return parse_data(content, format_file)


def generate_diff(file_path1, file_path2, formatter='stylish'):
    data1 = read_and_parse_file(file_path1)
    data2 = read_and_parse_file(file_path2)
    diff = build_diff(data1, data2)
    return format_diff(diff, formatter)
