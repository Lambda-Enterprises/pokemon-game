from time import sleep
from PhysicalMoves import *
from Pokemon import *
from StatusMoves import *

c1 = 0 #counters for animation
c2 = 0
c3 = 0

def setup():
    global plyrStats, plyrNames, plyrbox, plyracc, plyratk, plyrspatk, plyrsta, plyrstate, plyracc, cpuacc, accuplyr, accucpu, psn
    global cpuStats, cpuNames, cpubox, cpuacc, cpuatk, cpuspatk, cpusta, cpustate
    global playerPokemon, comPokemon
    global x, y, mode, r, textbox, x1, y1, win, lose
    global bulb, charm, squir, stage, select, weather
    global bulbf, bulbb, charf, charb, squirf, squirb
    size(800, 700)
    plyrStats = [] #these are the actual lists that will hold the stats for the player and cpu
    plyrNames = []
    plyraccu = 0
    
    cpuStats = []
    cpuNames = []
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
    playerPokemon = Pokemon() #calls upon PokemonData to receive the class stats for the lists
    comPokemon = Pokemon()
    
    #below are starting variables that may change later on
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
    
    #cpu pokemon
    r = int(random(2)) #cpu's pokemon is always random each battle
    if r == 0:
        playerPokemon.__setPokemon__('bulbasaur')
        print (comPokemon.__getStats__(), comPokemon.__getNames__())
        mode = 3 #battlemode
        print ("press i to select move")
    elif r == 1:
        playerPokemon.__setPokemonList__('charmander')
        print (comPokemon.__getStats__(), comPokemon.__getNames__())
        mode = 3
        print ("press i to select move")
    elif r == 2:
        playerPokemon.__setPokemon__('squirtle')
        print (comPokemon.__getStats__(), comPokemon.__getNames__())
        mode = 3
        print ("press i to select move")
    cpuStats, cpuNames = comPokemon.__getStats__(), comPokemon.__getNames__()

def draw():
    global x, y, mode, c1, c2, c3, r, x1, y1
    global playerPokemon, comPokemon
    global plyrStats, plyrNames, plyrbox, fight, plyratk, plyrspatk, cpuatk, cpuspatk, plyrsta, cpusta, plyrstate, cpustate, plyracc, cpuacc, accuplyr, accucpu, psn
    global cpuStats, cpuNames, cpubox, textbox, win, lose
    global bulb, charm, squir, stage, select
    background(0, 125, 157)
    rect(x, y, 100, 100)
    fill(0, 200, 0)
    rect(200, 400, 80, 80)
    fill(200, 0, 0)
    rect(400, 400, 80, 80)
    fill(0, 0, 200)
    rect(600, 400, 80, 80)
    fill(255)
    #animation
    a = (c1 % 16) * 60
    b = (c1 / 16) * 70
    copy(bulb, a, b, 60, 70, 100, 100, 180, 213)
    c1 = c1 + 1 #runs through a sprite sheet to create the animation
    delay(50)
    if c1 == 15:
        c1 = 0
    
    a = (c1 % 16) * 60
    b = (c1 / 16) * 70
    copy(charm, a, b, 60, 70, 300, 100, 180, 213)
    c1 = c1 + 1
    delay(50)
    if c1 == 15:
        c1 = 0
    
    a = (c1 % 16) * 60
    b = (c1 / 16) * 70
    copy(squir, a, b, 60, 70, 500, 100, 180, 213)
    c1 = c1 + 1
    delay(50)
    if c1 == 15:
        c1 = 0
    
    #Pokemon Selection
    if mode == 1:
        text("LEFT and RIGHT to move, u to select", 0, 32)
        textSize(32)
        fill (255)
    #Battle Mode
    elif mode == 3:
        image (stage, 0, 0, 800, 600)
        image (plyrbox, 465, 475, 335, 125)
        image (cpubox, 0, 200, 260, 100)
        image (textbox, 0, 600, 800, 100)
        image (select, x1, y1, 15, 15)
        #below are damage and stat values given based on the values in the lists
        plyratk = PhysicalMove(50, plyrStats[1], cpuStats[8], plyrNames[1], cpuNames[8], cpuacc, weather, 0)
        plyrspatk = PhysicalMove(50, plyrStats[3], cpuStats[10], plyrNames[1], cpuNames[8], cpuacc, weather, 0)
        plyrsta = StatusMove(cpuStats[6], cpuStats[7], cpuStats[8], cpustate, cpuacc, plyrStats[2])
        cpuatk = PhysicalMove(50, cpuStats[7], plyrStats[2], cpuNames[8], plyrNames[1], plyracc, weather, 0)
        cpuspatk = PhysicalMove(50, cpuStats[9], plyrStats[4], cpuNames[8], plyrNames[1], plyracc, weather, 0)
        cpusta = StatusMove(plyrStats[0], plyrStats[1], plyrStats[2], plyrstate, plyracc, cpuStats[8]) 
        #more animation
        if plyrNames[0] == "bulbasaur":
            c = (c2 % 2) * 80
            d = (c2 / 2) * 61
            copy (bulbb, c, d, 80, 61, 100, 440, 160, 160)
            c2 = c2 + 1
            if c2 == 2:
                c2 = 0
        elif plyrNames[0] == "charmander":
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
        
        if cpuNames[7] == "bulbasaur":
            e = (c3 % 2) * 80
            f = (c3 / 2) * 80
            copy (bulbf, e, f, 80, 80, 470, 210, 240, 240)
            c3 = c3 + 1
            if c3 == 2:
                c3 = 0
        elif cpuNames[7] == "charmander":
            e = (c3 % 2) * 80
            f = (c3 / 2) * 80
            copy (charf, e, f, 80, 80, 470, 210, 240, 240)
            c3 = c3 + 1
            if c3 == 2:
                c3 = 0
        elif cpuNames[7] == "squirtle":
            e = (c3 % 2) * 80
            f = (c3 / 2) * 80
            copy (squirf, e, f, 80, 80, 470, 210, 240, 240)
            c3 = c3 + 1
            if c3 == 2:
                c3 = 0
        #sets the text to suit the pokemon selected
        fill (0)
        text (plyrNames[0], 520, 525)
        text ("50", 740, 525)
        textSize (25)
        text (cpuNames[7], 10, 250)
        text ("50", 180, 250)
        textSize (28)
        text (plyrNames[3], 50, 640)
        text (plyrNames[4], 195, 640)
        text (plyrNames[5], 360, 640)
        text (plyrNames[6], 495, 640)
        textSize (30)
        fill(255)
        
        fill (20, 100, 50)
        rect(650, 540, plyrStats[0], 10)
        rect(100, 265, cpuStats[6], 10)
    # CPU Turn
    elif mode == 4:
        accucpu = int(random(0, cpuacc))
        if accucpu == 0:
            r1 = int(random(0, 3)) #the move the cpu uses is always random
            if r1 == 0:
                print(cpuNames[7], "used", cpuNames[10])
                if cpuNames[7] == "bulbasaur" or cpuNames[7] == "squirtle":
                    plyrStats[0] = plyrStats[0] - cpuatk.tackle()
                if cpuNames[7] == "charmander":
                    plyrStats[1] = cpusta.growl()
                    
            if r1 == 1:
                print(cpuNames[7], "used", cpuNames[11])
                if cpuNames[7] == "bulbasaur":
                    plyrStats[0] = plyrStats[0] - cpuatk.vinewhip()
                    if plyrNames[1] == "fire" or plyrNames[1] == "grass":
                        print("it's not very effective")
                    if plyrNames[1] == "water":
                        print("it's super effective")
                if cpuNames[7] == "charmander":
                    plyrStats[0] = plyrStats[0] - cpuatk.scratch()
                if cpuNames[7] == "squirtle":
                    plyrStats[2] = cpusta.tailwhip()
                    
            if r1 == 2:
                print(cpuNames[7], "used", cpuNames[12])
                if cpuNames[7] == "bulbasaur":
                    plyrStats[1] = cpusta.growl()
                if cpuNames[7] == "charmander":
                    plyrStats[0] = plyrStats[0] - cpuspatk.ember()
                    if plyrNames[1] == "fire" or plyrNames[1] == "water":
                        print("it's not very effective")
                    if plyrNames[1] == "grass":
                        print("it's super effective")
                if cpuNames[7] == "squirtle":
                    plyrStats[0] = plyrStats[0] - cpuspatk.bubble()
                    if plyrNames[1] == "water" or plyrNames[1] == "grass":
                        print("it's not very effective")
                    if plyrNames[1] == "fire":
                        print("it's super effective")
            
            if r1 == 3:
                print(cpuNames[7], "used", cpuNames[13])
                if cpuNames[0] == "Bulbasaur":
                    plyrstate = cpusta.poisonpowder()
                if cpuNames[0] == "Charmander":
                    plyracc = cpusta.smokescreen()
                if cpuNames[0] == "Squirtle":
                    cpuStats[8] = cpusta.withdraw() 
        else:
            print("oppponent missed")
        if cpustate == "poisoned":
            image(psn, 25, 260, 40, 20)
            print(cpuNames[7], "is hurt by poison")
            cpuStats[6] = cpuStats[6] - (cpuStats[6] * 0.16)
        if plyrStats[0] <= 0: #if player health is equal or below 0
            mode = 6 #loss
        else:
            mode = 3 #player turn
    #Player Win
    elif mode == 5:
        image(win, 0, 0, 800, 800)
    #PLayer Loss
    elif mode == 6:
        image(lose, 0, 0, 800, 800)

def keyPressed():
    global playerPokemon, plyrStats, plyrNames, accuplyr
    global cpuStats, cpuNames
    global x, y, l, mode, x1, y1
    #the movement controls for the cursors
    if mode == 1: #Pokemon Selection
        if keyCode == ENTER: #depending on the position of the cursor, different pokemon are selected
            if x == 200:
                playerPokemon.__setPokemon__('bulbasaur')
                print playerPokemon.__getStats__(), playerPokemon.__getNames__()
                mode = 2 #cpu choice
            elif x == 400:
                playerPokemon.__setPokemon__('charmander')
                print playerPokemon.__getStats__(), playerPokemon.__getNames__()
                mode = 2 
            elif x == 600:
                playerPokemon.__setPokemon__('squirtle')
                print playerPokemon.__getStats__(), playerPokemon.__getNames__()
                mode = 2
            plyrStats, plyrNames = playerPokemon.__getStats__(), playerPokemon.__getNames__()
        elif keyCode == LEFT or key == 'a': #left
            x = x - 200
            if x < 200:
                x = 600
        elif keyCode == RIGHT or key == 'd': #right
            x = x + 200
            if x > 600:
                x = 200
    elif mode == 3: #Battle Mode
        if keyPressed:
            if keyCode == ENTER: #select move with ENTER
                accuplyr = int(random(0, plyracc)) #checks to see if you hit the target
                if accuplyr == 0: #the higher plyracc, the more likely to miss
                    if x1 == 25: #cursor position and pokemon affect which move is used
                        print(plyrNames[0], "used", plyrNames[3])
                        if plyrNames[0] == "bulbasaur" or plyrNames[0] == "squirtle":
                            cpuStats[6] = cpuStats[6] - plyratk.tackle()
                        if plyrNames[0] == "charmander":
                            cpuStats[7] = plyrsta.growl()
                    elif x1 == 175:
                        print(plyrNames[0], "used", plyrNames[4])
                        if plyrNames[0] == "bulbasaur":
                            cpuStats[6] = cpuStats[6] - plyratk.vinewhip()
                            if cpuNames[8] == "fire" or cpuNames[8] == "grass":
                                print ("it's not very effective")
                            if cpuNames[8] == "water":
                                print("it's super effective")
                        if plyrNames[0] == "charmander":
                            cpuStats[6] = cpuStats[6] - plyratk.scratch()
                        if plyrNames[0] == "squirtle":
                            cpuStats[8] = plyrsta.tailwhip()
                    elif x1 == 325:
                        print(plyrNames[0], "used", plyrNames[5])
                        if plyrNames[0] == "bulbasaur":
                            cpuStats[7] = plyrsta.growl()
                        if plyrNames[0] == "charmander":
                            cpuStats[6] = cpuStats[6] - plyrspatk.ember()
                            if cpuNames[8] == "fire" or cpuNames[8] == "water":
                                print ("it's not very effective")
                            if cpuNames[8] == "grass":
                                print("it's super effective")
                        if plyrNames[0] == "squirtle":
                            cpuStats[6] = cpuStats[6] - plyrspatk.bubble()
                            if cpuNames[8] == "grass" or cpuNames[8] == "water":
                                print ("it's not very effective")
                            if cpuNames[8] == "fire":
                                print("it's super effective")
                    elif x1 == 475:
                        print(plyrNames[0], "used", plyrNames[6])
                        if plyrNames[0] == "bulbasaur":
                            cpustate = plyrsta.poisonpowder()
                        if plyrNames[0] == "charmander":
                            cpuuacc = plyrsta.smokescreen()
                        if plyrNames[0] == "squirtle":
                            plyrStats[2] = plyrsta.withdraw()
                else:
                    print("your attack missed")
                if plyrstate == "poisoned":
                    image(psn, 550, 535, 40, 20)
                    print(plyrNames[0], "is hurt by poison")
                    plyrStats[0] = plyrStats[0] - (plyrStats[0] * 0.16)
                if cpuStats[6] <= 0: #if cpu health is equal or below 0
                    mode = 5 #victory
                else:
                    mode = 4 #cpu turn
        if keyCode == LEFT or key == 'a': #left
            x1 = x1 - 150
            if x1 < 25:
                x1 = 475
        elif keyCode == RIGHT or key == 'd': #right
            x1 = x1 + 150
            if x1 > 600:
                x1 = 25
    while not keyReleased():
        sleep(0.001)

def keyReleased():
    return True
