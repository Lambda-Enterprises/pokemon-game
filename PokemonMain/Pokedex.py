from Pokemon import *
from Type import *
from Move import *

class Pokedex:
    def __init__(self):
        self.stats = [] #[lvl, hp, atk, def, spatk, spdef, sp]
        self.names = [] #[name, type1, type2, move1, move2, move3, move4]
    
    @staticmethod
    def loadPokemon(name):
        pokeDict = {
            'Bulbasaur': {
                'stats': [50, 140, 108, 64, 126, 65, 104],
                'names': ['Bulbasaur', 'grass', 'poison', 'tackle', 'vine whip', 'growl', 'poison powder']
            },
            'Charmander': {
                'stats': [50, 140, 112, 62, 120, 60, 126],
                'names': ['Charmander', 'fire', 'none', 'growl', 'scratch', 'ember', 'smokescreen']
            },
            'Squirtle': {
                'stats': [50, 140, 107, 65, 109, 63, 102],
                'names': ['Squirtle', 'water', 'none', 'tackle', 'tailwhip', 'bubble', 'withdraw']
            }
        }
        
        return pokeDict[name]
