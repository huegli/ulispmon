#!/usr/bin/env python

from __future__ import unicode_literals
from prompt_toolkit import prompt

from blessings import Terminal
import time

term = Terminal()

cmd = ''
while (cmd != 'bye'):
    print('Hello World')
    with term.location(0, 10):
        cmd = prompt('>>> ')
    with term.location(0, 20):
        print('You entered: %s' % cmd)

# for i in range(100):
#     print("Hello World ", i)
#     with term.location(0, 0):
#         print("This is ", term.bold("a test"))
#     time.sleep(1)
