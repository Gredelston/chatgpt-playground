#!/usr/bin/env python3

"""Library for CLI interactions, such as input and output."""

import textwrap

from . import types


def print_message(message: types.Message) -> None:
    text_wrapper = textwrap.TextWrapper(
        initial_indent="\t",
        subsequent_indent="\t",
        tabsize=4,
    )
    message_content = message["content"].strip()
    wrapped_lines = text_wrapper.wrap(message_content)
    print("\n" + "\n".join((line for line in wrapped_lines)) + "\n")


def prompt_user(prompt: str = "> ") -> str:
    return input(prompt)
