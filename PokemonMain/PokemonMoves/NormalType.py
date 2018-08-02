from Move import *

class NormalType("Move"):
    
    
    # physical attacks
    def tackle(self): #all variables need to have self beside it to retain the data
        typemove = "normal" #type of attack
        power = 40 #standard power
        crit = 1 #crit and stab (special type attack bonus) are extra variables that influence how much damage is used
        stab = 1
        x = int(random(1, 30)) #attacks have a 1/30 chance of being critical
        if x == 1:
            crit = 2
        if typemove == self.typepkmn: #stab works when the user's type is the same as the move type
            stab = 1.5
        mod1 = crit * 0.85 * stab #code will calculate two values (rng1 and rng2)
        mod2 = crit * 1.00 * stab
        rng1 = ((((2 * self.lvl)/5 + 2) * power * (self.atk/self.defn))/50 + 2) * mod1
        rng2 = ((((2 * self.lvl)/5 + 2) * power * (self.atk/self.defn))/50 + 2) * mod2
        self.dmg = int(random(rng1, rng2)) #the final damage is a random integer between the two ranges
        # if cputype == "ghost":
        #     dmg = dmg * 0
        return (self.dmg) #return the damage
    
    def scratch (self): #all attacks have their own methods
        typemove = "normal"
        power = 40
        uses = 35
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
        # if cputype == "ghost":
        #     dmg = dmg * 0 
        return (self.dmg)
    
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
    
    def dig (self):
        typemove = "ground"
        power = 45
        
