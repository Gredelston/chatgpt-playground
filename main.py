#!/usr/bin/env python3

import datetime
from typing import Any, Optional

import openai

from lib import auth
from lib import chatgpt
from lib import constants
from lib import display
from lib import types


class ChatSession:
    _MODEL = "gpt-3.5-turbo"

    def __init__(self) -> None:
        self._message_history: list[types.Message] = []

    @staticmethod
    def collect_input() -> str:
        return input("> ")

    def add_system_instruction(self, system_instruction: str):
        new_message = types.Message(
            role=constants.ROLE_SYSTEM, content=system_instruction
        )
        self._message_history.append(new_message)

    def solicit_system_instruction(self) -> None:
        print("What kind of bot would you like to chat with?")
        system_instruction = self.collect_input()
        if system_instruction:
            print("Sure, no problem.\n")
            self.add_system_instruction(system_instruction)
        else:
            print("Okay, we'll just fly by the seat of our pants.")

    def send_message(self, user_message_content: str):
        user_message = types.Message(
            role=constants.ROLE_USER, content=user_message_content
        )
        self._message_history.append(user_message)
        response_message = chatgpt.send_messages(self._message_history)
        self._message_history.append(response_message)
        display.print_message(response_message)

    def loop(self) -> None:
        user_input = self.collect_input()
        if not user_input:
            return
        self.send_message(user_input)
        self.loop()


def main() -> None:
    auth.authenticate()
    chat_session = ChatSession()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    chat_session.add_system_instruction(
        f"You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nCurrent date: {today}"
    )
    chat_session.loop()


if __name__ == "__main__":
    main()
