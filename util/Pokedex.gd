extends Move
extends Type
extends Pokedex

class_name Pokedex #holds all the stats for each pokemon

func __init__(self, name = None):
	if name:
		self.id = None
		self.name = None
		self.type1 = None
		self.type2 = None

func setPokedex(self, id = None, name = None,
				type1 = None, type2 = None):
	if name:
		self.id = id
		self.name = name
		self.type1 = type1
		self.type2 = type2
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
