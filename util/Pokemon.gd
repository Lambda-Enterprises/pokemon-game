const Move = preload("res://util/Move.gd")
const Type = preload("res://util/Type.gd")

# holds all the stats for each pokemon
class_name Pokemon

var id: int
var name: String
var type1: Type
var type2: Type
var lvl: int
var hp: int
var attack: int
var defense: int
var specialAttack: int
var specialDefense: int
var speed: int
var moves: Array setget set_moves, get_moves

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
	self.moves = [
		Move.new(),
		Move.new(),
		Move.new(),
		Move.new()
	]

func get_moves():
	return moves

func set_moves(m: Array = []):
	if len(m) == 4:
		moves = m
	elif moves.empty():
		moves = [Move.new(), Move.new(), Move.new(), Move.new()]

func setPokemon(id: int = 0, name: String = "", type1: Type = Type.new(), 
		type2: Type = Type.new(), lvl: int = 1, hp: int = 1, attack: int = 1,
		defense: int = 1, specialAttack: int = 1, specialDefense: int = 1,
		speed: int = 1, move1: Move = Move.new(), move2: Move = Move.new(),
		move3: Move = Move.new(), move4: Move = Move.new()) -> void:
	if name != "":
		self.id = id
		self.name = name
		self.type1 = type1
		self.type2 = type2
		self.lvl = lvl
		self.hp = int(((2*hp*lvl)/100) + lvl + 10)
		self.attack = int(((2*attack*lvl)/100) + 5)
		self.defense = int(((2*defense*lvl)/100) + 5)
		self.specialAttack = int(((2*specialAttack*lvl)/100) + 5)
		self.specialDefense = int(((2*specialDefense*lvl)/100) + 5)
		self.speed = int(((2*speed*lvl)/100) + 5)
		self.moves = [
			move1,
			move2,
			move3,
			move4
		]
	else:
		print('Empty Pokemon Name!')

func display() -> void:
	print("""
	id = %s\n
	name = %s\n
	type1 = %s\n
	type2 = %s
	""" % self.id, self.name, 
		self.type1, self.type2)
