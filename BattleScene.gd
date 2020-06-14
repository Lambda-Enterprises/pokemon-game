extends TextureRect


# Import necessary *.gd files
const BattleEffects = preload("res://util/BattleEffects.gd")
onready var move_buttons = [$Move1, $Move2, $Move3, $Move4]

# Declare member variables here. Examples:
var turn = ["player", 0]


# Called when the node enters the scene tree for the first time.
func _ready():
#	for i in range(len(move_buttons)):
#		move_buttons[i].connect("pressed", self, "selected")
	for i in range(len(move_buttons)):
		move_buttons[i].text = Global.player.moves[i].name
		
	$Opponent.set_animation(Global.opponent.name)
	$Player.set_animation(Global.player.name)
	if Global.player.speed >= Global.opponent.speed:
		turn[0] = "player"
	else:
		turn[0] = "opponent"


# Called every frame. 'delta' is the elapsed time since the previous frame.
# warning-ignore:unused_argument
func _process(delta):
	randomize()
	
		
				
	if turn[0] == "opponent" and turn[1] != 2:
		BattleEffects.baseDamage(Global.opponent, Global.player, Global.opponent.moves[randi() % 3])
		turn[1] += 1
		turn[0] = "player"
		#print(turn)
	if turn[1] == 2:
		turn[1] = 0
		print("player hp:" + str(Global.player.hp))
		print("opponent hp:" + str(Global.opponent.hp))


func _on_Move1_pressed():
	if turn[0] == "player" and turn[1] != 2:
		BattleEffects.baseDamage(Global.player, Global.opponent, Global.player.moves[0])
		turn[1] += 1
		turn[0] = "opponent"


func _on_Move2_pressed():
	if turn[0] == "player" and turn[1] != 2:
		BattleEffects.baseDamage(Global.player, Global.opponent, Global.player.moves[1])
		turn[1] += 1
		turn[0] = "opponent"



func _on_Move3_pressed():
	if turn[0] == "player" and turn[1] != 2:
		BattleEffects.baseDamage(Global.player, Global.opponent, Global.player.moves[2])
		turn[1] += 1
		turn[0] = "opponent"


func _on_Move4_pressed():
	if turn[0] == "player" and turn[1] != 2:
		BattleEffects.baseDamage(Global.player, Global.opponent, Global.player.moves[3])
		turn[1] += 1
		turn[0] = "opponent"
