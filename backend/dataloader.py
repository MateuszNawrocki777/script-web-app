import json


def load_scripts():
    with open("./scripts.json") as fh:
        return json.load(fh)


def load_users():
    with open("./users.json") as fh:
        return json.load(fh)
