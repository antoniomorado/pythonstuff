#Defined the function cheese_and_crackers that receives 2 arguments called cheese_count
#and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#This prints a string containing a formatter variable %d. The cheese_count variable passes
	#the argument to %d.
	print "You have %d cheeses!" % cheese_count
	#This prints a string with a formatter variable for numbers %d. The boxes_of_crackers variable
	#is passed to the %d.
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
	
print "We can just give the function numbers directly:"
#the cheese_and_crackers function is called. The number 20 is passed to cheese_count argument
#and 30 is passed to the boxes_of_crackers.
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
#The integer 10 is assigned to a new variable amount_of_cheese
amount_of_cheese = 10
#The integer 50 is assigned to a new variable amount_of_crackers
amount_of_crackers = 50

#the cheese_and_crackers function is called with the new variables amount_of_cheese and
#amount_of_crackers passed to the functions original arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
#the cheese_and_crackers function is called and the integer addition 10+20 is passed to the 
#cheese_count argument and 5+6 is passed to the boxes_of_crackers argument
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
#The cheese_and_crackers function is called. The new amount_of_cheese variable is added to the
#integer 100 and passed to the cheese_count argument. The new amount_of_crackers variable is
#added to 1000 and passed to the box_of_crackers argument in the function
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)