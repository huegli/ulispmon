from __future__ import print_function
if hasattr(__builtins__, 'raw_input'):
    input = raw_input

import serial
import sys

with serial.Serial('/dev/ttyS1', 9600, timeout=0.5) as ser:
    ser.write(')\n')
    while (1):
        line = ser.readline()
        while (line != ''):
            sys.stdout.write(line)
            line = ser.readline()
        cmd = input('')
        if (cmd == '!q'):
            break
        ser.write(cmd)
        ser.write('\n')

