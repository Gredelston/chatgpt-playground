#!/usr/bin/env python3

import os

import openai

from lib import constants
from lib import fs

def authenticate() -> None:
    """Authenticate the OpenAI API with the locally saved secret key."""
    if not os.path.exists(constants.SECRET_FILEPATH):
        raise FileNotFoundError(
            "You need to create a secret file, %s, containing your API key."
            % os.path.abspath(constants.SECRET_FILEPATH)
        )
    api_key = fs.read_file(constants.SECRET_FILEPATH)
    openai.api_key = api_key
