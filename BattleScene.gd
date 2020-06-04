extends TextureRect


# Import necessary *.gd files
const Pokemon = preload("res://util/Pokemon.gd")
const BattleEffects = preload("res://util/BattleEffects.gd")


# Declare member variables here. Examples:
var pokemonColl = []


# Called when the node enters the scene tree for the first time.
func _ready():
	$Opponent.pokemon = Global.opponent.pokemon
	$Opponent.set_animation($Opponent.pokemon.name)
	$Player.pokemon = Global.player.pokemon
	$Player.set_animation($Player.pokemon.name)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	pass
