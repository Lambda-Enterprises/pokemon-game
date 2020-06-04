class_name Type

var name: String
var superEffective: Array
var notEffective: Array
var noEffect: Array

func _init():
	self.name = ""
	self.superEffective = []
	self.notEffective = []
	self.noEffect = []

func setType(name: String = "", superEffective: Array = [],
			notEffective: Array = [], noEffect: Array = []) -> void:
	if name:
		self.name = name
		self.superEffective = superEffective
		self.notEffective = notEffective
		self.noEffect = noEffect
	else:
		print('Empty Type Name!')

func display() -> void:
	print("""
		name = %s\n
		superEffective = %s\n
		notEffective = %s\n
		noEffect = %s
		""" % self.name, self.superEffective, 
			self.notEffective, self.noEffect)
