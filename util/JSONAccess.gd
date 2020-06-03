const Move = preload("res://util/Move.gd")
const Type = preload("res://util/Type.gd")
const Pokemon = preload("res://util/Pokemon.gd")
const Pokedex = preload("res://util/Pokedex.gd")
const BattleEffects = preload("res://util/BattleEffects.gd")

class JSONAccess:
	func _init():
		var file = File.new()
		file.open("res://data/type.json", file.READ)
		self.typeData = file.get_as_text()
		file.close()
		file.open("res://data/move.json", file.READ)
		self.moveData = file.get_as_text()
		file.close()
		file.open("res://data/pokemon.json", file.READ)
		self.pokemonData = file.get_as_text()
		file.close()
		file.open("res://data/pokedex.json", file.READ)
		self.pokedexData = file.get_as_text()
		file.close()
	
	func accessType(name = ""):
		var type = Type.new()
		var data = self.typeData[name]
		if data == null:
			return type
		type.setType(name, data["supereff"], data["noteff"], 
				data["noeff"])
		return type
	
	func accessMove(name = ""):
		var move = Move.new()
		var data = self.typeData[name]
		if data == null:
			return move
		move.setMove(name, data["kind"], accessType(data["type"]),
				data["power"], data["accuracy"], data["pp"], data["range"])
		return move
	
	func accessPokemon(id = ""):
		var pokemon = Pokemon.new()
		var data1 = self.pokedexData[id]
		var data2 = self.pokemonData[id]
		if data1 == null or data2 == null:
			return pokemon
		pokemon.setPokemon(id, data1["name"], accessType(data1["type1"]),
				accessType(data1["type2"]), data2["lvl"], data2["hp"],
				data2["attack"], data2["defense"], data2["specialAttack"],
				data2["specialDefense"], data2["speed"],
				accessMove(data2["move1"]), accessMove(data2["move2"]),
				accessMove(data2["move3"]), accessMove(data2["move4"]))
		return pokemon
	
	func accessPokedex(name = ""):
		return self.pokedexData[name]
