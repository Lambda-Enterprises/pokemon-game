extends Control


const Pokemon = preload("res://util/Pokemon.gd")
#need the button scene
const SelectButton = preload("res://PokemonSelect/SelectButton.tscn")


# Declare member variables here. Examples:
var button = [] #contains all the button data


# Called when the node enters the scene tree for the first time.
func _ready():
	"""sets a certain amount of buttons for the pokedex"""
	var data
	var icon
	for i in range(Global.numOfPokemon):
		#load Pokemon data
		data = Global.js.accessPokedex(i+1)
		#load a button instance for every Pokemon
		button.append(SelectButton.instance())
		#set name to pokemon name
		button[i].get_node("Name").set_text(data["name"])
		#set pokemon icon
		icon = load("res://img/pokemon/icons/" + data["icon"])
		button[i].get_node("PokemonIcon").set_texture(icon)
		#add child node for each button
		$ScrollBar/PokemonList.add_child(button[i])


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	#checks to see if a button was pressed to switch scenes and also change gui
	for i in range(len(button)):
		if button[i].is_hovered():
			Global.id = i+1
			$PokeSprite.set_animation(Global.js.accessPokedex(i+1)["name"])
		if button[i].is_pressed():
			get_tree().change_scene("res://PokemonSelect/PokemonData.tscn")


func _on_Button_pressed():
	randomize() #random seed initializer
	Global.player = Global.js.accessPokemon(Global.id)
	Global.opponent = Global.js.accessPokemon(randi() % 10)
	get_tree().change_scene("res://BattleScene.tscn")
