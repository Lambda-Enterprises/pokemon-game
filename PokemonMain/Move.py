from Pokemon import *
from Type import *

class Move:
    def __init__ (self, name = '', type = Type(), power = 0, accuracy = 0):
       self.name = name
       self.type = type
       self.power = power
       self.accuracy = accuracy
    
    def calcDamage(self, atk, defn, opptype):
        mod = 1 #factor that indicates more damage
        for opptype in self.type.superEffective:
            mod = mod * 2
        for opptype in self.type.notEffective:
            mod = mod / 2
        for opptype in self.type.noEffect:
            mod = mod * 0
        dmg = ((((2 * 50)/5 + 2) * self.power * (atk/defn))/50 + 2) * mod
        
        return (dmg)
    
    @staticmethod
    def loadMove(name):
        moveDict = {
            'tackle' : Move('tackle', type.loadType('normal'), 40, 100),
            'scratch' : Move('scratch', type.loadType('normal'), 35, 100),
            'vinewhip' : Move('vine whip', type.loadType('grass'), 45, 100),
            'ember' : Move('ember', type.loadType('fire'), 40, 100),
            'bubble' : Move('bubble', type.loadType('water'), 40, 100)
        }
        
        return(moveDict[name])
    
