const Move = preload("res://util/Move.gd")
const Type = preload("res://util/Type.gd")
const Pokemon = preload("res://util/Pokemon.gd")
const Pokedex = preload("res://util/Pokedex.gd")

class_name JSONAccess

var typeData
var moveData
var pokemonData
var pokedexData

func _init():
	var file = File.new()
	file.open("res://data/type.json", file.READ)
	self.typeData = parse_json(file.get_as_text()) as Dictionary
	file.close()
	file.open("res://data/move.json", file.READ)
	self.moveData = parse_json(file.get_as_text()) as Dictionary
	file.close()
	file.open("res://data/pokemon.json", file.READ)
	self.pokemonData = parse_json(file.get_as_text()) as Dictionary
	file.close()
	file.open("res://data/pokedex.json", file.READ)
	self.pokedexData = parse_json(file.get_as_text()) as Dictionary
	file.close()

func accessType(name: String = ""):
	var type = Type.new()
	var data = self.typeData[name]
	if data == null:
		return type
	var supereff = [] if data["supereff"] == null else data["supereff"].split(",")
	var noteff = [] if data["noteff"] == null else data["noteff"].split(",")
	var noeff = [] if data["noeff"] == null else data["noeff"].split(",")
	type.setType(name, supereff, noteff, noeff)
	return type

func accessMove(name: String = ""):
	var move = Move.new()
	var data = self.moveData[name]
	if data == null:
		return move
	move.setMove(name, data["kind"], accessType(data["type"]),
			data["power"], data["accuracy"], data["pp"], data["range"])
	return move

func accessPokemon(id: int = 0):
	var pokemon = Pokemon.new()
	var data1 = self.pokedexData[str(id)]
	var data2 = self.pokemonData[str(id)]
	if data1 == null or data2 == null:
		return pokemon
	pokemon.setPokemon(id, data1["name"], accessType(data1["type1"]),
			accessType(data1["type2"]), data2["lvl"], data2["hp"],
			data2["attack"], data2["defense"], data2["special_attack"],
			data2["special_defense"], data2["speed"],
			accessMove(data2["move1"]), accessMove(data2["move2"]),
			accessMove(data2["move3"]), accessMove(data2["move4"]))
	return pokemon

func accessPokedex(name: String = ""):
	return self.pokedexData[name]
