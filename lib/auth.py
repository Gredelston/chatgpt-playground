#!/usr/bin/env python3

import os

import openai

SECRET_FILEPATH = "secret.txt"

def authenticate() -> None:
    """Authenticate the OpenAI API with the locally saved secret key."""
    if not os.path.exists(SECRET_FILEPATH):
        raise FileNotFoundError(
            "You need to create a secret file, %s, containing your API key."
            % os.path.abspath(SECRET_FILEPATH))
    with open("secret.txt") as f:
        api_key = ''.join(f.readlines()).strip()
    openai.api_key = api_key
