class PokemonData: #holds all the stats for each pokemon
    keylist = [] #lists hold the stats where key holds the digits and name holds the names
    namelist = []
    
    def chimchar (self): #chimchar stats
        self.stats = [180, 108, 63, 113, 64, 103] #[health, attack, defense, special attack, special defense, speed]
        self.names = ["Chimchar", "fire", "none", "tackle", "flame charge", "growl", "dig"]
        return (self.stats, self.names)
    
    def eevee (self): #eevee stats
        self.stats = [200, 103, 82, 120, 58, 68] #[health, attack, defense, special attack, special defense, speed]
        self.names = ["Eevee", "normal", "none", "growl", "scratch", "shadowball", "dig"]
        return (self.stats, self.names)
    
    def bidoof (self): #bidoof stats
        self.stats = [198, 85, 76, 67, 79, 80] #[health, attack, defense, special attack, special defense, speed]
        self.names = ["Bidoof", "normal", "none", "tackle", "tailwhip", "icebeam", "cut"]
        return (self.stats, self.names)
    
    def bulbasaur (self): #bulbasaur stats
        self.stats = [140, 108, 64, 126, 65, 104] #[health, attack, defense, special attack, special defense, speed]
        self.names = ["Bulbasaur", "grass", "poison", "tackle", "vine whip", "growl", "poison powder"]
        return (self.stats, self.names)
    
    def charmander (self): #charmander stats
        self.stats = [140, 112, 62, 120, 60, 126] #[health, attack, defense, special attack, special defense, speed]
        self.names = ["Charmander", "fire", "none", "growl", "scratch", "ember", "smokescreen"]
        return (self.stats, self.names)
    
    def squirtle (self): #squirtle stats
        self.stats = [140, 107, 65, 109, 63, 102] #[health, attack, defense, special attack, special defense, speed]
        self.names = ["Squirtle", "water", "none", "tackle", "tailwhip", "bubble", "withdraw"]
        return (self.stats, self.names)
    
    def __getitem__ (self, key): #methods add the variables to their proper lists
        self.keylist.extend(self.stats)
        return (self.keylist)
    
    def __getitem1__ (self, key):
<<<<<<< HEAD
        self.namelist.extend(self.names)
=======
        self.namelist.extend(self.names)
        return (self.namelist)
        #for some reason all the variables appear in the same list but it still works so it's fine
>>>>>>> eae8e93c518592c063e03496cd50d53dacabafb7
