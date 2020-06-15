extends TextureRect


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	if Global.win == false:
		set_texture(load("res://img/fail.png"))


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_Button_pressed():
	Global.id = 1
	Global.win = false
	get_tree().change_scene("res://PokemonSelect/PokemonSelect.tscn")
