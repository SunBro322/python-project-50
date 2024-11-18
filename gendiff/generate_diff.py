from gendiff.parse_files import get_info_from_file
from gendiff.diff import check_diff
from gendiff.view.json_view import view_json


def generate_diff(file_path1, file_path2):
    """ Данные полученые из main читаем через parse_files и обрабатываем"""
    values1 = get_info_from_file(file_path1)
    values2 = get_info_from_file(file_path2)
    return check_diff(values1, values2)
