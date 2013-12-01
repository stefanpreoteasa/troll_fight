
#TROLL FIGHT 
#Made by Stefan Preoteasa to test out all the cool Python stuff he's learned :)
#The point of the game is to exercise certain things I've learned how to do in Python:
	#lists
	#functions and odularity in design (trying to think to write a program on which I might improve later since there are mahy places I can improve)
	#classes and constructors
	#regex (just a bit in this one though)
	#loops (unfortunately could't find use for a for loop)
	#multiple files
	#user friendly design :P


import random
import time
import re
import string

#importing classes from classes.py
from classes import Warrior
from classes import Mage
from classes import Troll

from utils import s
from utils import n
from utils import valid_username




troll_names = ['Gumlug', "Blurpig", "The Great Trollowski", "AXE BODY SPRAY"]
#a timer that makes the program sleep for WAIT seconds.... creates aditional tension and anticipation!!!


#intro for the game
def intro():
	print "Hello World!!! ...\n "
	s()
	print "And welcome to The Troll Pit, where aspiring, n00b or l33t, hackers \n fight their fears and confront the nastiest of all internet monsters: \n "
	s()
	s()
	print "THE VICIOUS TROLL!\n\n"
	s()
	print "This will be a battle to the death where you will be allowed to use:\n"
	print "SWORDS!!!"
	s()
	print "MAGIC!!!!!!"
	s()
	print "FOUL LANGUAGE FROM BEHIND AN ANONYMOUS USERNAME!!!! (note: in future patches)"
	s()
	print "...and everyone's favorite..."
	s()
	print "A RANDOM NUMBER GENERATOR TO RANDOMLY DETERMINE YOUR CHANCES OF SUCCESS!!!1!1\n\n\n"

#choosing function. Returns player class
def choose_class():
	print "First, please choose your class of combatant by pressing the appropriate number:\n"
	print "1. The Warrior - master of close combat, uses a two-handed sword and has the SLASH and THRUST abilities"
	print "2. The Mage - user of arcane magic, can cast FIREBALL and LIGHTNING STRIKE"
	print "\n"
	player_class = ""
	player_choice = False
	while player_choice == False:
		c = raw_input()
		if c == "1":
			player_class = "Warrior"
			player_choice =  True
		elif c =="2":
			player_class = "Mage"
			player_choice = True
		else:
			print "Please type in an appropriate number! The trolls are waiting!"
	return player_class

#user input from the keyboard, using regex
def get_user_name():
	user = ""
	user_in = False
	while user_in is False:
		print "Please enter your name (between 3 and 20 characters long):"
		user = raw_input()
		if valid_username(user):
			user_in = True
		else:
			print "Invalid username! Do you want to die a nameless hero???"
			s()
	return user


def dead_check(entity): #troll or player, see if someone died after an attack
	if entity.hitpoints <= 0:
		return True

def fight(player, troll):
	#Main fight function
	#Is called by the Mage or Warrior classes and takes in the player and troll objects
	#Handles their abilities, keeps track of the rounds and determines the winners.
	#Modularity and all that :)
	
	#Initialization conditions
	player_win = False
	troll_win = False
	round = 1

	#main loop
	while (player_win is False and troll_win is False): #main fighting sequence
		if round == 1:
			n()
			print "Tutorial:"
			print "Both you and the troll get one action (or attack) per turn."
			print "You can choose which action you want to do by pressing the appropriate key (usually 1 or 2...maybe more in future implementations ;) )"
			n()

		print "ROUND "+ str(round) + "!"
		n()
		if round == 1:
			s()
			print "FIGHT!"

		n()

		print "Troll: %s hitpoints"%troll.hitpoints
		print "%s: %s hitpoints"%(player.name, player.hitpoints) 
		s()
		n()

		player_damage = player.action()

		if player_damage != 0:
			if troll.dodge_attack():
				player_damage = 0
				n()
				s()
			else:
				troll.hitpoints = troll.hitpoints - player_damage
				print "Troll: %s hitpoints"%troll.hitpoints
				s()
				n()

		if dead_check(troll) is True:
			player_win = True
			break

		troll_damage = troll.action()

		if player.dodge_attack() is True:
			troll_damage = 0
			s()
		else:
			player.hitpoints = player.hitpoints - troll_damage
			if round%2==0:
				print "Arrrghhh...you take one for the team"
				n()
				s()
			else:
				print "Not fast enough...dammit..."	
				n()
				s()
			print "%s: %s hitpoints"%(player.name, player.hitpoints) 
			n()

		if dead_check(player) is True:
			troll_win = True

		round += 1
		
	if troll_win is True:
		print "%s finally smashes you into the ground...\n...alas bro, you have given in to his incessant trolling... "%troll.name

	if player_win is True:
		print "You are victorious!!!"
		s()
		n()
		print "%s lies defeated in a pool of his on blood after being on the receiving end of your attacks (and good arguments) one too many times"%troll.name
		print "Young children and old ladies can peruse forums and chatboards without being exposed to his vileness. \n The interwebs are safe...for now. "				# 


def warrior_fight(user_name):
	player = Warrior(name = user_name)
	print player.name
	
	troll_name = troll_names[random.randrange(0, len(troll_names))]

	print "GET RRRRRRREEEEEEAAAADY! %s is about to enter the foru...arrr... I mean ...THE ARENA!!! "%player.name
	n()
	
	troll = Troll(name = troll_name)
	s()
	print "On the other side..."
	s()
	print "...a being so foul, so nasty..."
	s()
	print "...known throughout the internets as..."
	n()
	s()
	print "%s!!!!"%troll.name.upper()
	print "GET READY ..."
	s()
	print "It's %s versus %s!!!"%(troll.name, player.name)
	s()

	return fight(player, troll)


def mage_fight(user_name):
	player = Mage(name = user_name)
	print player.name

	print "GET RRRRRRREEEEEEAAAADY! %s is about to enter the foru...arrr... I mean ...THE ARENA!!! "%player.name

	troll_name = troll_names[random.randrange(0, len(troll_names))]
	troll = Troll(name = troll_name)
	s()
	print "On the other side..."
	s()
	print "...a being so foul, so nasty..."
	s()
	print "...known throught the internets as..."
	s()
	print "%s!!!!"%troll.name.upper()
	print "GET READY ..."
	print "It's %s versus %s!!!"%(troll.name, player.name)

	return fight(player, troll)
	

#___________________GAME START__________________________________________________
intro() #Intro sequence. disactivate for testing reasons
player_class = choose_class()
user_name = get_user_name()
print user_name

if player_class == "Warrior":
	warrior_fight(user_name)
if player_class == "Mage":
	mage_fight(user_name)

n()
n()

print "Thanks for playing TROLL FIGHT!"
n()
print "We hope you had (a relatively good amount of) fun!"
n()
n()



