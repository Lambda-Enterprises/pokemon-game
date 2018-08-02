from Pokedex import *
from Type import *
from Move import *

class Pokemon: #holds all the stats for each pokemon
    def __init__(self, name=""):
        self.pokedex = Pokedex()
        if name != "":
            self.__setPokemonLists__(name)
            self.lvl = self.stats[0]
            self.hp = self.stats[1]
            self.atk = self.stats[2]
            self.defn = self.stats[3]
            self.spatk = self.stats[4]
            self.spdefn = self.stats[5]
            self.sp = self.stats[6]
            self.name = self.names[0]
            self.type = [self.names[1], self.names[2]]
            self.move = [self.names[3], self.names[4], self.names[5], self.names[6]]
        else:
            self.lvl = 0
            self.hp = 0
            self.atk = 0
            self.defn = 0
            self.spatk = 0
            self.spdefn = 0
            self.sp = 0
            self.name = ""
            self.type = ["", ""]
            self.move = ["", "", "", ""]
    
    def __setPokemonLists__(self, name):
        if name == 'chimchar':
            (self.stats, self.names) = self.pokedex.chimchar()
        elif name == 'eevee':
            (self.stats, self.names) = self.pokedex.eevee()
        elif name == 'bidoof':
            (self.stats, self.names) = self.pokedex.bidoof()
        elif name == 'bulbasaur':
            (self.stats, self.names) = self.pokedex.bulbasaur()
        elif name == 'charmander':
            (self.stats, self.names) = self.pokedex.charmander()
        elif name == 'squirtle':
            (self.stats, self.names) = self.pokedex.squirtle()
        else:
            raise Exception('Invalid Pokemon!')
    
    def __setPokemonStats__(self, name):
        self.lvl = self.stats[0]
        self.hp = self.stats[1]
        self.atk = self.stats[2]
        self.defn = self.stats[3]
        self.spatk = self.stats[4]
        self.spdefn = self.stats[5]
        self.sp = self.stats[6]
        self.name = self.names[0]
        self.type = [self.names[1], self.names[2]]
        self.move = [self.names[3], self.names[4], self.names[5], self.names[6]]
