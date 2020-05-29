extends Type

class_name Move

	def __init__(self):
		self.name = None
		self.kind = None
		self.type = None
		self.power = None
		self.accuracy = None
		self.pp = None
		self.range = None
	
	def setMove(self, name = None, kind = None, type = None, 
				power = None, accuracy = None, pp = None, range = None):
		if name:
			self.name = name
			self.kind = kind
			self.type = type
			self.power = power
			self.accuracy = accuracy
			self.pp = pp
			self.range = range
		else:
			print('Empty Move Name!')
	
	def display():
		print("""
			name = %s\n
			kind = %s\n
			type = %s\n
			power = %s\n
			accuracy = %s\n
			pp = %s\n
			range = %s
			""" % self.name, self.kind, self.type,
			self.power, self.accuracy, self.pp, self.range)
