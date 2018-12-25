from sys import path
path.append("./../Database")
from Database import *
from Type import *

class Move:
    def __init__(self, name = None, db = None):
        self.data = db.accessMove(name)
        if name and self.data:
            self.name = self.data[0]
            self.kind = self.data[1]
            self.type = self.data[2]
            self.power = int(self.data[3])
            self.accuracy = int(self.data[4])
            self.pp = int(self.data[5])
            self.range = self.data[6]
        elif not self.data:
            print('Invalid Move!')
    
    def setMove(self, name = None):
        self.data = db.accessMove(name)
        if name and self.data:
            self.name = self.data[0]
            self.kind = self.data[1]
            self.type = self.data[2]
            self.power = int(self.data[3])
            self.accuracy = int(self.data[4])
            self.pp = int(self.data[5])
            self.range = self.data[6]
        elif not name:
            print('Empty Move Name!')
        elif not self.data:
            print('Invalid Move!')
