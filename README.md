Arduino Leonardo is one of Arduino family, which can emulate keyboard and mouse, some of my friends asked me to write an interpreter for the Arduino which can turn a ducky like script into C code. This post is going to be how to use that Leo interpreter

### How to Run It?

Its pretty simple just clone the repo and copy the leo.py to desire location, then

python leo.py payload.txt -o payload.c
This will convert the Leo script into C code

### What is Ducky Script

Ducky Script is the language of the USB Rubber Ducky. Writing scripts for can be done from any common ascii text editor such as Notepad, vi, emacs, nano, gedit, kedit, TextEdit, etc.

### What is Leo Script

Leo is a ducky like script, it very simple and easy to understand. I said ducky like script because actually, you can not use a ducky script with Leo, some syntax might look similar to ducky script but its not

### Syntax

Leo script is simple. Each command resides on a new line and may have options follow. Commands are written in ALL CAPS, Below is a list of commands and their function, followed by some example usage.

### REM

Similar to the REM command in Basic and other languages, lines beginning with REM will not be processed. REM is a comment.

REM The next three lines execute a command prompt in Windows
GUI r
STRING cmd
ENTER

### DELAY

DELAY creates a momentary pause in the Leo script. It is quite handy for creating a moment of pause between sequential commands that may take the target computer sometime to process. DELAY time is specified in milliseconds from 1 to 10000. Multiple DELAY commands can be used to create longer delays.

DELAY 500
REM will wait 500ms before continuing to the next command.

### STRING

STRING processes the text following taking special care to auto-shift. STRING can accept a single or multiple characters.

GUI r
DELAY 500
STRING notepad.exe
ENTER
DELAY 1000
STRING Hello World!

### GUI

Emulates the Windows-Key, sometimes referred to as the Super-key.

GUI r
REM will hold the Windows-key and press r, on windows systems resulting in the Run menu.

### SHIFT

Unlike CAPSLOCK, cruise control for cool, the SHIFT command can be used when navigating fields to select text, among other functions.

SHIFT TAB
REM this is paste for most operating systems
Check out python leo.py keylist to see all available argument keys

### ALT 

Found to the left of the space key on most keyboards, the ALT key is instrumental in many automation operations. ALT is envious of CONTROL

GUI r
DELAY 50
STRING notepad.exe
ENTER
DELAY 100
STRING Hello World
ALT f
STRING s

### CTRL 

The king of key-combos, CONTROL is all mighty.

CTRL ESC
REM this is equivalent to the GUI key in Windows

### Arrow Keys

- UP
- DOWN
- LEFT
- RIGHT

### PRESS

PRESS allow you to perform multiple keypresses

PRESS ALT F4
ENTER

### REPEAT

Repeat is the one important command that differs from ducky script, sucky script repeats the last command to given iteration count, but in Leo the command follows with a colon

DELAY 100
REPEAT 6: ENTER