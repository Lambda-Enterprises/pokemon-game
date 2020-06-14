extends TextureRect


# Import necessary *.gd files
const BattleEffects = preload("res://util/BattleEffects.gd")


# Declare member variables here. Examples:
var turn = ["player", 0]


# Called when the node enters the scene tree for the first time.
func _ready():
	$Opponent.set_animation(Global.opponent.name)
	$Player.set_animation(Global.player.name)
	if Global.player.speed >= Global.opponent.speed:
		turn[0] = "player"
	else:
		turn[0] = "opponent"


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if turn[0] == "player":
		pass
		#print(turn)
	else:
		pass
		#print(turn)
