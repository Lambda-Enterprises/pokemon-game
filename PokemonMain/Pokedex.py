class Pokedex:
    def __init__(self):
        self.stats = [] #[lvl, hp, atk, def, spatk, spdef, sp]
        self.names = [] #[name, type1, type2, move1, move2, move3, move4]
    
    def chimchar (self): #chimchar stats
        self.stats = [50, 180, 108, 63, 113, 64, 103]
        self.names = ["Chimchar", "fire", "none", "tackle", "flame charge", "growl", "dig"]
        return (self.stats, self.names)
    
    def eevee (self): #eevee stats
        self.stats = [50, 200, 103, 82, 120, 58, 68]
        self.names = ["Eevee", "normal", "none", "growl", "scratch", "shadowball", "dig"]
        return (self.stats, self.names)
    
    def bidoof (self): #bidoof stats
        self.stats = [50, 198, 85, 76, 67, 79, 80]
        self.names = ["Bidoof", "normal", "none", "tackle", "tailwhip", "icebeam", "cut"]
        return (self.stats, self.names)
    
    def bulbasaur (self): #bulbasaur stats
        self.stats = [50, 140, 108, 64, 126, 65, 104]
        self.names = ["Bulbasaur", "grass", "poison", "tackle", "vine whip", "growl", "poison powder"]
        return (self.stats, self.names)
    
    def charmander (self): #charmander stats
        self.stats = [50, 140, 112, 62, 120, 60, 126]
        self.names = ["Charmander", "fire", "none", "growl", "scratch", "ember", "smokescreen"]
        return (self.stats, self.names)
    
    def squirtle (self): #squirtle stats
        self.stats = [50, 140, 107, 65, 109, 63, 102]
        self.names = ["Squirtle", "water", "none", "tackle", "tailwhip", "bubble", "withdraw"]
        return (self.stats, self.names)
    
    def __getStats__(self):
        return self.stats
    
    def __getNames__(self):
        return self.names
