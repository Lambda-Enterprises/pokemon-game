extends Area2D

var anime = "neutral"
var Type = load("Type.gd")

func _ready():
	get_node("AnimationPlayer").play(anime)
