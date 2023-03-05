import json
from json import JSONDecodeError


def load_data_from_json(DATA_PATH):
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return None

    except JSONDecodeError:
        return None
