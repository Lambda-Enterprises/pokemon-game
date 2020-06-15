extends TextureRect


# Import necessary *.gd files
const BattleEffects = preload("res://util/BattleEffects.gd")
onready var move_buttons = [$Move1, $Move2, $Move3, $Move4]

# Declare member variables here. Examples:
var turn = ["player", 0]

var playertotal = Global.player.hp
var opponenttotal = Global.opponent.hp


# Called when the node enters the scene tree for the first time.
func _ready():
#	for i in range(len(move_buttons)):
#		move_buttons[i].connect("pressed", self, "selected")
	for i in range(len(move_buttons)):
		move_buttons[i].text = Global.player.moves[i].name
	$PlayerBox/PlayerLvl.text = str(Global.player.lvl)
	$PlayerBox/PlayerName.text = Global.player.name
	$OpponentBox/OpponentLvl.text = str(Global.opponent.lvl)
	$OpponentBox/OpponentName.text = Global.opponent.name
	
	$Opponent.set_animation(Global.opponent.name)
	$Player.set_animation(Global.player.name)
	if Global.player.speed >= Global.opponent.speed:
		turn[0] = "player"
	else:
		turn[0] = "opponent"
	print("player hp:" + str(Global.player.hp))
	print("opponent hp:" + str(Global.opponent.hp))


# Called every frame. 'delta' is the elapsed time since the previous frame.
# warning-ignore:unused_argument
func _process(delta):
	randomize()
	if turn[0] == "opponent" and turn[1] != 2:
		var move_num = randi()%3
		BattleEffects.baseDamage(Global.opponent, Global.player, Global.opponent.moves[move_num])
		if Global.player.hp <= 0:
			get_tree().change_scene("res://End.tscn")
		print(Global.opponent.moves[move_num].name)
		$PlayerHealthBar.value = (float(100/playertotal*Global.player.hp))
		turn[1] += 1
		turn[0] = "player"
		
	if turn[1] == 2:
		turn[1] = 0
		print("player hp:" + str(Global.player.hp))
		print("opponent hp:" + str(Global.opponent.hp))


func _on_Move1_pressed():
	if turn[0] == "player" and turn[1] != 2:
		BattleEffects.baseDamage(Global.player, Global.opponent, Global.player.moves[0])
		if Global.opponent.hp <= 0:
			Global.win = true
			get_tree().change_scene("res://End.tscn")
		print(Global.player.moves[0].name)
		$OpponentHealthBar.value = (float(100/opponenttotal*Global.opponent.hp))
		turn[1] += 1
		turn[0] = "opponent"

func _on_Move2_pressed():
	if turn[0] == "player" and turn[1] != 2:
		BattleEffects.baseDamage(Global.player, Global.opponent, Global.player.moves[1])
		if Global.opponent.hp <= 0:
			Global.win = true
			get_tree().change_scene("res://End.tscn")
		print(Global.player.moves[1].name)
		$OpponentHealthBar.value = (float(100/opponenttotal*Global.opponent.hp))
		turn[1] += 1
		turn[0] = "opponent"


func _on_Move3_pressed():
	if turn[0] == "player" and turn[1] != 2:
		BattleEffects.baseDamage(Global.player, Global.opponent, Global.player.moves[2])
		if Global.opponent.hp <= 0:
			Global.win = true
			get_tree().change_scene("res://End.tscn")
		print(Global.player.moves[2].name)
		$OpponentHealthBar.value = (float(100/opponenttotal*Global.opponent.hp))
		turn[1] += 1
		turn[0] = "opponent"


func _on_Move4_pressed():
	if turn[0] == "player" and turn[1] != 2:
		BattleEffects.baseDamage(Global.player, Global.opponent, Global.player.moves[3])
		if Global.opponent.hp <= 0:
			Global.win = true
			get_tree().change_scene("res://End.tscn")
		print(Global.player.moves[3].name)
		$OpponentHealthBar.value = (float(100/opponenttotal*Global.opponent.hp))
		turn[1] += 1
		turn[0] = "opponent"
