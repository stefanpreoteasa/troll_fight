#Player and Troll classes defined here

import random
import time

def melee_dmgroll():
	return random.randrange(0, 20)

def magic_dmgroll():
	return random.randrange(5, 25)

def dodge_roll():
	return random.randrange(0, 50)

class Warrior:
	def __init__(self, name):
		self.name = name
		self.type = "Warrior"
		self.hitpoints = 100
		self.dodge = 80

	def slash(self):
		base_damage = 10
		print "You slash with your two-hander..."
		return base_damage + melee_dmgroll()

	def thrust(self):
		base_damage = 15
		print "You attempt to thrust the whole two-hander into the troll..."
		time.sleep(0.5)
		if (dodge_roll() + self.dodge)>100:
			"You hit the troll for a lot of damage!"
			return base_damage + melee_dmgroll()
		else:
			print "You miss..."
			return 0

	def dodge_attack(self):
		print "You attempt to dodge the attack..."
		time.sleep(0.2)
		if (self.dodge + dodge_roll())>90:
			print "You dodge his obnoxious non-arguments with your brilliant argumentative skills!"
			return True
		else:
			return False

	def action(self):
		print "Attack:"
		print "1. Slash - a basic melee attack. Medium damage."
		print "2. Thrust - a daring attept to stab the bastards. High damage. Chance to miss."
		
		action = False
		while not action:
			i = raw_input()
			if i is "1":
				return self.slash()
				
			elif i is "2":
				return self.thrust()
				
			else:
				print "Please choose either 1 or 2!"

   

class Mage:
	def __init__(self, name):
		self.name = name
		self.type = "Mage"
		self.hitpoints = 80
		self.dodge = 70

	def fireball(self):
		base_damage = 15
		print "You cast and hurl a ball of fire...mmm toasty..."
		return base_damage + magic_dmgroll()

	def lightning_strike(self):
		base_damage = 30
		print "You cast lightning strike, zzzzzzzapping towards your nefarious enemy..."
		r_damage = magic_dmgroll()
		if  r_damage % 5 == 0:
			self.hitpoints -+ r_damage
			print "You are hit as well for %s damage!! Aiiiiiii" %r_damage
			return base_damage + magic_dmgroll()
		else:
			return base_damage + magic_dmgroll()

	def dodge_attack(self):
		print "You attempt to dodge the attack..."
		time.sleep(0.2)
		if (self.dodge + dodge_roll())>90:
			print "You dodge his obnoxious non-arguments with your brilliant argumentative skills!"
			return True
		else:
			return False
	def action(self):
		print "Attack:"
		print "1. Fireball - a basic magic attack. Medium damage."
		print "2. Lightning Strike - very high damage. Chance to backfire."
		
		action = False
		while not action:
			i = raw_input()
			if i == "1":
				action is True
				return self.fireball()
			elif i == "2":
				action is True
				return self.lightning_strike()
			else:
				print "Please choose either 1 or 2!"


class Troll:
	def __init__(self, name):
		self.name = name
		self.hitpoints = 150  
		self.dodge = 65

	def smash(self):
		base_damage = 15
		print "%s attempts to smash you with his giant club!"%self.name
		damage = base_damage + melee_dmgroll()
		if damage > 25:
			print "BUUUUURNNNN!!!"
		return damage 

	def dodge_attack(self):
		print "Troll attempts to dodge the attack..."
		time.sleep(0.2)
		if (self.dodge + dodge_roll())>90:
			print "He slips away for now...how can you kill that which has got no life???"
			return True
		else:
			print "FAAAAIIILLLL"
			return False	

	def action(self):
		return self.smash()