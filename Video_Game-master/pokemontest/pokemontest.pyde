from time import sleep

class MoveDamage: #class calculates damage value from attacks
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

class Status: #for status variables, there are two options, convert the stat (as shown below) and make that value equal to current stats or take a changed value in the stat and subtract it or add it from the original value
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

class pokemondata: #holds all the stats for each pokemon
    keylist = [] #lists hold the stats where key holds the digits and name holds the names
    namelist = []
    
    def bulbasaur (self): #bulbasaur stats
        self.stats = [140, 108, 64, 126, 65, 104] #[140, 108, 108, 126, 126, 104]
        self.names = ["bulbasaur", "grass", "poison", "tackle", "vine whip", "growl", "poison powder"]
        return (self.stats, self.names)
    
    def charmander (self): #charmander stats
        self.stats = [140, 112, 62, 120, 60, 126] #[140, 112, 102, 120, 109, 126]
        self.names = ["charmander", "fire", "none", "growl", "scratch", "ember", "smokescreen"]
        return (self.stats, self.names)
        
    def squirtle (self): #squirtle stats
        self.stats = [140, 107, 65, 109, 63, 102] #[140, 107, 126, 109, 125, 102]
        self.names = ["squirtle", "water", "none", "tackle", "tailwhip", "bubble", "withdraw"]
        return (self.stats, self.names)
        
    def __getitem__ (self, key): #methods add the variables to their proper lists
        self.keylist.extend(self.stats)
        return (self.keylist)
    def __getitem1__ (self, key):
        self.namelist.extend(self.names)
        return (self.namelist)
        #for some reason all the variables appear in the same list but it still works so it's fine
c1 = 0 #counters for animation
c2 = 0
c3 = 0
def setup():
    global plyrlist, plyrname, plyrbox, plyracc, plyratk, plyrspatk, plyrsta, plyrstate, plyracc, cpuacc, accuplyr, accucpu, psn
    global cpulist, cpuname, cpubox, cpuacc, cpuatk, cpuspatk, cpusta, cpustate
    global x, y, p, c, m, l, mode, r, textbox, x1, y1, win, lose
    global bulb, charm, squir, stage, select, weather
    global bulbf, bulbb, charf, charb, squirf, squirb
    size(800, 700)
    plyrlist = [] #these are the actual lists that will hold the stats for the player and cpu
    plyrname = []
    plyraccu = 0
   
    cpulist = []
    cpuname = []
    cpuaccu = 0

    bulb = loadImage("bulbasaur.png")
    charm = loadImage("charmander.png")
    squir = loadImage("squirtle.png")
    bulbf = loadImage("bfront.png")
    bulbb = loadImage("bbacks.png")
    charf = loadImage("cfront.png")
    charb = loadImage("cbacks.png")
    squirf = loadImage("sfront.png")
    squirb = loadImage("sbacks.png")
    plyrbox = loadImage("plyrbox.png")
    cpubox = loadImage("cpubox.png")
    textbox = loadImage("textbox.png")
    select = loadImage("select.png")
    psn = loadImage("poison.png")
    win = loadImage("win.png")
    lose = loadImage("fail.png")
    p = pokemondata() #calls upon pokemondata to receive the class stats for the lists
    c = pokemondata()
    l = p
    m = c
    #below are starting variables that are changed later on
    plyracc = 0
    accuplyr = 0
    plyrstate = "normal"
    cpuacc = 0
    acccpu = 0
    cpustate = "normal"
    weather = "clear"
    
    plyratk = 0
    plyrspatk = 0
    plyrsta = 0
    cpuatk = 0
    cpuspatk = 0
    cpusta = 0
    
    #below are the coordinates for the cursor which can be changed to move its position
    x = 200 #helps to choose pokemon and moves
    y = 400 #there are two sets of coordinates for two different cursors
    x1 = 25
    y1 = 620
    stage = loadImage("18502.png")
    mode = 1
    
def draw():
    global x, y, p, c, l, mode, c1, c2, c3, m, r, x1, y1
    global plyrlist, plyrname, plyrbox, fight, plyratk, plyrspatk, cpuatk, cpuspatk, plyrsta, cpusta, plyrstate, cpustate, plyracc, cpuacc, accuplyr, accucpu, psn
    global cpulist, cpuname, cpubox, textbox, win, lose
    global bulb, charm, squir, stage, select
    background(0, 125, 157) 
    rect (x, y, 100, 100)
    fill (0, 200, 0)
    rect (200, 400, 80, 80)
    fill (200, 0, 0)
    rect(400, 400, 80, 80)
    fill (0, 0, 200)
    rect(600, 400, 80, 80)
    fill (255)
    #animation    
    a = (c1 % 16) * 60
    b = (c1 / 16) * 70
    copy (bulb, a, b, 60, 70, 100, 100, 180, 213)
    c1 = c1 + 1 #runs through a sprite sheet to create the animation
    delay(50)
    if c1 == 15:
        c1 = 0
    
    a = (c1 % 16) * 60
    b = (c1 / 16) * 70
    copy (charm, a, b, 60, 70, 300, 100, 180, 213)
    c1 = c1 + 1
    delay(50)
    if c1 == 15:
        c1 = 0
    
    a = (c1 % 16) * 60
    b = (c1 / 16) * 70
    copy (squir, a, b, 60, 70, 500, 100, 180, 213)
    c1 = c1 + 1
    delay(50)
    if c1 == 15:
        c1 = 0
     
    #your pokemon
    if mode == 1:
        text("LEFT and RIGHT to move, u to select", 0, 32)
        textSize(32)
        fill (255)
        if keyPressed:
            if key == 'u': #depending on the position of the cursor, different pokemon are selected
                if x == 200:
                    plyrlist.extend(l.__getitem__(p.bulbasaur())) #calls upon the class and obtains the proper variables
                    plyrname.extend(l.__getitem1__(p.bulbasaur()))
                    print plyrlist, plyrname 
                    mode = 2 #cpu choice
                elif x == 400:
                    plyrlist.extend(l.__getitem__(p.charmander()))
                    plyrname.extend(l.__getitem1__(p.charmander()))
                    print plyrlist, plyrname
                    mode = 2 
                elif x == 600:
                    plyrlist.extend(l.__getitem__(p.squirtle()))
                    plyrname.extend(l.__getitem1__(p.squirtle()))
                    print plyrlist, plyrname
                    mode = 2
    #cpu pokemon
    if mode == 2:
        r = int(random(2)) #cpu's pokemon is always random each battle
        if r == 0:
            cpulist.extend(m.__getitem__(c.bulbasaur()))
            cpuname.extend(m.__getitem1__(c.bulbasaur()))
            print cpulist, cpuname
            mode = 3 #battlemode
            print ("press i to select move")
        elif r == 1:
            cpulist.extend(m.__getitem__(c.charmander()))
            cpuname.extend(m.__getitem1__(c.charmander()))
            print cpulist, cpuname
            mode = 3
            print ("press i to select move")
        elif r == 2:
            cpulist.extend(m.__getitem__(c.squirtle()))
            cpuname.extend(m.__getitem1__(c.squirtle()))
            print cpulist, cpuname
            mode = 3
            print ("press i to select move")
    #battlemode
    if mode == 3:
        image (stage, 0, 0, 800, 600)
        image (plyrbox, 465, 475, 335, 125)
        image (cpubox, 0, 200, 260, 100)
        image (textbox, 0, 600, 800, 100)
        image (select, x1, y1, 15, 15)
        #below are damage and stat values given based on the values in the lists
        plyratk = MoveDamage(50, plyrlist[1], cpulist[8], plyrname[1], cpuname[8], cpuacc, weather, 0)
        plyrspatk = MoveDamage(50, plyrlist[3], cpulist[10], plyrname[1], cpuname[8], cpuacc, weather, 0)
        plyrsta = Status(cpulist[6], cpulist[7], cpulist[8], cpustate, cpuacc, plyrlist[2])
        cpuatk = MoveDamage(50, cpulist[7], plyrlist[2], cpuname[8], plyrname[1], plyracc, weather, 0)
        cpuspatk = MoveDamage(50, cpulist[9], plyrlist[4], cpuname[8], plyrname[1], plyracc, weather, 0)
        cpusta = Status(plyrlist[0], plyrlist[1], plyrlist[2], plyrstate, plyracc, cpulist[8]) 
        #more animation
        if plyrname[0] == "bulbasaur":
            c = (c2 % 2) * 80
            d = (c2 / 2) * 61
            copy (bulbb, c, d, 80, 61, 100, 440, 160, 160)
            c2 = c2 + 1
            if c2 == 2:
                c2 = 0
        elif plyrname[0] == "charmander":
            c = (c2 % 2) * 80
            d = (c2 / 2) * 61
            copy (charb, c, d, 80, 61, 100, 440, 160, 160)
            c2 = c2 + 1
            if c2 == 2:
                c2 = 0
        else:
            c = (c2 % 2) * 80
            d = (c2 / 2) * 80
            copy (squirb, c, d, 80, 61, 100, 440, 160, 160)
            c2 = c2 + 1
            if c2 == 2:
                c2 = 0
                
        if cpuname[7] == "bulbasaur":
            e = (c3 % 2) * 80
            f = (c3 / 2) * 80
            copy (bulbf, e, f, 80, 80, 470, 210, 240, 240)
            c3 = c3 + 1
            if c3 == 2:
                c3 = 0
        elif cpuname[7] == "charmander":
            e = (c3 % 2) * 80
            f = (c3 / 2) * 80
            copy (charf, e, f, 80, 80, 470, 210, 240, 240)
            c3 = c3 + 1
            if c3 == 2:
                c3 = 0
        elif cpuname[7] == "squirtle":
            e = (c3 % 2) * 80
            f = (c3 / 2) * 80
            copy (squirf, e, f, 80, 80, 470, 210, 240, 240)
            c3 = c3 + 1
            if c3 == 2:
                c3 = 0
        #sets the text to suit the pokemon selected
        fill (0)
        text (plyrname[0], 520, 525)
        text ("50", 740, 525)
        textSize (25)
        text (cpuname[7], 10, 250)
        text ("50", 180, 250)
        textSize (28)
        text (plyrname[3], 50, 640)
        text (plyrname[4], 195, 640)
        text (plyrname[5], 360, 640)
        text (plyrname[6], 495, 640)
        textSize (30)
        fill(255)
        
        fill (20, 100, 50)
        rect(650, 540, plyrlist[0], 10)
        rect(100, 265, cpulist[6], 10)
        
        if keyPressed:
            if key == "i": #select move with i
                accuplyr = int(random(0, plyracc)) #checks to see if you hit the target
                if accuplyr == 0: #the higher plyracc, the more likely to miss
                    if x1 == 25: #cursor position and pokemon affect which move is used
                        print(plyrname[0], "used", plyrname[3])
                        if plyrname[0] == "bulbasaur" or plyrname[0] == "squirtle":
                            cpulist[6] = cpulist[6] - plyratk.tackle()
                        if plyrname[0] == "charmander":
                            cpulist[7] = plyrsta.growl()
                        
                        
                    if x1 == 175:
                        print(plyrname[0], "used", plyrname[4])
                        if plyrname[0] == "bulbasaur":
                            cpulist[6] = cpulist[6] - plyratk.vinewhip()
                            if cpuname[8] == "fire" or cpuname[8] == "grass":
                                print ("it's not very effective")
                            if cpuname[8] == "water":
                                print("it's super effective")
                        if plyrname[0] == "charmander":
                            cpulist[6] = cpulist[6] - plyratk.scratch()
                        if plyrname[0] == "squirtle":
                            cpulist[8] = plyrsta.tailwhip()
                        
        
                    if x1 == 325:
                        print(plyrname[0], "used", plyrname[5])
                        if plyrname[0] == "bulbasaur":
                            cpulist[7] = plyrsta.growl()
                        if plyrname[0] == "charmander":
                            cpulist[6] = cpulist[6] - plyrspatk.ember()
                            if cpuname[8] == "fire" or cpuname[8] == "water":
                                print ("it's not very effective")
                            if cpuname[8] == "grass":
                                print("it's super effective")
                        if plyrname[0] == "squirtle":
                            cpulist[6] = cpulist[6] - plyrspatk.bubble()
                            if cpuname[8] == "grass" or cpuname[8] == "water":
                                print ("it's not very effective")
                            if cpuname[8] == "fire":
                                print("it's super effective")
                        
                        
                    if x1 == 475:
                        print(plyrname[0], "used", plyrname[6])  
                        
                        if plyrname[0] == "bulbasaur":
                            cpustate = plyrsta.poisonpowder()
                        if plyrname[0] == "charmander":
                            cpuuacc = plyrsta.smokescreen()
                        if plyrname[0] == "squirtle":
                            plyrlist[2] = plyrsta.withdraw()
                else:
                    print("your attack missed")
                if plyrstate == "poisoned":
                    image(psn, 550, 535, 40, 20)
                    print(plyrname[0], "is hurt by poison")
                    plyrlist[0] = plyrlist[0] - (plyrlist[0] * 0.16)   
                if cpulist[6] <= 0: #if cpu health is equal or below 0
                    mode = 5 #victory
                else:    
                    mode = 4 #cpu turn
            
    if mode == 4: #cpu turn
        accucpu = int(random(0, cpuacc))
        if accucpu == 0:
            r1 = int(random(0, 3)) #the move the cpu uses is always random
            if r1 == 0:
                print(cpuname[7], "used", cpuname[10])
                if cpuname[7] == "bulbasaur" or cpuname[7] == "squirtle":
                    plyrlist[0] = plyrlist[0] - cpuatk.tackle()
                if cpuname[7] == "charmander":
                    plyrlist[1] = cpusta.growl()
                    
            if r1 == 1:
                print(cpuname[7], "used", cpuname[11])
                if cpuname[7] == "bulbasaur":
                    plyrlist[0] = plyrlist[0] - cpuatk.vinewhip()
                    if plyrname[1] == "fire" or plyrname[1] == "grass":
                        print("it's not very effective")
                    if plyrname[1] == "water":
                        print("it's super effective")
                if cpuname[7] == "charmander":
                    plyrlist[0] = plyrlist[0] - cpuatk.scratch()
                if cpuname[7] == "squirtle":
                    plyrlist[2] = cpusta.tailwhip()
                    
            if r1 == 2:
                print(cpuname[7], "used", cpuname[12])
                if cpuname[7] == "bulbasaur":
                    plyrlist[1] = cpusta.growl()
                if cpuname[7] == "charmander":
                    plyrlist[0] = plyrlist[0] - cpuspatk.ember()
                    if plyrname[1] == "fire" or plyrname[1] == "water":
                        print("it's not very effective")
                    if plyrname[1] == "grass":
                        print("it's super effective")
                if cpuname[7] == "squirtle":
                    plyrlist[0] = plyrlist[0] - cpuspatk.bubble()
                    if plyrname[1] == "water" or plyrname[1] == "grass":
                        print("it's not very effective")
                    if plyrname[1] == "fire":
                        print("it's super effective")
            
            if r1 == 3:
                print(cpuname[7], "used", cpuname[13])
                if cpuname[0] == "bulbasaur":
                    plyrstate = cpusta.poisonpowder()
                if cpuname[0] == "charmander":
                    plyracc = cpusta.smokescreen()
                if cpuname[0] == "squirtle":
                    cpulist[8] = cpusta.withdraw() 
        else:
            print("oppponent missed")
        if cpustate == "poisoned":
            image(psn, 25, 260, 40, 20)
            print(cpuname[7], "is hurt by poison")
            cpulist[6] = cpulist[6] - (cpulist[6] * 0.16)
        if plyrlist[0] <= 0: #if player health is equal or below 0
            mode = 6 #loss
        else:
            mode = 3 #player turn
    
    if mode == 5: #victory screen
        image(win, 0, 0, 800, 800)
    if mode == 6: #losing screen
        image(lose, 0, 0, 800, 800)
        
def keyPressed():
    global plyrlist, plyrname
    global cpulist, cpuname, weather
    global x, y, p, c, l, mode, x1, y1
    #the movement controls for the cursors
    if mode == 1:
        if keyCode == LEFT or key == 'a': #left
            x = x - 200
            if x < 200:
                x = 600
        if keyCode == RIGHT or key == 'd': #right
            x = x + 200
            if x > 600:
                x = 200
    if mode == 3:
        if keyCode == LEFT or key == 'a': #left
            x1 = x1 - 150
            if x1 < 25:
                x1 = 475
        if keyCode == RIGHT or key == 'd': #right
            x1 = x1 + 150
            if x1 > 600:
                x1 = 25
    while not keyReleased():
        sleep(0.001)

def keyReleased():
    return True
