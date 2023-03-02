#!/usr/bin/env python3

import datetime
from typing import Any, Optional

import openai

from lib import session


def main() -> None:
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    system_instruction = (
        "You are Nira, my personal robotic assistant. "
        + "Answer as concisely as possible.\n"
        + f"Current date: {today}"
    )
    chat_session = session.ChatSession(system_instruction=system_instruction)
    chat_session.loop()


if __name__ == "__main__":
    main()
