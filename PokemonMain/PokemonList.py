from Pokedex import *

class PokemonData: #holds all the stats for each pokemon
    self.stats = [] # [health, attack, defense, special attack, special defense, speed]
    self.names = [] # [name, type1, type2, move1, move2, move3, move4]
    
    def __init__ (self, name):
        if name == 'chimchar':
            chimchar (self)
        elif name == 'eevee':
            eevee (self)
        elif name == 'bidoof':
            bidoof (self)
        elif name == 'bulbasaur':
            bulbasaur (self)
        elif name == 'charmander':
            charmander (self)
        elif name == 'squirtle':
            squirtle (self)
        else:
            raise Exception('Invalid Pokemon!')
    
    def __getStats__ (self, name): #methods add the variables to their proper lists
        return (self.stats)
    
    def __getNames__ (self):
        return (self.names)
        #for some reason all the variables appear in the same list
        #but it still works so it's fine
