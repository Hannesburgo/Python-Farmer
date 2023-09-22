from Item import *

class Plt(Item):
    def __init__(self, name, time, value):
        super(Plt, self).__init__(name, "Plant", value)
        self.time = time
    
    def grow(self, value):
        self.time -= value