#!/usr/bin/env python3

import datetime
from typing import Any, Optional

import openai


def _authenticate() -> None:
    """Tell OpenAI about my secret key."""
    with open("secret.txt") as f:
        api_key = ''.join(f.readlines()).strip()
    openai.api_key = api_key


class ChatSession:
    _MODEL = "gpt-3.5-turbo"

    def __init__(self) -> None:
        self._message_history: list[dict[str, str]] = []

    @staticmethod
    def collect_input() -> str:
        return input("> ")

    def add_system_instruction(self, system_instruction: str):
        new_message = {"role": "system", "content": system_instruction}
        self._message_history.append(new_message)

    def solicit_system_instruction(self) -> str:
        print("What kind of bot would you like to chat with?")
        system_instruction = self.collect_input()
        if system_instruction:
            print("Sure, no problem.\n")
            self.add_system_instruction(system_instruction)
        else:
            print("Okay, we'll just fly by the seat of our pants.")

    @staticmethod
    def _display_message_content(message: dict[str, str]):
        display_role = {
            "user": "You",
            "assistant": "My Cool AI",
            "system": "The System",
        }[message["role"]]
        message_content = message["content"].strip()
        #print(f"[{display_role}] {message_content}")
        print(message_content)

    def send_message(self, user_message_content: str):
        user_message = {"role": "user", "content": user_message_content}
        self._message_history.append(user_message)
        response = openai.ChatCompletion.create(
            model=self._MODEL,
            messages=self._message_history,
        )
        assistant_message = response.choices[0]["message"]
        self._message_history.append(assistant_message)
        self._display_message_content(assistant_message)
    
    def loop(self) -> None:
        user_input = self.collect_input()
        if not user_input:
            return
        self.send_message(user_input)
        self.loop()


def main() -> None:
    _authenticate()
    chat_session = ChatSession()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    chat_session.add_system_instruction(f"You are ChatGPT, a large language model trained by OpenAI. Answer as concisely as possible.\nCurrent date: {today}")
    chat_session.loop()


if __name__ == "__main__":
    main()
