#!/usr/bin/env python3

import pprint

import openai

from lib import constants
from lib import types


def send_messages(messages: list[types.Message], debug: bool = False) -> types.Message:
    """Send a bunch of messages to ChatGPT, and return the response message.

    Args:
        messages: The full message history to send to ChatGPT.
        debug: If true, print out the raw response from the ChatGPT API.
    """
    response = openai.ChatCompletion.create(
        model=constants.CHATGPT_MODEL, messages=messages
    )
    if debug:
        pprint.pprint(response)
    return types.Message(
        role=types.Role(response["choices"][0]["message"]["role"]),
        content=response["choices"][0]["message"]["content"],
    )


def send_message(message: types.Message) -> types.Message:
    """Send a single message to ChatGPT, and return the response message.

    Note that since we only tell ChatGPT about the one message, it won't have
    history for the rest of the chat session.
    """
    return send_messages([message])
