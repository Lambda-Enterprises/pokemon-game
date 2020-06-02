const Type = preload("Type.gd")

class Move:
	func _init():
		self.name = ""
		self.kind = ""
		self.type = Type.new()
		self.power = 0
		self.accuracy = 0
		self.pp = 0
		self.m_range = 0
	
	func setMove(name = "", kind = "", type = Type.new(), 
				power = 0, accuracy = 0, pp = 0, m_range = 0):
		if name:
			self.name = name
			self.kind = kind
			self.type = type
			self.power = power
			self.accuracy = accuracy
			self.pp = pp
			self.m_range = m_range
		else:
			print('Empty Move Name!')
	
	func display():
		print("""
			name = %s\n
			kind = %s\n
			type = %s\n
			power = %s\n
			accuracy = %s\n
			pp = %s\n
			range = %s
			""" % self.name, self.kind, self.type,
			self.power, self.accuracy, self.pp, self.m_range)
