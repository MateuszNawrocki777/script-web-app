from fastapi import HTTPException

from dataloader import SCRIPTS, USERS


def get_user_by_username(username: str):
    for user in USERS:
        if user["username"] == username:
            return user
    raise HTTPException(status_code=400, detail="User not found")


def get_script_ids_by_username(username: str):
    user = get_user_by_username(username)
    return user["scriptIds"]


def get_scripts_by_username(username: str):
    script_ids = get_script_ids_by_username(username)
    script_list = []
    for script in SCRIPTS:
        if script["id"] in script_ids:
            script_list.append(script)
    return script_list


def has_access_to_script(username: str, script_id: int):
    return script_id in get_script_ids_by_username(username)


def get_script_file_by_id(script_id: int):
    for script in SCRIPTS:
        if script["id"] == script_id:
            return script["file"]
    raise HTTPException(status_code=400, detail="Script not found")
