#!/usr/bin/env python3

import os

import openai

from lib import auth
from lib import chatgpt
from lib import constants
from lib import cli
from lib import fs
from lib import types


def request_filepath() -> str:
    print("\nEnter a filepath. ChatGPT will tell you what that file does.\n")
    return cli.prompt_user()


def ask_chatgpt_to_describe_file(filepath: str):
    file_contents = fs.read_file(filepath)
    user_message_content = "\n".join(
        ("What does the following code do? Be succinct.", "", file_contents)
    )
    user_message = types.Message(role=constants.ROLE_USER, content=user_message_content)
    response_message = chatgpt.send_message(user_message)
    cli.print_message(response_message)


if __name__ == "__main__":
    auth.authenticate()
    filepath = request_filepath()
    ask_chatgpt_to_describe_file(filepath)
