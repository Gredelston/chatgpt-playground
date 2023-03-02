#!/usr/bin/env python3

from . import types

CHATGPT_MODEL = "gpt-3.5-turbo"
SECRET_FILEPATH = "secret.txt"

ROLE_USER = types.Role("user")
ROLE_ASSISTANT = types.Role("assistant")
ROLE_SYSTEM = types.Role("system")
