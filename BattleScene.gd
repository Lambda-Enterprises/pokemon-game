extends TextureRect


# Import necessary *.gd files
const BattleEffects = preload("res://util/BattleEffects.gd")

#export (NodePath) var Move1
#export (NodePath) var Move2
#export (NodePath) var Move3
#export (NodePath) var Move4




onready var move_buttons = [$Move1, $Move2, $Move3, $Move4]
# Declare member variables here. Examples:
var turn = ["player", 0]


# Called when the node enters the scene tree for the first time.
func _ready():
#	for i in range(len(move_buttons)):
#		move_buttons[i].connect("pressed", self, "selected")
	for i in range(len(move_buttons)):
		move_buttons[i].text = Global.player.move1.name
		
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
		
