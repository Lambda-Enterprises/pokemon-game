from Pokemon import *

class PhysicalMove: #class calculates damage value from attacks
    def __init__(self, attacker, defender, weather): #initializes variables that are given in the class
        self.attacker = attacker
        self.defender = defender
        self.weather = weather
