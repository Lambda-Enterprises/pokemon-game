extends Node

class_name Type

var typeName
var superEffective
var notEffective
var noEffect

func __init__(self):
	typeName = None
	superEffective = None
	notEffective = None
	noEffect = None

func setType(self, name = None, superEffective = None,
			notEffective = None, noEffect = None):
	if name:
		self.name = name
		self.superEffective = superEffective
		self.notEffective = notEffective
		self.noEffect = noEffect
	else:
		print('Empty Type Name!')

func display():
	print("""
		name = %s\n
		superEffective = %s\n
		notEffective = %s\n
		noEffect = %s
		""" % self.name, self.superEffective, 
			self.notEffective, self.noEffect)
