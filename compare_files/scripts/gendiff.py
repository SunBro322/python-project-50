#!/usr/bin/env python3
from compare_files.main_code_to_skripts import main_code
from compare_files.main_code_to_skripts import read_json

def main():
    main_code.scripts_for_diff()
    read_json.read_json()


if __name__ == '__main__':
    main()