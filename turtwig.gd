extends Area2D

var anime = "neutral"

func _ready():
	get_node("AnimationPlayer").play(anime)
