extends Polygon2D

# Need this script in order to draw on top of the root node
#center = 292, 240
var data = Global.js.accessPokedex(Global.id)
var points = [
	Vector2(292, 240 - data["hp"]*1.6), #hp
	Vector2(292 + data["atk"]*1.5, 240 - data["atk"]/1.2), #atk
	Vector2(292 + data["def"]*1.5, 240 + data["def"]/1.2), #def
	Vector2(292, 240 + data["speed"]*1.7), #speed
	Vector2(292 - data["spatk"]*1.5, 240 + data["spatk"]/1.2), #spdef
	Vector2(292 - data["spdef"]*1.5, 240 - data["spdef"]/1.2) #spatk
]

func _draw():
	for i in range(-1, len(points)-1):
		draw_line(points[i], points[i+1], Color(225, 0, 225), 2.0)
