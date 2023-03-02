#!/usr/bin/env python3

import os

import openai

from lib import cli
from lib import fs
from lib import session


def request_filepath() -> str:
    print("\nEnter a filepath. ChatGPT will tell you what that file does.\n")
    return cli.prompt_user()


def main():
    system_instruction = (
        "You are an AI assistant that interprets code in a human-readable way."
    )
    chat_session = session.ChatSession(system_instruction=system_instruction)
    filepath = request_filepath()
    file_contents = fs.read_file(filepath)
    user_message_content = "\n".join(
        ("What does the following code do? Be succinct.", "", file_contents)
    )
    chat_session.ask(user_message_content)


if __name__ == "__main__":
    main()
