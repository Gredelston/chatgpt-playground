#!/usr/bin/env python3

import os

import openai

from lib import auth
from lib import constants
from lib import types

_MODEL = "gpt-3.5-turbo"

def request_filepath() -> str:
    print("Give me a filepath, and ChatGPT will tell you what that file does!")
    filepath = input("> ")
    return os.path.expanduser(filepath)

def _get_file_contents(filepath: str) -> str:
    with open(filepath) as f:
        return "\n".join(f.readlines()).strip()

def ask_chatgpt_to_describe_file(filepath: str):
    file_contents = _get_file_contents(filepath)
    user_message_content = f"What does the following code do? Be succinct.\n\n{file_contents}"
    response = openai.ChatCompletion.create(
        model=_MODEL,
        messages=[
            types.Message(
                role=constants.ROLE_USER,
                content=user_message_content,
            ),
        ])
    print(response["choices"][0]["message"]["content"].strip())

if __name__ == "__main__":
    auth.authenticate()
    filepath = request_filepath()
    ask_chatgpt_to_describe_file(filepath)
