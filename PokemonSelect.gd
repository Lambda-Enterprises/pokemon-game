extends Control


const Pokemon = preload("res://util/Pokemon.gd")
const Pokedex = preload("res://util/Pokedex.gd")


# Declare member variables here. Examples:
var js = JSONAccess.new()
var id = 1


# Called when the node enters the scene tree for the first time.
func _ready():
	randomize()
	$Name.text = $Pokemon.get_animation()
	Global.opponent.pokemon = js.accessPokemon(randi() % 10)


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if (Input.is_action_just_pressed("ui_left") or
			Input.is_action_just_pressed("ui_up")):
		id = id - 1 if id > 1 else 1
		switch_pokemon(id)
	if (Input.is_action_just_pressed("ui_right") or
			Input.is_action_just_pressed("ui_down")):
		id = id + 1 if id < 9 else 9
		switch_pokemon(id)


func _on_Button_pressed():
	get_tree().change_scene("res://BattleScene.tscn")


func switch_pokemon(id: int):
	$Pokemon.pokemon = js.accessPokemon(id)
	$Pokemon.set_animation($Pokemon.pokemon.name)
	$Name.text = $Pokemon.pokemon.name
	Global.player.pokemon = $Pokemon.pokemon
