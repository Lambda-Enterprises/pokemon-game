extends AnimatedSprite


const JSONAccess = preload("res://util/JSONAccess.gd")
const Pokemon = preload("res://util/Pokemon.gd")


# Declare member variables here. Examples:
var js = JSONAccess.new()
var pokemon = js.accessPokemon(1)


# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
