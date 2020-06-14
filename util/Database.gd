#extends configparser
#extends pymysql
#from sys import path
#path.append("./../EntityClasses")
const Move = preload("res://util/Move.gd")
const Type = preload("res://util/Type.gd")
const Pokemon = preload("res://util/Pokemon.gd")
const BattleEffects = preload("res://util/BattleEffects.gd")

class_name Database

func _init():
#	var config = configparser.ConfigParser()
#	config.read('../../DB_Config/Database.ini')
#	self.con = pymysql.connect(
#		config['Oracle_SQL'].get('host'),
#		config['Oracle_SQL'].get('user'),
#		config['Oracle_SQL'].get('pass'),
#		config['Oracle_SQL'].get('name'))
	self.cur = self.con.cursor()

func accessMove(name):
	var move = Move.new()
#	try:
#		self.cur.execute("""SELECT * FROM MOVE
#						WHERE NAME = '%s'""" % name)
#		result = self.cur.fetchone() # change this later
#		if result:
#			move.name = result[0]
#			move.kind = result[1]
#			move.type = accessType(result[2])
#			move.power = int(result[3])
#			move.accuracy = int(result[4])
#			move.pp = int(result[5])
#			move.range = result[6]
#		else:
#			raise Exception('Invalid Move!')
#	except DatabaseError as errDB:
#		print(str(errDB))
#	except Exception as err:
#		print(str(err))
	return move

func accessPokemon(name):
	var pokemon = Pokemon.new()
#	try:
#		self.cur.execute("""SELECT * FROM POKEMON
#						WHERE NAME = '%s'""" % name)
#		result = self.cur.fetchone() # change this later
#		if result:
#			pokemon.id = self.data[0]
#			pokemon.name = self.data[1]
#			pokemon.type1 = accessType(self.data[2])
#			pokemon.type2 = accessType(self.data[3])
#		else:
#			raise Exception('Invalid Pokemon!')
#	except DatabaseError as errDB:
#		print(str(errDB))
#	except Exception as err:
#		print(str(err))
	return pokemon

func accessType(name):
	var type = Type.new()
#	try:
#		self.cur.execute("""SELECT * FROM TYPE
#						WHERE NAME = '%s'""" % name)
#		result = self.cur.fetchone() # change this later
#		if result:
#			type.name = result[0]
#			type.superEffective = result[1]
#			type.notEffective = result[2]
#			type.noEffect = result[3]
#		else:
#			raise Exception('Invalid Type!')
#	except DatabaseError as errDB:
#		print(str(errDB))
#	except Exception as err:
#		print(str(err))
	return type

func closeCon():
	self.cur.close()
	self.con.close()
"""db = Database()
type = db.accessType('Normal')
type.display()
poke = db.accessPokemon('Bulbasaur')
poke.display()
move = db.accessMove('Tackle')
move.display()
pode = db.accessPokedex('Bulbasaur')
pode.display()"""
