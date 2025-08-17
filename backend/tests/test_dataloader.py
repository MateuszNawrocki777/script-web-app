import sys
import os

import copy


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataloader import (sanitize_scripts,  # noqa: E402
                        delete_filenames,  # noqa: E402
                        add_default_icons  # noqa: E402
                        )


TEST_SCRIPTS = [
    {
        "id": 1,
        "file": "./scripts/example.sh",
        "name": "Example",
        "icon": "ExampleIcon"
    },
    {
        "id": 2,
        "file": "./scripts/different_example.sh",
        "name": "DifferentExample",
    }
]


def test_delete_filenames():
    scripts = copy.deepcopy(TEST_SCRIPTS)
    delete_filenames(scripts)
    assert scripts == [
        {
            "id": 1,
            "name": "Example",
            "icon": "ExampleIcon"
        },
        {
            "id": 2,
            "name": "DifferentExample",
        }
    ]


def test_add_default_icons():
    scripts = copy.deepcopy(TEST_SCRIPTS)
    add_default_icons(scripts)
    assert scripts == [
        {
            "id": 1,
            "file": "./scripts/example.sh",
            "name": "Example",
            "icon": "ExampleIcon"
        },
        {
            "id": 2,
            "file": "./scripts/different_example.sh",
            "name": "DifferentExample",
            "icon": "/defaultScriptIcon.svg"
        }
    ]


def test_sanitize_scripts():
    scripts = sanitize_scripts(TEST_SCRIPTS)
    assert scripts == [
        {
            "id": 1,
            "name": "Example",
            "icon": "ExampleIcon"
        },
        {
            "id": 2,
            "name": "DifferentExample",
            "icon": "/defaultScriptIcon.svg"
        }
    ]
