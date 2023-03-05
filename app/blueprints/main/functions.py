import json
from json import JSONDecodeError


def load_data_from_json(data_path):
    try:
        with open(data_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return None

    except JSONDecodeError:
        return None
