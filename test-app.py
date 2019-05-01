#!/usr/bin/env python

from prompt_toolkit import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import HSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings

buffer2 = Buffer(read_only=False)  # Read-only buffer
buffer2.insert_text('Hello World\n')

def enter_cmd(cmd):
    buffer2.insert_text(cmd.document.text)
    buffer2.insert_text('\n')
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

app = Application(key_bindings=kb, layout=layout, full_screen=True)
app.run() # You won't be able to Exit this app
