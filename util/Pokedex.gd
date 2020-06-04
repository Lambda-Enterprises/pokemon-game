const Type = preload("res://util/Type.gd")

# holds all the stats for each pokemon
class_name Pokedex

var id: int
var name: String
var type1: Type
var type2: Type

func _init():
	self.id = 0
	self.name = ""
	self.type1 = Type.new()
	self.type2 = Type.new()

func setPokedex(id: int = 0, name: String = "",
				type1: Type = Type.new(), type2: Type = Type.new()) -> void:
	if name:
		self.id = id
		self.name = name
		self.type1 = type1
		self.type2 = type2
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
