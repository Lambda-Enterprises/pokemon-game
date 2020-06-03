const Pokemon = preload("res://util/Pokemon.gd")

class BattleEffects:
	func baseDamage(attacker, defender):
		var mod = 1 # factor that indicates more damage
		for defender in defender.type.superEffective:
			mod = mod*2
		for defender in defender.type.notEffective:
			mod = mod/2
		for defender in defender.type.noEffect:
			mod = mod*0
		var dmg = ((((2*attacker.level)/5 + 2)*attacker.power*
		(attacker.attack/defender.defense))/defender.level + 2)*mod
		return (dmg)
	
	func calcStatChange(attacker, defender):
		return 0 # to do
	
	func burned(pkmn): #incomplete
		var original_atk = pkmn.atk
		var burn_atk = pkmn.atk/2
		if pkmn.status == "burned":
			pkmn.atk = burn_atk
			pkmn.hp -= int(pkmn.hp/16)
		else:
			pkmn.atk = original_atk
		
	func paralysis(pkmn): #incomplete
		randomize()
		var orignal_spe = pkmn.spe
		var para_spe = pkmn.spe / 2
		if pkmn.status == "paralysis":
			#0-1 random int number
			var paralyzed = randi()%1
			pkmn.spe = para_spe
		else:
			pkmn.spe = orignal_spe
	
	func confusion(pkmn): #incomplete
		randomize()
		var hit = randi()%1
		var snapout = randi()%2
		if snapout == 2:
			pkmn.status = ""
		elif pkmn.status == "confusion" and hit == 1:
			#0-1 random int number
			#hits themselves
			self.baseDamage(pkmn, pkmn)
		
	func poisoned(pkmn): #incomplete
		pkmn.hp -= int(pkmn.hp/16)
		
	func badly_poisoned(pkmn): #incomplete
		var dmg_ratio = 1
		pkmn.hp -= int((pkmn.hp*dmg_ratio)/16)
	
	func statusCondition(name):
		var status = {
			"asleep": 25,
			"burned": 25,
			"frozen": 25,
			"paralyzed": 25,
			"poisoned": 25
		}
		return status[name] # to do
