import json

class Type:
    def __init__(self, name = None):
        try:
            with open('Data/Type.json', 'r') as file:
                typeDict = json.loads(file.read())
                file.close()
            type = typeDict[name]
            self.name = name
            self.superEffective = type['superEffective']
            self.notEffective = type['notEffective']
            self.noEffect = type['noEffect']
        except:
            print('Invalid Tpye!')
    
    def setType(self, name):
        with open('Data/Type.json', 'r') as file:
            typeDict = json.loads(file.read())
            file.close()
        type = typeDict[name]
        self.name = type[name]
        self.superEffective = type['superEffective']
        self.notEffective = type['notEffective']
        self.noEffect = type['noEffect']
