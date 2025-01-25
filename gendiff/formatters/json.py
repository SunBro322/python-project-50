import json


def make_json_result(d_list):
    return json.dumps(d_list, indent=2)
