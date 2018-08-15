from Database import *

class Pokedex:
    def __init__(self):
        self.pokeList = []
    
    def addPokemon(self, name):
        pokeDict = _referenceData()
        self.pokeList.append(pokeDict[name])
    
    def loadPokemon(self, name):
        pokeDict = _referenceData()
        return pokeDict[name]
    
    def __repr__(self):
        return str(self.pokeList)
    
    # [lvl, hp, atk, def, spatk, spdef, sp]
    # [name, type1, type2, move1, move2, move3, move4]
