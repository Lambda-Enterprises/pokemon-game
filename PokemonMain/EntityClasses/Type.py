from sys import path
path.append("./../Database")
from Database import *

class Type:
    def __init__(self, name = None, db = None):
        self.data = db.accessType(name)
        if name and self.data:
            self.name = self.data[0]
            self.superEffective = self.data[1]
            self.notEffective = self.data[2]
            self.noEffect = self.data[3]
        elif not self.data:
            print('Invalid Type!')
    
    def setType(self, name):
        self.data = db.accessType(name)
        if name and self.data:
            self.name = self.data[0]
            self.superEffective = self.data[1]
            self.notEffective = self.data[2]
            self.noEffect = self.data[3]
        elif not name:
            print('Invalid Type!')
        elif not self.data:
            print('Empty Type Name!')
	
    def getAttributes():
        return [self.name, self.superEffective, self.notEffective, self.noEffect]