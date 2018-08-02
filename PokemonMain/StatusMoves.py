from Pokemon import *

class StatusMove: #for status variables, there are two options, convert the stat (as shown below) and make that value equal to current stats or take a changed value in the stat and subtract it or add it from the original value
    def __init__ (self, hp, atk, defn, state, accuracy, selfdef): #no damage but alters stats of pokemon
        self.hp = hp
        self.atk = atk
        self.defn = defn
        self.state = state
        self.accuracy = accuracy #accuracy = random(0, 0) if accuracy = 0, do the attack
        self.selfdef = selfdef #user defense
    #status moves
    def growl (self): 
        typemove = "normal" 
        counter = 0 #counters to indicate there is a limit to how many times it can be used before it has no effect
        if counter == 6:
            print ("attack cannot go lower")
        else:
            self.atk = int(self.atk - self.atk * 0.16) #lowers attack by 1/6
            counter = counter + 1
        return (self.atk)
    
    def tailwhip (self):
        typemove = "normal"
        counter = 0
        if counter == 6:
            print ("defense cannot go lower")
        else:
            self.defn = int(self.defn - self.defn * 0.16)
            counter = counter + 1
        return (self.defn)
    
    def withdraw (self):
        typemove = "water"
        counter = 0
        if counter == 6:
            print ("defense cannot go higher")
        else:
            self.selfdef = int(self.selfdef + self.selfdef * 0.16) #increases user's defense by 1/6
            counter = counter + 1
        return(self.selfdef)
    
    def poisonpowder (self): #changes the state of the opponent to poison
        typemove = "poison" #more details below
        if self.state != "poisoned":
            self.state = "poisoned"
        else:
            print ("target already poisoned")
        return (self.state)
    
    def smokescreen (self): #lowers accuracy
        typemove = ("normal")
        counter = 0
        if counter == 6:
            print ("accuracy cannot go lower")
        else:
            self.accuracy = int (self.accuracy + 1)
            counter = counter + 1
        return (self.accuracy)
