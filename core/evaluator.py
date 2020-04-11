class Evaluator:
    def __init__(self, tokens, keys_map):
        self.tokens = tokens
        self.keys_map = keys_map
        self.i = 0
        self.variables = {}

    def run(self):
        output = """#include "Keyboard.h"
void typeKey(int key) {Keyboard.press(key);delay(50);Keyboard.release(key);}void combo(int key, char letter) {Keyboard.press(key);Keyboard.press(letter);Keyboard.releaseAll();}void setup() {Keyboard.begin();"""
        for token in self.tokens:
            if token.label == "echo":
                for k in token.value:
                    if k.startswith("$"):
                        output += "Keyboard.print({});".format(self.variables[k])
                    elif k.startswith('"'):
                        output += "Keyboard.print({});".format(k)
            elif token.label == "string_variable":
                output += """char* sv{}={};""".format(self.i, token.value)
                self.variables[token.identifier] = "sv{}".format(self.i)
            elif token.label == "number_variable":
                output += """int iv{}={};""".format(self.i, token.value)
                self.variables[token.identifier] = "iv{}".format(self.i)
            elif token.label == "sleep":
                if token.value.startswith("$"):
                    output += "delay({});".format(self.variables[token.value])
                else:
                    output += "delay({});".format(token.value)
            elif token.label == "keys":
                for k in token.value:
                    if k in self.keys_map:
                        output += "Keyboard.press({});delay(50);".format(self.keys_map[k])
                    elif k.find('"') > -1:
                        output += "Keyboard.print({});delay(50);".format(k)
                    elif k.startswith("$"):
                        output += "Keyboard.print({});delay(50);".format(self.variables[k])

                output += "Keyboard.releaseAll();"

            self.i += 1

        output += """Keyboard.end();}void loop() {}"""
        return output