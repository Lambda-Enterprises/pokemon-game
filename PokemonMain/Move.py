class Moves:
   def __init__ (self, name = '', type = Type(), power = 0, accuracy = 0):
       self.name = name
       self.type = type
       self.power = power
       self.accuracy = accuracy
       
    def loadMove(self, name):
        typedict = {
            'normal' : MoveTypes('normal', [], ['rock', 'steel'], ['ghost']),
            'fire' : MoveTypes('fire', ['grass', 'bug', 'ice', 'steel'], ['water', 'fire', 'dragon', 'rock', 'ground'], []),
            'water' : MoveTypes('water', ['fire', 'rock', 'ground'], ['water', 'dragon', 'grass', 'steel'], []),
            'grass' : MoveTypes('grass', ['water', 'rock', 'ground'], ['grass', 'fire', 'poison', 'bug', 'ice', 'flying', 'steel'], []),
            'electric' : MoveTypes('electric', ['water', 'flying'], ['rock', 'dragon', 'steel', 'electric'], ['ground']),
            'fighting' : MoveTypes('fighting', ['normal', 'rock', 'steel', 'dark'], ['flying', 'poison', 'psychic'], ['ghost']),
            'flying' : MoveTypes('flying', ['grass', 'bug', 'fighting'], ['electric', 'ice', 'rock', 'steel'], []),
            'ground' : MoveTypes('ground', ['electric', 'rock', 'fire'], ['ice'], ['flying']),
            'rock' : MoveTypes('rock', ['bug', 'flying', 'ice', 'fire'], ['water', 'grass', 'steel', 'rock'], []),
            'psychic' : MoveTypes('psychic', ['fighting', 'poison'], ['ghost', 'bug', 'steel'], ['dark']),
            'ghost' : MoveTypes('ghost', ['ghost', 'psychic'], ['dark'], ['normal']),
            'dark' : MoveTypes('dark', ['ghost', 'psychic'], ['bug', 'fighting'], []),
            'dragon' : MoveTypes('dragon', ['dragon'], ['ice'], []),
            'steel' : MoveTypes('steel', ['rock', 'ice'], ['dragon'], []),
            'poison' : MoveTypes('poison', ['grass', 'bug'], ['rock', 'ground'], ['steel']),
            'ice' : MoveTypes('ice', ['grass', 'bug', 'flying', 'ground', 'dragon'], ['water', 'fire', 'steel'], [])
        }
        
        return(typedict[name])
    
