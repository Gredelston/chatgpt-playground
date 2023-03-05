#!/usr/bin/env python3

import datetime

from lib import session
from lib import tkui

if __name__ == "__main__":
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    system_instruction = (
        "You are Nira, my personal robotic assistant. "
        + "Answer as concisely as possible.\n"
        + f"Current date: {today}"
    )
    chat_session = session.ChatSession(system_instruction=system_instruction)
    chat_session.register_command("clear", chat_session.clear_history_except_system)
    tkui.UI(chat_session).run()
