#!/usr/bin/env python3

import openai

from lib import constants
from lib import types

def send_messages(messages: list[types.Message]) -> types.Message:
    """Send a bunch of messages to ChatGPT, and return the response message."""
    response = openai.ChatCompletion.create(
        model=constants.CHATGPT_MODEL,
        messages=messages)
    return types.Message(
        role=types.Role(response["choices"][0]["message"]["role"]),
        content=response["choices"][0]["message"]["content"])

def send_message(message: types.Message) -> types.Message:
    """Send a single message to ChatGPT, and return the response message.

    Note that since we only tell ChatGPT about the one message, it won't have
    history for the rest of the chat session.
    """
    return send_messages([message])
