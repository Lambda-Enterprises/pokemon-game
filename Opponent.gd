extends AnimatedSprite


const JSONAccess = preload("res://util/JSONAccess.gd")
const Pokemon = preload("res://util/Pokemon.gd")


# Declare member variables here. Examples:
export var pokemonName = ""
var pokemon = JSONAccess.accessPokemon(1)


# Called when the node enters the scene tree for the first time.
func _ready():
	pass


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
