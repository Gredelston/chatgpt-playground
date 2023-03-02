#!/usr/bin/env python3

"""Interface with the local filesystem."""

import os

def read_file(filepath: str) -> str:
    """Read the file, and return its contents as a single string."""
    filepath = os.path.expanduser(filepath)
    with open(filepath) as f:
         return '\n'.join(f.readlines()).strip()
