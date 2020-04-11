#!/usr/bin/env python3
# coding=utf-8

"""
Copyright (c) 2019 suyambu developers (http://suyambu.net/leo)
See the file 'LICENSE' for copying permission
"""


class Error:
    def __init__(self, name, message):
        self.name = name
        self.message = message

    def __repr__(self):
        return "{}: {}".format(self.name, self.message)


class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__("IllegalCharError", details)

