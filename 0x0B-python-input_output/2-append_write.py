#!/usr/bin/python3
"""append_write module"""


def append_write(filename="", text=""):
    """append_write - appends a string at the end of a text file (UTF8),
        and returns the number of characters added"""
        with open(filename, mode="a", encoding="UTF-8") as f:
            return (f.write(text))
