#!/usr/bin/python3
"""This module defines a text reading file function"""


def read_file(filename=""):
   """ prints the contents of UTF8 text files"""
   with open(filename, encoding="utf-8") as f:      print(f.read(), end="")
