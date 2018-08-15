from Database import *
from Pokemon import *
from Type import *

class Move:
    def __init__(self, name = None):
        try:
            with open('Data/Move.json', 'r') as file:
                moveDict = json.loads(file.read())
                file.close()
            move = moveDict[name]
            self.name = name
            self.type = move['type']
            self.power = move['power']
            self.accuracy = move['accuracy']
        except:
            print('Invalid Move!')
    
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
    
    def setMove(self, name):
        with open('Data/Move.json', 'r') as file:
            moveDict = json.loads(file.read())
            file.close()
        move = moveDict[name]
        self.name = name
        self.type = move['type']
        self.power = move['power']
        self.accuracy = move['accuracy']
