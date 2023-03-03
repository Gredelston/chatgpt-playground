#!/usr/bin/env python3

"""Library for a persistent chat session with history."""

from lib import auth
from lib import chatgpt
from lib import cli
from lib import constants
from lib import types


class ChatSession:
    """A single chat session which tracks message history."""

    def __init__(self, system_instruction: str = "", debug=False) -> None:
        """Initialize the session with an empty message history.

        Args:
            debug: If True, print out additional debug information.
            system_instruction: Additional instructions to give to ChatGPT as a
                prefix before user interactions.
        """
        self._debug = debug
        self._message_history: list[types.Message] = []
        auth.authenticate()
        if system_instruction:
            self._append_system_content(system_instruction)

    def _append_message_to_history(self, new_message: types.Message) -> None:
        """Add a message to the session history."""
        self._message_history.append(new_message)

    def _append_user_content(self, content: str) -> None:
        """Create a message from the user, and add it to the session history."""
        new_message = types.Message(role=constants.ROLE_USER, content=content)
        self._append_message_to_history(new_message)

    def _append_system_content(self, content: str) -> None:
        """Create a message from the system. Add it to the session history."""
        new_message = types.Message(role=constants.ROLE_SYSTEM, content=content)
        self._append_message_to_history(new_message)

    def _get_system_messages(self) -> list[types.Message]:
        """Return a list of system messages in the session history."""
        return [
            msg for msg in self._message_history if msg["role"] == constants.ROLE_SYSTEM
        ]

    def ask(self, content: str, with_history=True) -> None:
        """Send a user message to ChatGPT, and print the response.

        Args:
            content: What the user is asking.
            with_history: Whether to include the whole chat history in the
                request. If False, system instructions will still be sent, but
                not other message history; and the new request and response will
                not be retained.
        """
        user_message = types.Message(role=constants.ROLE_USER, content=content)
        if with_history:
            self._append_message_to_history(user_message)
            response_message = chatgpt.send_messages(
                self._message_history, debug=self._debug
            )
            self._append_message_to_history(response_message)
        else:
            response_message = chatgpt.send_messages(
                self._get_system_messages() + [user_message], debug=self._debug
            )
        cli.print_message(response_message)

    def interact(self) -> bool:
        """Prompt the user for input and print ChatGPT's response.

        Returns:
            True if the user entered any input; otherwise, False.
        """
        user_input = cli.prompt_user()
        if not user_input:
            return False
        self.ask(user_input, with_history=True)
        return True

    def loop(self) -> None:
        """Continually interact until the user stops."""
        if self.interact():
            self.loop()
