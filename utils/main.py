import json


def read_json(json_file: str):
    with open(json_file, mode="r", encoding="utf-8") as file:
        return json.load(file)
