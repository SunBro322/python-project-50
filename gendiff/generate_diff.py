from gendiff.parse_files import read_json
from gendiff.diff import check_diff


def generate_diff(file_path1, file_path2):
    """ Данные полученые из main читаем через read_json и обрабатываем"""
    data_from_file1, data_from_file2 = read_json(file_path1, file_path2)
    return check_diff(data_from_file1, data_from_file2)
