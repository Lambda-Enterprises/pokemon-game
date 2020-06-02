class Type:
	func _init():
		self.typeName = ""
		self.superEffective = []
		self.notEffective = []
		self.noEffect = []
	
	func setType(name = "", superEffective = [],
				notEffective = [], noEffect = []):
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
