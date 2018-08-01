class PokemonData: #holds all the stats for each pokemon
    keylist = [] #lists hold the stats where key holds the digits and name holds the names
    namelist = []
    
    def chimchar (self): #chimchar stats
        self.stats = [180, 108, 63, 113, 64, 103] #[health, attack, defense, special attack, special defense, speed]
        self.names = ["chimchar", "fire", "none", "tackle", "flame charge", "growl", "dig"]
        return (self.stats, self.names)
    
    def eevee (self): #eevee stats
        self.stats = [200, 103, 82, 120, 58, 68] #[health, attack, defense, special attack, special defense, speed]
        self.names = ["eevee", "normal", "none", "growl", "scratch", "shadowball", "dig"]
        return (self.stats, self.names)
        
    def bidoof (self): #bidoof stats
        self.stats = [198, 85, 76, 67, 79, 80] #[health, attack, defense, special attack, special defense, speed]
        self.names = ["bidoof", "normal", "none", "tackle", "tailwhip", "icebeam", "cut"]
        return (self.stats, self.names)
        
    def bulbasaur (self): #bulbasaur stats
        self.stats = [140, 108, 64, 126, 65, 104] #[health, attack, defense, special attack, special defense, speed]
        self.names = ["bulbasaur", "grass", "poison", "tackle", "vine whip", "growl", "poison powder"]
        return (self.stats, self.names)
    
    def charmander (self): #charmander stats
        self.stats = [140, 112, 62, 120, 60, 126] #[health, attack, defense, special attack, special defense, speed]
        self.names = ["charmander", "fire", "none", "growl", "scratch", "ember", "smokescreen"]
        return (self.stats, self.names)
        
    def squirtle (self): #squirtle stats
        self.stats = [140, 107, 65, 109, 63, 102] #[health, attack, defense, special attack, special defense, speed]
        self.names = ["squirtle", "water", "none", "tackle", "tailwhip", "bubble", "withdraw"]
        return (self.stats, self.names)
        
    def __getitem__ (self, key): #methods add the variables to their proper lists
        self.keylist.extend(self.stats)
        return (self.keylist)
    def __getitem1__ (self, key):
        self.namelist.extend(self.names)
