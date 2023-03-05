#!/usr/bin/env python3

import inspect
import os

import openai

from lib import constants
from lib import fs


def get_secret_file_abspath() -> str:
    auth_filepath = inspect.stack()[0][1]
    lib_path = os.path.join(auth_filepath, '..')
    playground_path = os.path.join(lib_path, '..')
    secret_filepath = os.path.join(playground_path, constants.SECRET_FILENAME)
    return os.path.abspath(secret_filepath)


def authenticate() -> None:
    """Authenticate the OpenAI API with the locally saved secret key."""
    secret_filepath = get_secret_file_abspath()
    if not os.path.exists(secret_filepath):
        raise FileNotFoundError(
            "You need to create a secret file, %s, containing your API key."
            % os.path.abspath(secret_filepath)
        )
    api_key = fs.read_file(secret_filepath)
    openai.api_key = api_key
