class Plt:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def getName(self):
        return self.name
    
    def getTime(self):
        return self.time
    
    def rdcTime(self, value):
        self.time -= value