print "Time to play a game."
print "You wake up inside a cave in the Hyborean age. That's around the time of Atlantis."
print """Do you exit the cave mouth or delve deeper into the cave?
1. for exit.
2. delve deeper.
"""

choice = raw_input("> ")

if choice == "1":
	print "There's a pack of headhunters out here chanting something with razor teeth!"
	print "1. You fight."
	print "2. You make a run for it."
	
	battle = raw_input("> ")
	
	if battle == "1":
		print "Too many! You've been eaten. Too bad. :("
	elif battle == "2":
		print "Smart choice. You live to fight another day!"
	else:
		"You don't know how to play games."

elif choice == "2":
	print "There is a pool of water back here."
	print "1. Dive in."
	print "2. Try to make your way around the edge."
	print "3. Head back towards mouth."
	
	escape = raw_input("> ")
	
	if escape == "1" or escape == "2":
		print "You were eaten by lake monster!"
	else:
		print "We have a WINNER! Collect your prize."
		
else:
	print "You're not good at following directions, huh?"
