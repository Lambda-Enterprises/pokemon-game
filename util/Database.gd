import configparser
import pymysql
from sys import path
path.append("./../EntityClasses")
import Move
import Type
import Pokemon
import Pokedex
import BattleEffects

class Database:
	def __init__(self):
		config = configparser.ConfigParser()
		config.read('../../DB_Config/Database.ini')
		self.con = pymysql.connect(
			config['Oracle_SQL'].get('host'),
			config['Oracle_SQL'].get('user'),
			config['Oracle_SQL'].get('pass'),
			config['Oracle_SQL'].get('name'))
		self.cur = self.con.cursor()
	
	def accessMove(self, name):
		move = Move()
		try:
			self.cur.execute("""SELECT * FROM MOVE
							WHERE NAME = '%s'""" % name)
			result = self.cur.fetchone() # change this later
			if result:
				move.name = result[0]
				move.kind = result[1]
				move.type = accessType(result[2])
				move.power = int(result[3])
				move.accuracy = int(result[4])
				move.pp = int(result[5])
				move.range = result[6]
			else:
				raise Exception('Invalid Move!')
		except DatabaseError as errDB:
			print(str(errDB))
		except Exception as err:
			print(str(err))
		return move
	
	def accessPokemon(self, name):
		pokemon = Pokemon()
		try:
			self.cur.execute("""SELECT * FROM POKEMON
							WHERE NAME = '%s'""" % name)
			result = self.cur.fetchone() # change this later
			if result:
				pokemon.id = self.data[0]
				pokemon.name = self.data[1]
				pokemon.type1 = accessType(self.data[2])
				pokemon.type2 = accessType(self.data[3])
			else:
				raise Exception('Invalid Pokemon!')
		except DatabaseError as errDB:
			print(str(errDB))
		except Exception as err:
			print(str(err))
		return pokemon
	
	def accessPokedex(self, name):
		pokedex = Pokedex()
		try:
			self.cur.execute("""SELECT * FROM POKEMON
							WHERE NAME = '%s'""" % name)
			result = self.cur.fetchone() # change this later
			if result:
				pokedex = result[0]
				pokedex.name = result[1]
				pokedex.type1 = accessType(result[2])
				pokedex.type2 = accessType(result[3])
			else:
				raise Exception('Invalid Pokemon!')
		except DatabaseError as errDB:
			print(str(errDB))
		except Exception as err:
			print(str(err))
		return pokedex
	
	def accessType(self, name):
		type = Type()
		try:
			self.cur.execute("""SELECT * FROM TYPE
							WHERE NAME = '%s'""" % name)
			result = self.cur.fetchone() # change this later
			if result:
				type.name = result[0]
				type.superEffective = result[1]
				type.notEffective = result[2]
				type.noEffect = result[3]
			else:
				raise Exception('Invalid Type!')
		except DatabaseError as errDB:
			print(str(errDB))
		except Exception as err:
			print(str(err))
		return type
	
	def closeCon(self):
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
