extends Node


const Move = preload("res://util/Move.gd")
const Type = preload("res://util/Type.gd")
var Pokemon = load("res://util/Pokemon.gd")

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

func accessType(name: String = "") -> Type:
	var type = Type.new()
	var data = self.typeData[name]
	if data == null:
		return type
	var supereff = [] if data["supereff"] == null else data["supereff"].split(",")
	var noteff = [] if data["noteff"] == null else data["noteff"].split(",")
	var noeff = [] if data["noeff"] == null else data["noeff"].split(",")
	type.setType(name, supereff, noteff, noeff)
	return type

func accessMove(name: String = "") -> Move:
	var move = Move.new()
	if name == "NULL":
		return move
	var data = self.moveData[name]
	move.setMove(name, data["kind"], accessType(data["type"]),
			data["power"], data["accuracy"], data["pp"], data["range"])
	return move

func accessPokemon(id: int = 1):
	var pokemon = Pokemon.new()
	if id < 1 or id > Global.numOfPokemon:
		return Pokemon
	var data1 = self.pokedexData[str(id)]
	var data2 = self.pokemonData[str(id)][0]
	var type2 = null if data1["type2"] == "NULL" else accessType(data1["type2"])
	pokemon.setPokemon(id, data1["name"], accessType(data1["type1"]),
			type2, data2["lvl"], data1["hp"],
			data1["atk"], data1["def"], data1["spatk"],
			data1["spdef"], data1["speed"],
			accessMove(data2["move1"]), accessMove(data2["move2"]),
			accessMove(data2["move3"]), accessMove(data2["move4"]))
	return pokemon

func accessPokedex(id: int = 0) -> JSONParseResult:
	if id == 0:
		return self.pokedexData
	return self.pokedexData[str(id)]
