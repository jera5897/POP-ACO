import random, sys, time
from Tkinter import *

import antworld

class Gui:

    def __init__(self, world=None, message=None, handler=None, parent=None):
        self.canvas = Canvas(width=400, height=400, bg='green')
        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas.bind('<ButtonPress-1>', self.onClick)

        self.aw = world
        self.handler = handler
        self.print_message(message)

        mainloop()

    def onClick(self, event):
        #self.print_message(self.handler)
        #self.print_message('test')
        #self.canvas.move('message', random.randrange(-20,20), random.randrange(-20,20))
        self.handler.to_erl('Hej Erlang!')
        #for i in range (0,10):
        #    self.print_message('test')
        #time.sleep(1))

    def print_message(self, message):
        x = random.randrange(50, 350)
        y = random.randrange(50, 350)
        self.canvas.create_text(x, y, text=message, tag='message')

    def clear(self):
        self.canvas.delete('all')


if __name__ == '__main__':

    message = 'Hello World!'

    gui = Gui(message)