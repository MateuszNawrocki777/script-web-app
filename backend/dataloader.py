import json


def load_scripts():
    with open("./scripts.json") as fh:
        return json.load(fh)
