#!/usr/bin/python3
"""This program defines a LockedClass"""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first__name"]
