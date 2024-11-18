from gendiff.parse_files import get_info_from_file
from gendiff.diff import check_diff
from gendiff.formatters.stylish import stylish


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """ Данные полученые из main читаем через parse_files и обрабатываем"""
    values1 = get_info_from_file(file_path1)
    values2 = get_info_from_file(file_path2)
    return stylish(check_diff(values1, values2))
