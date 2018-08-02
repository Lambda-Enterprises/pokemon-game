from Pokemon import *
from Type import *

class Move:
   def __init__ (self, name = '', type = Type(), power = 0, accuracy = 0):
       self.name = name
       self.type = type
       self.power = power
       self.accuracy = accuracy
    
    def loadMove(self, name):
        moveDict = {
            
        }
        
        return(typedict[name])
    
