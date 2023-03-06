#!/usr/bin/env python3

"""Test the filesystem interactions."""

import os
import tempfile
import unittest

from lib import fs


class ReadFileTestCase(unittest.TestCase):
    """Test cases for read_file()."""

    def test_with_tilde(self):
        """Test that we can read a file containing ~."""
        # Arrange
        home = os.path.expanduser("~")
        file = tempfile.NamedTemporaryFile(dir=home)
        file.write(
            b"""line1
line2
"""
        )
        file.seek(0)

        # Act
        basename = os.path.basename(file.name)
        contents = fs.read_file(f"~/{basename}")

        # Assert
        self.assertEqual(contents, "line1\nline2")
