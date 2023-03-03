#!/usr/bin/env python3

"""Library for CLI interactions, such as input and output."""

import textwrap

from . import types


def print_message(message: types.Message) -> None:
    message_content = message["content"].strip()
    print(f"\n{message_content}\n")


def prompt_user(prompt: str = "> ") -> str:
    return input(prompt)
