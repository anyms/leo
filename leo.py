#!/usr/bin/env python3
# coding=utf-8

"""
Copyright (c) 2019 suyambu developers (http://suyambu.net/leo)
See the file 'LICENSE' for copying permission
"""

import sys

from core.lexer import Lexer
from core.evaluator import Evaluator
from utils.argparse import ArgParse


class Leo:
    def __init__(self):
        self.parser = ArgParse(20, "leo.py source.leo -o out.ino")
        self.parser.add_argument(["-help", "-h"], "show help")
        self.parser.add_argument(["-o"], "output file")
        self.args = self.parser.parse()

    def run(self):
        if self.args.help:
            self.parser.print_help()

        f = open(sys.argv[1], "rt")
        source = f.read()
        f.close()

        lexer = Lexer(source)
        evaluator = Evaluator(lexer.tokens, lexer.keys_map)

        f = open(self.args.o, "w+")
        f.write(evaluator.run())
        f.close()


if __name__ == "__main__":
    Leo().run()
