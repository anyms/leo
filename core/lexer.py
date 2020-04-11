#!/usr/bin/env python3
# coding=utf-8

"""
Copyright (c) 2019 suyambu developers (http://suyambu.net/leo)
See the file 'LICENSE' for copying permission
"""

from core.error import IllegalCharError
from data.token import Token


class Lexer:
    def __init__(self, text):
        lines = text.split("\n")
        self.tokens = []

        self.two_worders = ["sleep"]
        self.keys_map = {
            "ctrl": "KEY_LEFT_CTRL",
            "lctrl": "KEY_LEFT_CTRL",
            "shift": "KEY_LEFT_SHIFT",
            "lshift": "KEY_LEFT_SHIFT",
            "alt": "KEY_LEFT_ALT",
            "lalt": "KEY_LEFT_ALT",
            "gui": "KEY_LEFT_GUI",
            "lgui": "KEY_LEFT_GUI",
            "rctrl": "KEY_RIGHT_CTRL",
            "rshift": "KEY_RIGHT_SHIFT",
            "ralt": "KEY_RIGHT_ALT",
            "rgui": "KEY_RIGHT_GUI",
            "up_arrow": "KEY_UP_ARROW",
            "down_arrow": "KEY_DOWN_ARROW",
            "left_arrow": "KEY_LEFT_ARROW",
            "right_arrow": "KEY_RIGHT_ARROW",
            "backspace": "KEY_BACKSPACE",
            "tab": "KEY_TAB",
            "enter": "KEY_RETURN",
            "esc": "KEY_ESC",
            "insert": "KEY_INSERT",
            "delete": "KEY_DELETE",
            "page_up": "KEY_PAGE_UP",
            "page_down": "KEY_PAGE_DOWN",
            "home": "KEY_HOME",
            "end": "KEY_END",
            "caps_lock": "KEY_CAPS_LOCK",
            "f1": "KEY_F1",
            "f2": "KEY_F2",
            "f3": "KEY_F3",
            "f4": "KEY_F4",
            "f5": "KEY_F5",
            "f6": "KEY_F6",
            "f7": "KEY_F7",
            "f8": "KEY_F8",
            "f9": "KEY_F9",
            "f10": "KEY_F10",
            "f11": "KEY_F11",
            "f12": "KEY_F12",
        }

        for line in lines:
            if line.strip() == "" or line.strip().startswith("#"):
                continue
            token = self.tokenize(line)
            if token is not None:
                self.tokens.append(token)

    def get_nodes(self, line):
        nodes = []
        tmp = ""
        is_string = False
        is_string_found = False
        for c in line:
            if c == '"' and not is_string_found:
                is_string = True
                is_string_found = True
            elif c == '"' and is_string_found:
                if tmp[-1] != "\\":
                    is_string = False
                    is_string_found = False
                    tmp += '"'
                    nodes.append(tmp)
                    tmp = ""
                    continue

            if is_string_found:
                tmp += c
            elif c != " ":
                tmp += c
            elif c == " ":
                nodes.append(tmp)
                tmp = ""
        if tmp:
            nodes.append(tmp)
        return nodes

    def tokenize(self, line):
        nodes = self.get_nodes(line.strip())
        if nodes[-1].strip().endswith(":"):
            l = nodes.pop(0)
            return Token(
                is_block=True,
                label=l,
                value=" ".join(nodes).strip(),
                block=[],
                identifier=l
            )
        elif line.startswith("    "):
            if not self.tokens or not self.tokens[-1].is_block:
                raise SyntaxError('spaces out side of code block.')
            self.tokens[-1].block.append(self.tokenize(line.strip()))
            return None
        elif nodes[0] == "echo":
            l = nodes.pop(0)
            return Token(
                is_block=False,
                label=l,
                value=nodes,
                block=[],
                identifier=l
            )
        elif nodes[0] in self.two_worders:
            l = nodes.pop(0)
            return Token(
                is_block=False,
                label=l,
                value=" ".join(nodes).strip(),
                block=[],
                identifier=l
            )
        elif nodes[0] in self.keys_map:
            return Token(
                is_block=False,
                label="keys",
                value=nodes,
                block=[],
                identifier="keys"
            )
        elif nodes[0].startswith("$"):
            nodes = line.split(" ")
            identifier = nodes.pop(0)
            val = " ".join(nodes).strip()
            if '"' in val:
                t = "string"
            else:
                t = "number"
            return Token(
                is_block=False,
                label="{}_variable".format(t),
                value=val,
                block=[],
                identifier=identifier
            )
        return None
