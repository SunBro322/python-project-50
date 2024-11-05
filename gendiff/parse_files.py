import json

def read_json(file1, file2):
    """ Чтение Json """
    with open(file1, 'r') as open_file1, open(file2, 'r') as open_file2:
        info_from_file1 = open_file1.read()
        info_from_file2 = open_file2.read()

    return json.loads(info_from_file1), json.loads(info_from_file2)