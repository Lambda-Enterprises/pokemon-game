const Type = preload("res://util/Type.gd")

# holds all the stats for each pokemon
class Pokedex:
	func _init():
		self.id = ""
		self.name = ""
		self.type1 = Type.new()
		self.type2 = Type.new()
	
	func setPokedex(id = 0, name = "",
					type1 = Type.new(), type2 = Type.new()):
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
