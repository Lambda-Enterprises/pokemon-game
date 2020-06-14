extends Control


# Declare member variables here. Examples:
onready var weightHeight = $DescriptionBox/WeightHeight
onready var description = $DescriptionBox/Description
var data = Global.js.accessPokedex(Global.id)
var type_dict = {
	"Bug": 0, "Dark": 1, "Dragon": 2, "Electric": 3, "Fairy": 4, "Fighting": 5,
	"Fire": 6, "Flying": 7, "Ghost": 8, "Grass": 9, "Ground": 10, "Ice": 11,
	"Normal": 12, "Poison": 13, "Psychic": 14, "Rock": 15, "Steel": 16,
	"Water": 17, "NULL": 18
}


# Called when the node enters the scene tree for the first time.
func _ready():
	$PokeSprite.set_animation(data["name"])
	weightHeight.text = "Weight: %s\nHeight: %s" % [data["weight"], data["height"]]
	description.text = "Species: %s\n%s" % [data["species"], data["description"]]
	$Type1.frame = type_dict[data["type1"]]
	$Type2.frame = type_dict[data["type2"]]


func _on_Button_pressed():
	get_tree().change_scene("res://PokemonSelect/PokemonSelect.tscn")
