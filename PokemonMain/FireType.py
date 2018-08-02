from Move import *, 

class FireType("Move"):
    def __init__(self, name, type, power, accuracy):
        super(name, type, power, accuracy)
    
    #special attacks
    def ember (self): #in previous methods, they were all physical attacks
        typemove = "fire" #in special attacks, attack stats are switched with special attacks and defense is switch with special defense
        power = 40
        crit = 1
        stab = 1
        wthr = 1
        x = int(random(1, 30))
        if x == 1:
            crit = 2
        if typemove == self.typepkmn:
            stab = 1.5
        if self.sky == "rain": #some attacks are also affected by the weather which can reduce or increase the damage
            wthr = 0.5
        elif self.sky == "sunny":
            whtr = 1.5
        else:
            whtr = 1
        mod1 = wthr * crit * 0.85 * stab
        mod2 = wthr * crit * 1.00 * stab
        rng1 = ((((2 * self.lvl)/5 + 2) * power * (self.atk/self.defn))/50 + 2) * mod1
        rng2 = ((((2 * self.lvl)/5 + 2) * power * (self.atk/self.defn))/50 + 2) * mod2
        self.dmg = int(random(rng1, rng2))
        if self.typeopp == "grass":
             self.dmg = self.dmg * 2
        if self.typeopp == "water" or self.typeopp == "fire":
            self.dmg = self.dmg * 0.5
        return (self.dmg)