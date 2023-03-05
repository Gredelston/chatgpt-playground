#!/usr/bin/env python3

from lib import types

CHATGPT_MODEL = "gpt-3.5-turbo"
SECRET_FILENAME = "secret.txt"

ROLE_USER = types.Role("user")
ROLE_ASSISTANT = types.Role("assistant")
ROLE_SYSTEM = types.Role("system")
