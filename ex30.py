#if statements tell your script, if this boolean expression is True then run the indented
#code under it, otherwise skip it.
people = 50
cars = 40 
trucks = 45

#these statements are a block of conditional if-else statements. Each condition is tested
#and when a condition is true the code under that conditional is executed. Then the
#program leaves this block of conditional statements and moves on to the next. else is the
#the default to be executed if the other conditions are not met/True.

#tests if the value assigned to the cars variable is greater than people and if True,
#prints the next line
if cars > people:
	print "We should take the cars."
#if the above condition is False, this tests is the value assigned to the variable cars is
# les than the value assigned to the variable people and if true prints the next line.
elif cars < people:
	print "We should not take the cars."
#if both of the above conditions are False, the else statement that follows is the default 
#conditional statement, which prints out to the user
else:
	print "We can't decide."

#Tests if the value assigned to the trucks variable is greater than the value assigned to
#the cars variable. If True it prints the following statement. If False it moves to the
#the next conditional in this code block, which begins with elif.	
if trucks > cars:
	print "That's too many trucks."
#This next conditional statement tests if the value assigned to the trucks variable is
#less the value assigned to cars. If True it prints out the following string. If False it
#moves to the next conditional in this code block, which begins with else.
elif trucks < cars:
	print "Maybe we could take the trucks."
#this is the default conditional. If the above to conditional statements return False, the
#following string is printed out to the user.
else:
	print "We still can't decide."

#This line tests if the value assigned to the people variable is greater than the value
#assigned to trucks, if True the indented print function prints out the string.	
if people > trucks:
	print "Alright, let's just take the trucks."
#The else statement is the default conditional that prints the following string if the
#above condition is false.
else:
	print "Fine, let's stay home then."

if cars > people and trucks < cars:
	print "Most cars can fit may people."
elif trucks < people:
	print "We're gonna need a bus!"
else:
	print "We're stuck."
	
if trucks == people:
	print "Perfect match."
else:
	print "We're going to have extra space."