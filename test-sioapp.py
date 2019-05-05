#!/usr/bin/env python

from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.eventloop import use_asyncio_event_loop
from asyncio import gather, get_event_loop, sleep

import serial

ser = serial.Serial('/dev/ttyACM1')

buffer2 = Buffer(read_only=False)  # Read-only buffer

def enter_cmd(cmd):
    ser.write(cmd.document.text.encode())
    # buffer2.insert_text(cmd.document.text)
    return False

buffer1 = Buffer(multiline=False, accept_handler=enter_cmd)  # Editable buffer.

root_container = HSplit([
    # Display the text 'Hello world' on the right.
    Window(height=1, content=BufferControl(buffer=buffer1)),

    # A vertical line in the middle. We explicitly specify the width, to
    # make sure that the layout engine will not try to divide the whole
    # width by three for all these windows. The window will simply fill its
    # content by repeating this character.
    Window(height=1, char='-'),

    # One window that holds the BufferControl with the default buffer on
    # the left.
    Window(content=BufferControl(buffer=buffer2)),


])

layout = Layout(root_container)

kb = KeyBindings()

@kb.add('c-q')
def exit_(event):
    """
    Pressing Ctrl-Q will exit the user interface.

    Setting a return value means: quit the event loop that drives the user
    interface and return this value from the `Application.run()` call.
    """
    event.app.exit()

async def print_hello():
    for _ in range(100):
        buffer2.insert_text('Hello World\n')
        await sleep(0.5)


async def print_serial():
    while True:
        if (ser.inWaiting() > 0):
            ch_str = ser.read().decode()
            if (ch_str != '\r'):
                buffer2.insert_text(ch_str)
        else:
            await sleep(0.5)

app = Application(key_bindings=kb, layout=layout, full_screen=True)
use_asyncio_event_loop()
get_event_loop().run_until_complete(gather(
    app.run_async().to_asyncio_future(),
    print_serial()))
