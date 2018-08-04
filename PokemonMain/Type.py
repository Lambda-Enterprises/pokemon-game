class Type:
    def __init__(self, typeName = '', superEffective = [], notEffective = [], noEffect = []):
        self.name = typeName
        self.superEffective = superEffective
        self.notEffective = notEffective
        self.noEffect = noEffect
    
    @staticmethod
    def loadType (name):
        typeDict = {
            'normal': Type('normal', [], ['rock', 'steel'], ['ghost']),
            'fire': Type('fire', ['grass', 'bug', 'ice', 'steel'], ['water', 'fire', 'dragon', 'rock', 'ground'], []),
            'water': Type('water', ['fire', 'rock', 'ground'], ['water', 'dragon', 'grass', 'steel'], []),
            'grass': Type('grass', ['water', 'rock', 'ground'], ['grass', 'fire', 'poison', 'bug', 'ice', 'flying', 'steel'], []),
            'electric': Type('electric', ['water', 'flying'], ['rock', 'dragon', 'steel', 'electric'], ['ground']),
            'fighting': Type('fighting', ['normal', 'rock', 'steel', 'dark'], ['flying', 'poison', 'psychic'], ['ghost']),
            'flying': Type('flying', ['grass', 'bug', 'fighting'], ['electric', 'ice', 'rock', 'steel'], []),
            'ground': Type('ground', ['electric', 'rock', 'fire'], ['ice'], ['flying']),
            'rock': Type('rock', ['bug', 'flying', 'ice', 'fire'], ['water', 'grass', 'steel', 'rock'], []),
            'psychic': Type('psychic', ['fighting', 'poison'], ['ghost', 'bug', 'steel'], ['dark']),
            'ghost': Type('ghost', ['ghost', 'psychic'], ['dark'], ['normal']),
            'dark': Type('dark', ['ghost', 'psychic'], ['bug', 'fighting'], []),
            'dragon': Type('dragon', ['dragon'], ['ice'], []),
            'steel': Type('steel', ['rock', 'ice'], ['dragon'], []),
            'poison': Type('poison', ['grass', 'bug'], ['rock', 'ground'], ['steel']),
            'ice': Type('ice', ['grass', 'bug', 'flying', 'ground', 'dragon'], ['water', 'fire', 'steel'], [])
        }
        
        return(typeDict[name])

"""
x = Type.loadType('normal')
print (x.name, x.superEffective, x.notEffective)
"""
