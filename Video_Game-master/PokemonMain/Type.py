class Type:
    def __init__(self, typeName = '', superEffective = [], notEffective = [], noEffect = []):
        self.name = typeName
        self.superEffective = superEffective
        self.notEffective = notEffective
        self.noEffect = noEffect
    def loadType (self, name):
        typeDict = {
            'normal' : Types('normal', [], ['rock', 'steel'], ['ghost']),
            'fire' : Types('fire', ['grass', 'bug', 'ice', 'steel'], ['water', 'fire', 'dragon', 'rock', 'ground'], []),
            'water' : Types('water', ['fire', 'rock', 'ground'], ['water', 'dragon', 'grass', 'steel'], []),
            'grass' : Types('grass', ['water', 'rock', 'ground'], ['grass', 'fire', 'poison', 'bug', 'ice', 'flying', 'steel'], []),
            'electric' : Types('electric', ['water', 'flying'], ['rock', 'dragon', 'steel', 'electric'], ['ground']),
            'fighting' : Types('fighting', ['normal', 'rock', 'steel', 'dark'], ['flying', 'poison', 'psychic'], ['ghost']),
            'flying' : Types('flying', ['grass', 'bug', 'fighting'], ['electric', 'ice', 'rock', 'steel'], []),
            'ground' : Types('ground', ['electric', 'rock', 'fire'], ['ice'], ['flying']),
            'rock' : Types('rock', ['bug', 'flying', 'ice', 'fire'], ['water', 'grass', 'steel', 'rock'], []),
            'psychic' : Types('psychic', ['fighting', 'poison'], ['ghost', 'bug', 'steel'], ['dark']),
            'ghost' : Types('ghost', ['ghost', 'psychic'], ['dark'], ['normal']),
            'dark' : Types('dark', ['ghost', 'psychic'], ['bug', 'fighting'], []),
            'dragon' : Types('dragon', ['dragon'], ['ice'], []),
            'steel' : Types('steel', ['rock', 'ice'], ['dragon'], []),
            'poison' : Types('poison', ['grass', 'bug'], ['rock', 'ground'], ['steel']),
            'ice' : Types('ice', ['grass', 'bug', 'flying', 'ground', 'dragon'], ['water', 'fire', 'steel'], [])
        }
        
        return(typedict[name])

"""
x = MoveTypes()
x = x.loadType('normal')
print (x.name, x.supereffective, x.noteffective)
"""
