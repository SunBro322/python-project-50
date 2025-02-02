from gendiff.formatters.json import make_json_result
from gendiff.formatters.plain import make_plain_result
from gendiff.formatters.stylish import make_stylish_result


def format_diff(diff, formatter):
    match formatter:
        case 'stylish':
            return make_stylish_result(diff)
        case 'plain':
            return make_plain_result(diff)
        case 'json':
            return make_json_result(diff)
        case _:
            raise ValueError(f"Unsupported formatter: {formatter}")
