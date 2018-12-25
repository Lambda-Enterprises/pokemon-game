from Pokemon import *

class BattleEffects:
    def calcDamage(self, attacker, defender):
        mod = 1 #factor that indicates more damage
        for defender in self.type.superEffective:
            mod = mod * 2
        for defender in self.type.notEffective:
            mod = mod / 2
        for defender in self.type.noEffect:
            mod = mod * 0
        dmg = ((((2 * 50)/5 + 2) * self.power * (atk/defn))/50 + 2) * mod
        
        return (dmg)
    
    def calcStatChange(self, attacker, defender):
        return 0 #to do
    
    def statusCondition(self, name):
        status = {
            "asleep": 25
            "burned": 25,
            "frozen": 25,
            "paralyzed": 25,
            "poisoned": 25
        }
        return status[name] #to do
    