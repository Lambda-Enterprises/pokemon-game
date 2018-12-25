from sys import path
path.append("./../Database")
from Database import *
from Move import *
from Type import *
from Pokedex import *

class Pokemon: #holds all the stats for each pokemon
    def __init__(self, name = None, db = None):
        self.data = db.accessPokemon(name)
        if name and self.data and db:
            self.id = self.data[0]
            self.name = self.data[1]
            self.type1 = Type(self.data[2], db)
            self.type2 = Type(self.data[3], db)
        elif not self.data:
            print('Invalid Pokemon!')
    
    def setPokemon(self, name):
        self.data = db.accessPokemon(name)
        if name and self.data:
            id = self.data[0]
            name = self.data[1]
            type1 = self.data[2]
            type2 = self.data[3]
        elif not name:
            print('Empty Pokemon Name!')
        elif not self.data:
            print('Invalid Pokemon!')
    
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
