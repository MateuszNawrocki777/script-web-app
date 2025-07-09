from dataloader import SCRIPTS, USERS


def get_user_by_username(username: str):
    for user in USERS:
        if user["username"] == username:
            return user


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
