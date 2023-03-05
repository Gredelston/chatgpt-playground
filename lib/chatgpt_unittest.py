#!/usr/bin/env python3

import unittest
from unittest import mock

import openai

from lib import chatgpt
from lib import constants

SAMPLE_COMPLETION = {
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "Hi, it's me, ChatGPT",
                "role": "assistant",
            },
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

class SendMessagesTest(unittest.TestCase):
    def setUp(self):
        openai.ChatCompletion.create = mock.MagicMock(return_value=SAMPLE_COMPLETION)

    def testMessageExtraction(self):
        """Check that we extract the response message correctly."""
        input_messages = [{"role": "user", "content": "Hello, ChatGPT!"}]
        response_message = chatgpt.send_messages(input_messages)
        self.assertEqual(response_message["role"], "assistant")
        self.assertEqual(response_message["content"], "Hi, it's me, ChatGPT")
