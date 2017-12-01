import cmd
import optparse
import sys
import os
import re

if sys.argv[1] == "keylist":
        keys   = """
LEFT_CTRL     0x80    128
LEFT_SHIFT    0x81    129
LEFT_ALT      0x82    130
LEFT_GUI      0x83    131
RIGHT_CTRL    0x84    132
RIGHT_SHIFT   0x85    133
RIGHT_ALT     0x86    134
RIGHT_GUI     0x87    135
UP_ARROW      0xDA    218
DOWN_ARROW    0xD9    217
LEFT_ARROW    0xD8    216
RIGHT_ARROW   0xD7    215
BACKSPACE     0xB2    178
TAB           0xB3    179
RETURN        0xB0    176
ESC           0xB1    177
INSERT        0xD1    209
DELETE        0xD4    212
PAGE_UP       0xD3    211
PAGE_DOWN     0xD6    214
HOME          0xD2    210
END           0xD5    213
CAPS_LOCK     0xC1    193
F1            0xC2    194
F2            0xC3    195
F3            0xC4    196
F4            0xC5    197
F5            0xC6    198
F6            0xC7    199
F7            0xC8    200
F8            0xC9    201
F9            0xCA    202
F10           0xCB    203
F11           0xCC    204
F12           0xCD    205
"""
        print(keys)
        exit(0)

input = open(sys.argv[1], 'rt')


class Leo(cmd.Cmd):    
    use_rawinput = False
    prompt = ''

    variables = {}
    default_delay = 100
    parser = optparse.OptionParser("usage%prog "+
            "<input_file> -o <output_file>")
    parser.add_option('-o', dest='out', type='string',
            help='specify output file')
    (options, args) = parser.parse_args()
    if options.out == None:
        print parser.usage
        exit(0)
    else:
        out = options.out

    def do_BEGIN(self, line):
        print("[+] Starting...")
        try:
            os.remove(self.out)
        except WindowsError: pass

        self.f = open(self.out, "a+")
        self.f.write("""#include "Keyboard.h"

/*******************
Copyright:  https://tamilwired.com
Date:       27/11/2017
Author:     Jeeva
URL:        https://github.com/anyms/leo
********************/

void typeKey(int key) {Keyboard.press(key);delay(50);Keyboard.release(key);}void combo(int key, char letter) {Keyboard.press(key);Keyboard.press(letter);Keyboard.releaseAll();}void setup() {Keyboard.begin();""")

    def do_REM(self, line):
        """just a comment"""


    def do_DELAY(self, line):
        """sleep for spefied time (ms)"""
        line = self.replace_vars(line)
        print("[+] Adding delay '{}ms'".format(line))
        self.f.write("""delay({});""".format(line))


    def do_GUI(self, line):
        """press left GUI key in Windows its windows key"""
        line = self.replace_vars(line)
        print("[+] Adding GUI + {}".format(line))
        self.f.write("""combo(KEY_LEFT_GUI, '{}');""".format(line))


    def replace_vars(self, string):
        try:
            m = re.search(r'{{(.*?)}}', string)
        except TypeError:
            return string

        count = 0
        while True:
            try:
                key = str(m.group(count)).replace("{", "").replace("}", "")
            except IndexError: break
            except AttributeError: break
            try:
                string = re.sub(r'{{(.*?)}}', self.variables[key], string, 1)
            except KeyError: break
            count += 1
        return string


    def emptyline(self):
        pass


    def do_STRING(self, line):
        """type the given string"""
        line = line.replace('"', '\\"')
        print("[+] Adding STRING '{}'".format(line))

        if line.find("{{_i}}") > -1:
            line = line.replace('{{_i}}', '%d')
            line = self.replace_vars(line)
            self.f.write("""char buf[30];sprintf(buf, "{}", _i);""".format(line))
            self.f.write("""Keyboard.print(buf);""")
        elif line.find("{{") > -1:
            line = self.replace_vars(line)
            line = line.replace("{{", "").replace("}}", "")
            self.f.write("""Keyboard.print({});""".format(line))
        else:
            line = self.replace_vars(line)
            self.f.write("""Keyboard.print("{}");""".format(line))


    def do_ENTER(self, line):
        print("[+] Adding ENTER key")
        self.f.write("""typeKey(KEY_RETURN);""")


    def do_SHIFT(self, line):
        line = self.replace_vars(line)
        print("[+] Adding SHIFT + {}".format(line))
        if line.isupper():
            line = "KEY_{}".format(line)
            self.f.write("""combo(KEY_RIGHT_SHIFT, {});""".format(line))
        else:
            self.f.write("""combo(KEY_RIGHT_SHIFT, '{}');""".format(line))


    def do_ALT(self, line):
        line = self.replace_vars(line)
        print("[+] Adding ALT + {}".format(line))
        if line.isupper():
            line = "KEY_{}".format(line)
            self.f.write("""combo(KEY_RIGHT_ALT, {});""".format(line))
        else:
            self.f.write("""combo(KEY_RIGHT_ALT, '{}');""".format(line))


    def do_CTRL(self, line):
        line = self.replace_vars(line)
        print("[+] Adding CTRL + {}".format(line))
        if line.isupper():
            line = "KEY_{}".format(line)
            self.f.write("""combo(KEY_RIGHT_CTRL, {});""".format(line))
        else:
            self.f.write("""combo(KEY_RIGHT_CTRL, '{}');""".format(line))

    def do_DOWN(self, line):
        print("[+] Adding DOWN")
        self.f.write("""typeKey(KEY_DOWN_ARROW);""")


    def do_LEFT(self, line):
        print("[+] Adding LEFT")
        self.f.write("""typeKey(KEY_LEFT_ARROW);""")


    def do_RIGHT(self, line):
        print("[+] Adding RIGHT")
        self.f.write("""typeKey(KEY_RIGHT_ARROW);""")


    def do_UP(self, line):
        print("[+] Adding UP")
        self.f.write("""typeKey(KEY_UP_ARROW);""")


    def do_PRESS(self, line):
        line = self.replace_vars(line)
        print("[+] Adding PRESS '{}'".format(line))

        keys = line.split(" ")
        for key in keys:
            if key.isupper():
                self.f.write("""Keyboard.press(KEY_{});""".format(key))
            else:
                self.f.write("""Keyboard.press('{}');""".format(key))

        self.f.write("""Keyboard.releaseAll();""")


    def do_DEFAULT_DELAY(self, line):
        line = self.replace_vars(line)
        self.default_delay = int(line)


    def loop_magic_var(self, line):
        if line.startswith("{{") and line.endswith("}}"):
            line = line.replace("{{_i}}", 'buf')
        elif line.startswith("{{"):
            line = line.replace("{{_i}}", 'buf + "')
            line = line + '"'
        elif line.endswith("}}"):
            line = line.replace("{{_i}}", '" + buf')
            line = '"' + line
        else:
            line = line.replace("{{_i}}", '" + buf + "')
            line = '"' + line + '"'

        return line


    def do_REPEAT(self, line, op="++"):
        line = self.replace_vars(line)

        data = line.split(":")
        iteration = data[0]

        if op == "++":
            query = """for (int _i = 0; _i < {}; _i{}) {{""".format(iteration, op)
        else:
            query = """for (int _i = {}; _i >= 0; _i{}) {{""".format(int(iteration) - 1, op)
        self.f.write(query)

        main_commands = data[1].strip().split(";")
        for mc in main_commands:
            print("==> " + mc)
            command = mc.strip().split(" ")
            method = command[0]
            command.pop(0)
            line = ""
            for cmd in command:
                line += "{} ".format(cmd)
            line = line.strip()

            getattr(self, "do_" + method)(line)
    
        self.do_DELAY(self.default_delay)            
        print("[+] REPEAT added for {} times".format(iteration))
        self.f.write("}")


    def do_REVERSE_REPEAT(self, line, op="--"):
        self.do_REPEAT(line, op)


    def do_VAR(self, line):
        data = line.split(" ")
        name = data[0]
        content = ""
        data.pop(0)
        for d in data:
            content += (d + " ")
        content = content.strip()    

        self.variables[name] = content


    def do_EOF(self, line):
        return True


    def default(self, line):
        print("SYNTAX ERROR: invalid syntax '{}'".format(line))
        self.f.close()
        try:
            os.remove(self.out)
        except WindowsError: pass
        return True


    def do_END(self, line):
        print("[+] Finishing...")
        self.f.write("""Keyboard.end();}void loop() {}""")
        self.f.close()


if __name__ == '__main__':
    try:
        Leo(stdin=input).cmdloop()
    finally:
        input.close()
