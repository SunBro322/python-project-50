import pytest
from pathlib import Path
from gendiff import generate_diff


FIXTURES_DIR = Path(__file__).parent / 'fixtures'


def get_result_data(file_name):
    file_path = FIXTURES_DIR / file_name
    with open(file_path, 'r') as file:
        return file.read().strip()


@pytest.mark.parametrize(
    ('file1', 'file2', 'expected_file'),
    [
        (
            "flat_file1.json",
            "flat_file2.json",
            "expected_flat_diff.txt",
        ),
        (
            "flat_file1.yml",
            "flat_file2.yml",
            "expected_flat_diff.txt",
        ),
    ]
)
def test_stylish_flat(file1, file2, expected_file):
    file1_path = FIXTURES_DIR / file1
    file2_path = FIXTURES_DIR / file2
    expected_result = get_result_data(expected_file)
    result = generate_diff(str(file1_path), str(file2_path), 'stylish')
    assert result == expected_result


@pytest.mark.parametrize(
    ('file1', 'file2', 'expected_file'),
    [
        ("file1.json", "file2.json", "expected_diff.txt"),
        ("file1.yml", "file2.yml", "expected_diff.txt"),
    ]
)
def test_stylish_nested(file1, file2, expected_file):
    file1_path = FIXTURES_DIR / file1
    file2_path = FIXTURES_DIR / file2
    expected_result = get_result_data(expected_file)
    result = generate_diff(str(file1_path), str(file2_path), 'stylish')
    assert result == expected_result


@pytest.mark.parametrize(
    ('file1', 'file2', 'expected_file'),
    [
        ("file1.json", "file2.json", "expected_plain_output.txt"),
        ("file1.yml", "file2.yml", "expected_plain_output.txt"),
    ]
)
def test_plain_formatter(file1, file2, expected_file):
    file1_path = FIXTURES_DIR / file1
    file2_path = FIXTURES_DIR / file2
    expected_result = get_result_data(expected_file)
    result = generate_diff(str(file1_path), str(file2_path), 'plain')
    assert result == expected_result


@pytest.mark.parametrize(
    ('file1', 'file2', 'expected_file'),
    [
        ("file1.json", "file2.json", "expected_json_output.txt"),
        ("file1.yml", "file2.yml", "expected_json_output.txt"),
    ]
)
def test_json_formatter(file1, file2, expected_file):
    file1_path = FIXTURES_DIR / file1
    file2_path = FIXTURES_DIR / file2
    expected_result = get_result_data(expected_file)
    result = generate_diff(str(file1_path), str(file2_path), 'json')
    assert result == expected_result
