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

	x = 200
	y = 10
	#TESTCODE
	while True:	
		self.world.updatePos(x,y,1)
		x = x + random.randrange(-1,2)
		y = y + random.randrange(0,2)
		self.world.updatePos(x,y,0)
		time.sleep(0.01)
	#TESTCODE

        #self.world.print_message(self.message)


if __name__ == '__main__':

    proto = EventHandler()
    proto.run(Port(packet=1, use_stdio=True))

    #aw = AntWorld(message)
