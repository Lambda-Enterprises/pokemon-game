extends Control


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	$Name.text = $Pokemon.get_animation()


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


# Need to implement button here
func _on_click():
	get_tree().change_scene("res://BattleScene.tscn")
