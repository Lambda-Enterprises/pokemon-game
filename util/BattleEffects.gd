extends Node
extends Pokemon

class_name BattleEffects

func baseDamage(self, attacker, defender):
	mod = 1 # factor that indicates more damage
	for defender in defender.type.superEffective:
		mod = mod*2
	for defender in defender.type.notEffective:
		mod = mod/2
	for defender in defender.type.noEffect:
		mod = mod*0
	dmg = ((((2*attacker.level)/5 + 2)*attacker.power*
	(attacker.attack/defender.defense))/defender.level + 2)*mod
	return (dmg)

func calcStatChange(self, attacker, defender):
	return 0 # to do

func statusCondition(self, name):
	status = {
		"asleep": 25,
		"burned": 25,
		"frozen": 25,
		"paralyzed": 25,
		"poisoned": 25
	}
	return status[name] # to do
