import json
import copy


def load_scripts():
    with open("./scripts.json") as fh:
        return json.load(fh)


def load_users():
    with open("./users.json") as fh:
        return json.load(fh)


def sanitize_scripts(scripts):
    sanitized_scripts = copy.deepcopy(scripts)
    delete_filenames(sanitized_scripts)
    add_default_icons(sanitized_scripts)
    return sanitized_scripts


def delete_filenames(scripts):
    for script in scripts:
        script.pop("file")


def add_default_icons(scripts):
    for script in scripts:
        if not script.get("icon"):
            script["icon"] = "/defaultScriptIcon.svg"


SCRIPTS = load_scripts()
USERS = load_users()
FRONTEND_SCRIPTS = sanitize_scripts(SCRIPTS)
