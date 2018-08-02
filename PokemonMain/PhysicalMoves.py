class PhysicalMove: #class calculates damage value from attacks
    def __init__(self, lvl, atk, defn, typepkmn, typeopp, accuracy, sky, dmg): #initializes variables that are given in the class
        self.lvl = lvl #user level
        self.atk = atk #user attack/special attack
        self.defn = defn #opponent defense/special defense
        self.typepkmn = typepkmn #user type
        self.typeopp = typeopp #opponent type
        self.accuracy = accuracy #user accuracy
        self.sky = sky #weather
        self.dmg = dmg #damage value of attack
    # physical attacks
    def tackle (self): #all variables need to have self beside it to retain the data
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
    
    def dig (self):
        typemove = "ground"
        power = 45
        