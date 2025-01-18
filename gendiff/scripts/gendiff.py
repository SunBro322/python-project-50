#!/usr/bin/env python3


# Вызов файл с argparese для получения данных от пользователя
from gendiff.cli import get_input_value
from gendiff.generate_diff import generate_diff


def main():
    """ Полученные данные отправляем в
        код generate_diff для выявление разницы"""
    path_file1, path_file2, format_name = get_input_value()
    get_difference = generate_diff(path_file1, path_file2, format_name)
    print(get_difference)


if __name__ == '__main__':
    main()
