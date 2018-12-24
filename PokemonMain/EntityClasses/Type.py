from sys import path
path.append("./../Database")
from Database import *

class Type:
    def __init__(self, name = None, cur = None):
        (self.name, self.superEffective, self.notEffective, 
         self.noEffect) = tuple()
    
    def setType(self, name):
        
        try:
            
            self.name = cur[0]
            self.superEffective = cur[1]
            self.notEffective = cur[2]
            self.noEffect = cur[3]
        except DatabaseError:
            print('Could not AccessDatabase')
        except:
            print('Invalid Type!')
	
    def getAttributes():
        return [self.name, self.superEffective, self.notEffective, self.noEffect]
