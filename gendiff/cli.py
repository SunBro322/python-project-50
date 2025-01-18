import argparse


def get_input_value():
    """
    :param formats: Список допустимых форматов вывода.
    :return: Объект argparse.Namespace с аргументами.
    """
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    # Динамически формируем текст для help
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        choices=formats,  # Ограничиваем допустимые значения
        help=f'Select format of output from: {", ".join(formats)} (default: stylish)'
    )
    return parser.parse_args()
