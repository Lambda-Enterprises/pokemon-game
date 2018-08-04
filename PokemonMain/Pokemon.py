from Pokedex import *
from Type import *
from Move import *

class Pokemon: #holds all the stats for each pokemon
    def __init__(self, lvl = 0, hp = 0, atk = 0, defn = 0, spatk = 0, spdefn = 0, sp = 0,
                 name = "", type = [None, None], move = [None, None, None, None]):
        self.lvl = lvl
        self.hp = hp
        self.atk = atk
        self.defn = defn
        self.spatk = spatk
        self.spdefn = spdefn
        self.sp = sp
        self.name = name
        self.type = type
        self.move = move
    
    def setPokemon(self, name):
        pokeDict = loadPokemon(name)
        stats = pokeDict['stats']
        names = pokeDict['names']
        (self.lvl, self.hp, self.atk, self.defn, 
         self.spatk, self.spdefn, self.sp) = tuple(x for x in stats)
        self.name = names[0]
        self.type = [Type.loadType(x) for x in names[1:3]]
        self.move = [Move.loadMove(x) for x in names[3:]]
    
    def getStats(self, name):
        pokeDict = loadPokemon(self.name)
        return pokeDict['stats']
    
    def getNames(self, name):
        pokeDict = loadPokemon(self.name)
        return pokeDict['names']
