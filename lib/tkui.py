#!/usr/bin/env python3

import tkinter
from tkinter import scrolledtext
from tkinter import ttk

from lib import session

class UI:
    def __init__(self, chat_session: session.ChatSession, **kwargs) -> None:
        self._chat_session = chat_session

        self._root = tkinter.Tk()
        self._frame = ttk.Frame(self._root, padding=10)
        self._frame.grid()

        ttk.Label(self._frame, text="Hello World!").grid(column=0, row=0)
        self.input_frame = scrolledtext.ScrolledText(self._frame)
        self.input_frame.grid(column=0, row=1)
        ttk.Button(self._frame, text="SendMessage", command=self.send_message).grid(column=0, row=2)
        ttk.Button(self._frame, text="Quit", command=self._root.destroy).grid(column=0, row=3)

    def run(self):
        self._root.mainloop()

    def send_message(self):
        input_content = self.input_frame.get("1.0", "end-1c")
        self._chat_session.ask(input_content)
