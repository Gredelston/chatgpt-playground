#!/usr/bin/env python3

import datetime
from typing import Any, Optional

import openai

from lib import auth
from lib import chatgpt
from lib import constants
from lib import cli
from lib import types


class ChatSession:
    def __init__(self) -> None:
        self._message_history: list[types.Message] = []

    def add_system_instruction(self, system_instruction: str):
        new_message = types.Message(
            role=constants.ROLE_SYSTEM, content=system_instruction
        )
        self._message_history.append(new_message)

    def send_message(self, user_message_content: str):
        user_message = types.Message(
            role=constants.ROLE_USER, content=user_message_content
        )
        self._message_history.append(user_message)
        response_message = chatgpt.send_messages(self._message_history)
        self._message_history.append(response_message)
        cli.print_message(response_message)

    def loop(self) -> None:
        user_input = cli.prompt_user()
        self.send_message(user_input)
        self.loop()


def main() -> None:
    auth.authenticate()
    chat_session = ChatSession()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    chat_session.add_system_instruction(
        f"You are Nira, my personal robotic assistant. Answer as concisely as possible.\nCurrent date: {today}"
    )
    chat_session.loop()


if __name__ == "__main__":
    main()
