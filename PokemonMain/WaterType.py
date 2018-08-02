from Move import *

class WaterType("Move"):
    
    def bubble (self):
        typemove = "water"
        power = 40
        uses = 30
        counter = 0
        crit = 1
        stab = 1
        wthr = 1
        x = int(random(1, 30))
        y = int(random(0, 5))
        if x == 1:
            crit = 2
        if y == 0:
            self.accuracy = self.accuracy + 1
            counter = counter + 1
            if counter == 6:
                print ("accuracy cannot go lower")
        if typemove == self.typepkmn:
            stab = 1.5
        if self.sky == "sunny":
            whtr = 0.5
        elif self.sky == "rain":
            whtr = 2
        else:
            whtr = 1
        mod1 = wthr * crit * 0.85 * stab
        mod2 = wthr * crit * 1.00 * stab
        rng1 = ((((2 * self.lvl)/5 + 2) * power * (self.atk/self.defn))/50 + 2) * mod1
        rng2 = ((((2 * self.lvl)/5 + 2) * power * (self.atk/self.defn))/50 + 2) * mod2
        self.dmg = int(random(rng1, rng2))
        if self.typeopp == "fire":
             self.dmg = self.dmg * 2
        if self.typeopp == "grass" or self.typeopp == "water":
            self.dmg = self.dmg * 0.5
        return (self.dmg)
        return (self.accuracy)
