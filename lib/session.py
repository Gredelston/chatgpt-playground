#!/usr/bin/env python3

"""Library for a persistent chat session with history."""

from lib import auth
from lib import chatgpt
from lib import cli
from lib import constants
from lib import types


class ChatSession:
    """A single chat session which tracks message history."""

    def __init__(self, system_instruction: str = "") -> None:
        """Initialize the session with an empty message history."""
        self._message_history: list[types.Message] = []
        auth.authenticate()
        if system_instruction:
            self._append_system_message(system_instruction)

    def _append_message_to_history(self, new_message: types.Message) -> None:
        """Add a message to the session history."""
        self._message_history.append(new_message)

    def _append_user_message(self, content: str) -> None:
        """Create a message from the user, and add it to the session history."""
        new_message = types.Message(role=constants.ROLE_USER, content=content)
        self._append_message_to_history(new_message)

    def _append_system_message(self, content: str) -> None:
        """Create a message from the system. Add it to the session history."""
        new_message = types.Message(role=constants.ROLE_SYSTEM, content=content)
        self._append_message_to_history(new_message)

    def interact(self) -> bool:
        """Prompt the user for input and print ChatGPT's response.

        Returns:
            True if the user entered any input; otherwise, False.
        """
        user_input = cli.prompt_user()
        if not user_input:
            return False
        self._append_user_message(user_input)
        response_message = chatgpt.send_messages(self._message_history)
        cli.print_message(response_message)
        return True

    def loop(self):
        """Continually interact until the user stops."""
        if self.interact():
            self.loop()
