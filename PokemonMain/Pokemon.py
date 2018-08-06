import cx_Oracle
from Type import *
from Move import *

class Pokemon: #holds all the stats for each pokemon
    def __init__(self, name=None):
        try:
            with open('Data/Pokemon.json', 'r') as file:
                pokeDict = json.loads(file.read())
                file.close()
            pokemon = pokeDict[name]
            stats = pokemon['stats']
            names = pokemon['names']
            (self.lvl, self.hp, self.atk, self.defn, self.spatk,
            self.spdefn, self.sp) = tuple(x for x in stats)
            self.name = name
            self.type = [Type(x) for x in names[0:2]]
            self.move = [Move(x) for x in names[2:]]
        except:
            print('Invalid Pokemon!')
    
    def setPokemon(self, name):
        with open('Data/Pokemon.json', 'r') as file:
            pokeDict = json.loads(file.read())
            file.close()
        pokemon = pokeDict[name]
        stats = pokemon['stats']
        names = pokemon['names']
        (self.lvl, self.hp, self.atk, self.defn, self.spatk,
         self.spdefn, self.sp) = tuple(x for x in stats)
        self.name = name
        self.type = [Type(x) for x in names[0:2]]
        self.move = [Move(x) for x in names[2:]]
    
    @property
    def getStats(self):
        with open('Data/Pokemon.json', 'r') as file:
                pokeDict = json.loads(file.read())
                file.close()
        return pokeDict[self.name]['stats']
    
    @property
    def getNames(self):
        with open('Data/Pokemon.json', 'r') as file:
                pokeDict = json.loads(file.read())
                file.close()
        return pokeDict[self.name]['names']
