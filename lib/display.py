#!/usr/bin/env python3

from . import types


def print_message(message: types.Message):
    print("\n%s\n" % message["content"].strip())
