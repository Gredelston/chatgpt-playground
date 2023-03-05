#!/usr/bin/env python3

import unittest
from unittest import mock

import openai

from lib import chatgpt
from lib import constants

SAMPLE_USER_MESSAGE = {"role": "user", "content": "Hello, ChatGPT!"}
SAMPLE_ASSISTANT_MESSAGE = {"role": "assistant", "content": "Hello, user!"}
SAMPLE_COMPLETION = {
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": SAMPLE_ASSISTANT_MESSAGE,
        },
    ],
    "created": 1678043786,
    "id": "chatcmpl-abcdefghijklmnop12345",
    "model": constants.CHATGPT_MODEL,
    "object": "chat.completion",
    "usage": {
        "completion_tokens": 35,
        "prompt_tokens": 8,
        "total_tokens": 43,
    },
}


class MockAPITestCase(unittest.TestCase):
    def setUp(self):
        """Mock out the ChatGPT API call."""
        self._api_mock = openai.ChatCompletion.create = mock.MagicMock(
            return_value=SAMPLE_COMPLETION
        )


class SendMessagesTest(MockAPITestCase):
    """Test case for chatgpt.send_messages()"""

    def testMessageExtraction(self):
        """Check that we extract the response message correctly."""
        response_message = chatgpt.send_messages([SAMPLE_USER_MESSAGE])
        self.assertEqual(response_message, SAMPLE_ASSISTANT_MESSAGE)


class SendMessageTest(MockAPITestCase):
    def testMessagesSent(self):
        """Check that the API is called with the single given message."""
        chatgpt.send_message(SAMPLE_USER_MESSAGE)
        self._api_mock.assert_called_with(
            model=constants.CHATGPT_MODEL, messages=[SAMPLE_USER_MESSAGE]
        )
