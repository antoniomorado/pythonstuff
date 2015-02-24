people = 20
cats = 30
dogs = 15

#if evaluates the condition of the statement that follows the reserved word "if"
#if the statement is True, the list of arguments in the function are executed.
#The following lines are indented because an if-statement is a function. (If not indented
#the line is not associated with the if-statement and executes as normal.)
if people < cats:
	print "Too many cats! The world is doomed!"

if people > cats:
	print "Not many cats! The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print "People are less than or equal to dogs."
	
if people == dogs:
	print "People are dogs."
	
if dogs and cats > people:
	print "People are less than pets."
	
if people > dogs or cats:
	print "There's just a lot of cats hanging around."
	
if dogs != cats or people:
	print "Dogs are inferior."
	