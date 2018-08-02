from Pokedex import *

class Pokemon: #holds all the stats for each pokemon
    def __init__(self):
        self.pokedex = Pokedex()
        self.stats = []
        self.names = []
    
    def __setPokemon__(self, name):
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
    
    def __getStats__(self):
        return self.stats
    
    def __getNames__(self):
        return self.names
