#!/usr/bin/env python3

from typing import TypedDict


class Message(TypedDict):
    """A `message` object, as understood by the OpenAI ChatGPT API."""

    role: str
    content: str


class Role(str):
    """A `role` string, as understood by the OpenAI ChatGPT API.

    Typical values for this are 'system', 'user', and 'assistant'.
    """

    pass
