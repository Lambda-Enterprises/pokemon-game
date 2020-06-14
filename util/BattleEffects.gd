var Pokemon = load("res://util/Pokemon.gd")

class_name BattleEffects

static func baseDamage(attacker, defender, move):
	if !(attacker is Pokemon) or !(defender is Pokemon):
		print("Invalid datatype for attacker and/or defender!")
		return null
	var mod = 1.0 # factor that indicates more damage
	for m in move.type.superEffective:
		if m == defender.type1.name:
			mod = mod*2
		if defender.type2 != null and m == defender.type2.name:
			mod = mod*2
	for m in move.type.notEffective:
		if m == defender.type1.name:
			mod = mod/2
		if defender.type2 != null and m == defender.type2.name:
			mod = mod/2
	for m in move.type.noEffect:
		if m == defender.type1.name:
			mod = 0
		if defender.type2 != null and m == defender.type2.name:
			mod = 0
	
	var dmg = int(((((2*attacker.lvl)/5 + 2)*move.power*
	(attacker.attack/defender.defense))/50 + 2)*mod)
	if move.kind == "Status":
		dmg = 0
	defender.hp -= dmg

static func calcStatChange(attacker, defender):
	if !(attacker is Pokemon) or !(defender is Pokemon):
		print("Invalid datatype for attacker and/or defender!")
		return null
	return 0 # to do

static func burned(pkmn): #incomplete
	if !(pkmn is Pokemon):
		print("Invalid datatype for pkmn!")
		return null
	var original_atk = pkmn.atk
	var burn_atk = pkmn.atk/2
	if pkmn.status == "burned":
		pkmn.atk = burn_atk
		pkmn.hp -= int(pkmn.hp/16)
	else:
		pkmn.atk = original_atk

static func paralysis(pkmn): #incomplete
	if !(pkmn is Pokemon):
		print("Invalid datatype for pkmn!")
		return null
	randomize()
	var orignal_spe = pkmn.spe
	var para_spe = pkmn.spe / 2
	if pkmn.status == "paralysis":
		#0-1 random int number
		var paralyzed = randi()%1
		pkmn.spe = para_spe
	else:
		pkmn.spe = orignal_spe

static func confusion(pkmn, move): #incomplete
	if !(pkmn is Pokemon):
		print("Invalid datatype for pkmn!")
		return null
	randomize()
	var hit = randi()%1
	var snapout = randi()%2
	if snapout == 2:
		pkmn.status = ""
	elif pkmn.status == "confusion" and hit == 1:
		#0-1 random int number
		#hits themselves
		baseDamage(pkmn, pkmn, move)

static func poisoned(pkmn): #incomplete
	if !(pkmn is Pokemon):
		print("Invalid datatype for pkmn!")
		return null
	pkmn.hp -= int(pkmn.hp/16)

static func badly_poisoned(pkmn): #incomplete
	if !(pkmn is Pokemon):
		print("Invalid datatype for pkmn!")
		return null
	var dmg_ratio = 1
	pkmn.hp -= int((pkmn.hp*dmg_ratio)/16)

static func statusCondition(name: String):
	var status = {
		"asleep": 25,
		"burned": 25,
		"frozen": 25,
		"paralyzed": 25,
		"poisoned": 25
	}
	return status[name] # to do
