import pytest
from pathlib import Path
from gendiff import generate_diff


FIXTURES_DIR = Path(__file__).parent / 'fixtures'


def get_result_data(file_name):
    file_path = FIXTURES_DIR / file_name
    with open(file_path, 'r') as file:
        return file.read().strip()


@pytest.mark.parametrize(
    ('file1', 'file2', 'expected_file', 'formatter'),
    [
        (
            "flat_file1.json",
            "flat_file2.json",
            "expected_flat_diff.txt",
            "stylish"
        ),
        (
            "flat_file1.yml",
            "flat_file2.yml",
            "expected_flat_diff.txt",
            "stylish"
        ),
    ]
)
def test_flat_files(file1, file2, expected_file, formatter):
    file1_path = FIXTURES_DIR / file1
    file2_path = FIXTURES_DIR / file2
    expected_result = get_result_data(expected_file)
    result = generate_diff(str(file1_path), str(file2_path), formatter)
    assert result == expected_result, (
        f"Failed on {formatter} with {file1} and {file2}"
    )


@pytest.mark.parametrize(
    ('file1', 'file2', 'expected_file', 'formatter'),
    [
        ("file1.json", "file2.json", "expected_diff.txt", "stylish"),
        ("file1.yml", "file2.yml", "expected_diff.txt", "stylish"),
        ("file1.json", "file2.json", "expected_json_output.txt", "json"),
        ("file1.yml", "file2.yml", "expected_json_output.txt", "json"),
        ("file1.json", "file2.json", "expected_plain_output.txt", "plain"),
        ("file1.yml", "file2.yml", "expected_plain_output.txt", "plain"),
    ]
)
def test_formatters(file1, file2, expected_file, formatter):
    file1_path = FIXTURES_DIR / file1
    file2_path = FIXTURES_DIR / file2
    expected_result = get_result_data(expected_file)
    result = generate_diff(str(file1_path), str(file2_path), formatter)
    assert result == expected_result, (
        f"Failed on {formatter} with {file1} and {file2}"
    )
