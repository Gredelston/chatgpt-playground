#!/usr/bin/env python3

import os

import openai

from lib import auth
from lib import chatgpt
from lib import constants
from lib import display
from lib import types


def request_filepath() -> str:
    print("Give me a filepath, and ChatGPT will tell you what that file does!")
    filepath = input("> ")
    return os.path.expanduser(filepath)


def _get_file_contents(filepath: str) -> str:
    with open(filepath) as f:
        return "\n".join(f.readlines()).strip()


def ask_chatgpt_to_describe_file(filepath: str):
    file_contents = _get_file_contents(filepath)
    user_message_content = "\n".join(
        ("What does the following code do? Be succinct.", "", file_contents)
    )
    user_message = types.Message(role=constants.ROLE_USER, content=user_message_content)
    response_message = chatgpt.send_message(user_message)
    display.print_message(response_message)


if __name__ == "__main__":
    auth.authenticate()
    filepath = request_filepath()
    ask_chatgpt_to_describe_file(filepath)
