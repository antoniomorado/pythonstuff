print "You enter a dark room with three doors. Do you go through door #1, #2, or #3?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheesecake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Karate kick the bear."
	print "4. Vomit on yourself."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "the bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	elif bear == "3":
		print "Nice job Neo! You just beat the Matrix."
	else:
		print "Well, doing %s is probably better. bear runs away." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
		
elif door == "3":
	print "You step outside to a sunny day and fresh air."
	print "1. Take a break from the computer."
	print "2. Get some lunch."
	
	endgame = raw_input("> ")
	
	if endgame == "1":
		print "Type \"exit\"."
	else:
		print "Go order a pizza and play again later!"
		
else:
	print "You stumble around and fall on a knife and die. Good job!"