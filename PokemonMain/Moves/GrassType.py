from Move import *

class GrassType("Move"):
    def __init__(self, name, type, power, accuracy):
           super(name, type, power, accuracy)
    
    def vinewhip (self):
        typemove = "grass"
        power = 45
        crit = 1
        stab = 1
        x = int(random(1, 30))
        if x == 1:
            crit = 2
        if typemove == self.typepkmn:
            stab = 1.5
        mod1 = crit * 0.85 * stab
        mod2 = crit * 1.00 * stab
        rng1 = ((((2 * self.lvl)/5 + 2) * power * (self.atk/self.defn))/50 + 2) * mod1
        rng2 = ((((2 * self.lvl)/5 + 2) * power * (self.atk/self.defn))/50 + 2) * mod2
        self.dmg = int(random(rng1, rng2))
        if self.typeopp == "water": #some attack types are super effective against certain types
             self.dmg = self.dmg * 2 #super effective = 2 times the damage
        if self.typeopp == "fire" or self.typeopp == "grass":
            self.dmg = self.dmg * 0.5 #non effective = 0.5 times the damage
        return (self.dmg)
    