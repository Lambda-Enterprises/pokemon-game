extends Move
extends Type
extends Pokedex

class_name Pokemon # holds all the stats for each pokemon
	
func __init__(self):
	self.id = None
	self.name = None
	self.type1 = None
	self.type2 = None
	self.lvl = None
	self.hp = None
	self.attack = None
	self.defense = None
	self.specialAttack = None
	self.specialDefense = None
	self.speed = None
	self.move1 = None
	self.move2 = None
	self.move3 = None
	self.move4 = None

func setPokemon(self, id = None, name = None,
				type1 = None, type2 = None):
	if name:
		self.id = id
		self.name = name
		self.type1 = type1
		self.type2 = type2
		self.lvl = lvl
		self.hp = hp
		self.attack = attack
		self.defense = defense
		self.specialAttack = specialAttack
		self.specialDefense = specialDefense
		self.speed = speed
		self.move1 = move1
		self.move2 = move2
		self.move3 = move3
		self.move4 = move4
	else:
		print('Empty Pokemon Name!')

func display():
	print("""
	id = %s\n
	name = %s\n
	type1 = %s\n
	type2 = %s
	""" % self.id, self.name, 
		self.type1, self.type2)
