#!/usr/bin/env python3

# Вызов файл с argparese для получения данных от пользователя
from gendiff.argparse import get_input_value
from gendiff.generate_diff import generate_diff

def main():
    """ Полученные данные отправляем в код generate_diff для выявление разницы"""
    file1, file2 = get_input_value()
    get_difference = generate_diff(file1, file2)
    print(get_difference)


if __name__ == '__main__':
    main()