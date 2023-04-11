#!/usr/bin/python3
"""This module inherits from the list class"""

class Mylist(list):
    """This is a class that inherits from list"""
        def print_sorted(self):
            """prints a sorted list"""
            print(sorted(self))
