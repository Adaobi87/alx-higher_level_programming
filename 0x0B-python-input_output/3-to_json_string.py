#!/usr/bin/python3
"""This module defines a function that returnsJSON representation of a string"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of a string object"""
    json.dumps(my_obj)
