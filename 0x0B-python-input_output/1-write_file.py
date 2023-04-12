#!/usr/bin/python3
"""This module defines a function that writes a string to a UTF8 textfiles"""


def write_file(filename="", text=""):
    """writes a string to a UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
