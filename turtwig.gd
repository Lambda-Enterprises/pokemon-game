extends Area2D

var Pokemon = load("Pokemon.gd")
export var anime = "turtwig"


func _ready():
	$AnimationPlayer.play(anime)

func _process(delta):
	pass
