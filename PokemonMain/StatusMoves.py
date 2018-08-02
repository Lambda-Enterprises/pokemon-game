from Pokemon import *

class StatusMove: #for status variables, there are two options, convert the stat (as shown below) and make that value equal to current stats or take a changed value in the stat and subtract it or add it from the original value
    def __init__ (self, lvl, hp, atk, defn, state, accuracy, selfdef): #no damage but alters stats of pokemon
        self.lvl = lvl
        self.hp = hp
        self.atk = atk
        self.defn = defn
        self.state = state
        self.accuracy = accuracy #accuracy = random(0, 0) if accuracy = 0, do the attack
        self.selfdef = selfdef #user defense
