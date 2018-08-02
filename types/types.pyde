class Types:
    def __init__(self, typename = '', supereffective = [], noteffective = [], noeffect = []):
        self.name = typename
        self.supereffective = supereffective
        self.noteffective = noteffective
        self.noeffect = noeffect
    def typeloader (self, name):
        typedick = {
                    'normal' : MoveTypes('normal', [], ['rock', 'steel'], ['ghost']),
                    'fire' : MoveTypes('fire', ['grass', 'bug', 'ice', 'steel'], ['water', 'fire', 'dragon', 'rock', 'ground'], []),
                    'water' : MoveTypes('water', ['fire', 'rock', 'ground'], ['water', 'ice', 'dragon', 'grass', 'steel'], []),
                    'grass' : MoveTypes('grass', ['water', 'rock', 'ground'], ['grass', 'fire', 'poison', 'bug', 'ice', 'flying', 'steel'], [])
                }
        
        return(typedick[name])
    
# x = MoveTypes()
# x = x.typeloader('normal')
# print (x.name, x.supereffective, x.noteffective)
