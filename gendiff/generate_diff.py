from gendiff.parse_files import get_info_from_file
from gendiff.diff import check_diff
from gendiff.formatters.format_diff import format_diff


def generate_diff(file_path1, file_path2, format_name):
    """ Данные полученые из main читаем через parse_files и обрабатываем"""
    values1 = get_info_from_file(file_path1)
    values2 = get_info_from_file(file_path2)
    get_diff = check_diff(values1, values2)
    return format_diff(get_diff, format_name)
