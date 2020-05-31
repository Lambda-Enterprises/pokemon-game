extends Node

var type_matchup

func get_types():
	var file = File.new()
	file.open("res://data/types.json", file.READ)
	var text = file.get_as_text()
	file.close()
	
	type_matchup = JSON.parse(text).result
	#print(type_matchup)

func _ready():
	get_types()
