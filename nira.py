#!/usr/bin/env python3

import argparse
import datetime
import sys
from typing import Any, Optional

import openai

from lib import session


def main(debug: bool = False) -> None:
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    system_instruction = (
        "You are Nira, my personal robotic assistant. "
        + "Answer as concisely as possible.\n"
        + f"Current date: {today}"
    )
    chat_session = session.ChatSession(
        system_instruction=system_instruction, debug=debug
    )
    chat_session.loop()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true")
    opts = parser.parse_args(sys.argv[1:])
    main(debug=opts.debug)
