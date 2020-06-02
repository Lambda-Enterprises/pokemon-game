extends Area2D

var Pokemon = load("Pokemon.gd")
var anime = "chimchar"

func _ready():
	$AnimationPlayer.play(anime)
