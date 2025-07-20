import sys
import os

import pytest


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from access_functions import (get_user_by_username,  # noqa: E402
                              get_script_ids_by_username,  # noqa: E402
                              get_scripts_by_username,  # noqa: E402
                              has_access_to_script,  # noqa: E402
                              get_script_file_by_id,  # noqa: E402
                              exists_user_with_username  # noqa: E402
                              )

from pytest import MonkeyPatch, fixture  # noqa: E402


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
    },
    {
        "id": 2,
        "file": "./scripts/different_example.sh"
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
    assert user["scriptIds"] == [1]


def test_get_user_by_username_not_found(use_test_db):
    user = get_user_by_username("NonExistent")
    assert user is None


def test_get_script_ids_by_username_found(use_test_db):
    script_ids = get_script_ids_by_username("Example")
    assert script_ids == [1]


def test_get_script_ids_by_username_not_found(use_test_db):
    with pytest.raises(TypeError):
        get_script_ids_by_username("NonExistent")


def test_get_scripts_by_username_found(use_test_db):
    scripts = get_scripts_by_username("Example")
    assert scripts == [
        {
            "id": 1,
            "file": "./scripts/example.sh"
        }
    ]


def test_get_scripts_by_username_not_found(use_test_db):
    with pytest.raises(TypeError):
        get_scripts_by_username("NonExistent")


def test_has_access_to_script_correct(use_test_db):
    assert has_access_to_script("Example", 1)


def test_has_access_to_script_false(use_test_db):
    assert has_access_to_script("Example", 2) is False


def test_has_access_to_script_user_doesnt_exist(use_test_db):
    with pytest.raises(TypeError):
        has_access_to_script("NonExistent", 1)


def test_has_access_to_script_user_and_script_doesnt_exist(use_test_db):
    with pytest.raises(TypeError):
        has_access_to_script("NonExistent", 3)


def test_has_access_to_script_script_doesnt_exist(use_test_db):
    assert has_access_to_script("Example", 3) is False


def test_get_script_file_by_id_example(use_test_db):
    assert get_script_file_by_id(1) == "./scripts/example.sh"


def test_get_script_file_by_id_different_example(use_test_db):
    assert get_script_file_by_id(2) == "./scripts/different_example.sh"


def test_get_script_file_by_id_doesnt_exist(use_test_db):
    assert get_script_file_by_id(3) is None


def test_exists_user_with_username_true(use_test_db):
    assert exists_user_with_username("Example") is True


def test_exists_user_with_username_false(use_test_db):
    assert exists_user_with_username("NonExistent") is False
