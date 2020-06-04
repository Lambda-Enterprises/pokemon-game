extends Control


const Pokemon = preload("res://util/Pokemon.gd")
const Pokedex = preload("res://util/Pokedex.gd")


# Declare member variables here. Examples:
var js = JSONAccess.new()


# Called when the node enters the scene tree for the first time.
func _ready():
	$Name.text = $Pokemon.get_animation()


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if Input.is_action_pressed("ui_left") or Input.is_action_pressed("ui_up"):
		$Pokemon.pokemon = js.accessPokemon(1)
		$Pokemon.set_animation($Pokemon.pokemon.name)
		$Name.text = $Pokemon.pokemon.name
		Global.player.pokemon = $Pokemon.pokemon
	if Input.is_action_pressed("ui_right") or Input.is_action_pressed("ui_down"):
		$Pokemon.pokemon = js.accessPokemon(4)
		$Pokemon.set_animation($Pokemon.pokemon.name)
		$Name.text = $Pokemon.pokemon.name
		Global.player.pokemon = $Pokemon.pokemon

func _on_Button_pressed():
	get_tree().change_scene("res://BattleScene.tscn")
