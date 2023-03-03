#!/usr/bin/env python3

"""An audio/speech interface to ChatGPT."""

import argparse
import datetime
import sys
from typing import Any, Optional

import openai

from lib import record
from lib import session


def main(debug: bool = False) -> None:
    """Listen for audio input an interactive chat session with Nira, my assistant."""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    system_instruction = (
        "You are Chatterbox, my personal robotic assistant. "
        + "Answer as concisely as possible.\n"
        + f"Current date: {today}"
    )
    chat_session = session.ChatSession(
        system_instruction=system_instruction, debug=debug
    )

    recorder = record.Recorder()
    audio_filepath = recorder.record_n_seconds(5)
    with open(audio_filepath, "rb") as file:
        transcription = openai.Audio.transcribe("whisper-1", file)
    print(transcription)


if __name__ == "__main__":
    main()
