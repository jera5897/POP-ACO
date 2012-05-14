import sys
from erlport import Port, Protocol
from erlport import Atom, String

import gui,time,random

class EventHandler(Protocol):
    
    def __init__(self):
        pass

    def handle(self, port, message):
        self.port = port
        text = "%s" % String(message)
        aw = AntWorld(text, self)

    def to_erl(self, message):
        self.port.write(message)
        

class AntWorld:

    def __init__(self, message, handler=None):
        self.message = message
        self.handler = handler
        self.world = gui.Gui(self, self.message, self.handler)
	self.world.start()

	#TESTCODE
	while True:	
		self.world.updatePos(random.randrange(0,400), random.randrange(0,400),0)
		time.sleep(0.1)
	#TESTCODE

        #self.world.print_message(self.message)


if __name__ == '__main__':

    proto = EventHandler()
    proto.run(Port(packet=1, use_stdio=True))

    #aw = AntWorld(message)
