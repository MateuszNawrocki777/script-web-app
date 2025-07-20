import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from access_functions import (get_user_by_username, get_script_ids_by_username,
                              get_scripts_by_username, has_access_to_script,
                              get_script_file_by_id, exists_user_with_username)

from pytest import MonkeyPatch, fixture


TEST_USERS = [
    {
        "username": "Example",
        "hashedPassword":
        "$2b$12$9bzBAiMJfSfgBsvvzj4MTepX14OhyzI8IAuGMJYaQMtmMto2WmjlC",
        "scriptIds": [1]
    }
]

TEST_SCRIPTS = [
    {
        "id": 1,
        "file": "./scripts/example.sh"
    }
]


@fixture
def use_test_db(monkeypatch: MonkeyPatch):
    monkeypatch.setattr("access_functions.USERS", TEST_USERS)
    monkeypatch.setattr("access_functions.SCRIPTS", TEST_SCRIPTS)


def test_sanity_test():
    assert True


def test_get_user_by_username_found(use_test_db):
    user = get_user_by_username("Example")
    assert user is not None
    assert user["username"] == "Example"


def test_get_user_by_username_not_found(use_test_db):
    user = get_user_by_username("NonExistent")
    assert user is None
