from sys import argv
from os.path import exists
from sys import exit

# User must pass in the game file called mygame.py and the adventure intro called starwars.txt
def start():
	script, game1 = argv

	print "Welcome to Millenium Falcon choose your own adventure."
	print "You've loaded: %r \n" % game1

	story_1 = open(game1)

	print story_1.read()
	#User is given 3 choice (functions) to choose from in, above, and below.
	choice = raw_input("in, above, or below? ")
	
	if choice == "in":
		dive_in()
	elif choice == "above":
		above()
	elif choice == "below":
		below()
	else:
		print "Nice job hotshot. You've been blasted to death by tie fighter!"
		print "Better luck next time."
		exit(0)

# Design dive in choice. User can land or fight. land will send user to a land() func
def dive_in():
	print """
	The tie fighters give chase and follow you in.
	You notice a patch of large asteroids.
	Maybe you can land on one and give them the slip.
	It's dangerous. Do you land or fight?"""
	choice = raw_input("> ")
	
	if choice == "land":
		land()
	elif choice == "fight":
		dead("You fight well,")
	else:
		print "Nice job hotshot. You've been blasted to death by tie fighter!"
		print "Better luck next time."
		exit(0)


def above():
	print """
	You pull up.
	What's waiting for you is a Super Star Destroyer!
	We can either move into attack position or dive back into the asteroid field."""
	choice = raw_input("attack or dive in? ")
	
	if choice == "attack":
		dead("Wow! That was brave")
	elif choice == "dive in":
		dive_in()
	else:
		print "Nice job hotshot. You can't follow directions!"
		print "Better luck next time."
		exit(0)

def below():
	print """
	There's a black whole!
	We can enter the wormhole and see what happens or dive back into the Asteroid field"""
	choice = raw_input("black hole or asteroids? ")
	
	if choice == "black hole":
		start()
	elif choice == "asteroids":
		dive_in()
	else:
		print "Nice job hotshot. You can't follow directions!"
		print "Better luck next time."
		exit(0)
	

def land():
	print"""
	You land your ship in a cave on the face of an asteroid.
	The slip works.
	While waiting you hear banging on your hull again
	You can go outside and check it out or pulse the hull."""
	
	choice = raw_input("go outside or pulse? ")
	
	if choice == "go outside":
		mynock()
	elif choice == "pulse":
		print "Ok pulsing the hull will nock off whatever is on the ship."
		print "We can charge the pulse to a level between 1 and 10"
		print "How much charge?"
		charge = int(raw_input())
		
		if charge <= 3:
			dead("nice try")
		elif charge > 3 and charge <= 7:
			print "Congratulations! You gave the empire the slip. The force is with you."
		elif charge > 7:
			dead("You fried the ship")
		else:
			print "Nice job hotshot. You can't follow directions!"
			print "Better luck next time."
			exit(0)
	else:
		print "Nice job hotshot. Your hull cracked!"
		print "Better luck next time."
		exit(0)


def mynock():
	print "Oh no! There are mynocks on chewing on the power cables."
	print "We can shoot them or stab them."
	choice = raw_input("shoot or stab? ")
	
	if choice == "shoot":
		print "Congratulations! You gave the empire the slip. The Force is with you."
		exit(0)
	elif choice == "stab":
		dead ("Mynocks swarm you. Nice try")
	else:
		print "Nice job hotshot. You can't follow directions!"
		print "Better luck next time."
		exit(0)
		
def dead(reason):
	print reason + ", but without Luke the force just wasn't with you."	
	print "Better luck next time."
	exit(0)

start()
