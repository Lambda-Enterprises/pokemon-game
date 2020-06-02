const Move = preload("res://util/Move.gd")
const Type = preload("res://util/Type.gd")

# holds all the stats for each pokemon
class Pokemon:
	func _init():
		self.id = 0
		self.name = ""
		self.type1 = Type.new()
		self.type2 = Type.new()
		self.lvl = 1
		self.hp = 1
		self.attack = 1
		self.defense = 1
		self.specialAttack = 1
		self.specialDefense = 1
		self.speed = 1
		self.move1 = Move.new()
		self.move2 = Move.new()
		self.move3 = Move.new()
		self.move4 = Move.new()
	
	func setPokemon(id = 0, name = "", type1 = Type.new(), type2 = Type.new(),
			lvl = 1, hp = 1, attack = 1, defense = 1, specialAttack = 1,
			specialDefense = 1, speed = 1, move1 = Move.new(), 
			move2 = Move.new(), move3 = Move.new(), move4 = Move.new()):
		if name != "":
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
