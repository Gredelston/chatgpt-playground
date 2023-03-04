#!/usr/bin/env python3

import tkinter
from tkinter import ttk

class UIProgram:
    def __init__(self):
        self._root = tkinter.Tk()
        self._frame = ttk.Frame(self._root, padding=10)
        self._frame.grid()
        ttk.Label(self._frame, text="Hello World!").grid(column=0, row=0)
        ttk.Button(self._frame, text="Quit", command=self._root.destroy).grid(column=1, row=0)

    def run(self):
        self._root.mainloop()
