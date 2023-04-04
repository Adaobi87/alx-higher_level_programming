#!/usr/bin/python3
class LockedClass:
    """ only allows instance attribute called first_name"""
    __slots__ = ["first_name"]
