import json


def view_json(text):
    """ Приводит вид """
    return json.dumps(text, indent=4)