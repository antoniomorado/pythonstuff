#This string is assigned to the variable x and contains a % character followed by the format variable
#d which is used for integers. The value 10 after the string is assigned to the %d. 
x = "There are %d types of people." % 10

#the string binary is assigned to the variable named binary
binary = "binary"
#the string don't is assigned to the variable named do_not
do_not = "don't"

#This string is assigned to the variable y, and contains 2 format variables as well. s is the the format
#variable for strings. The variables after the string; binary is assigned to the first %s and do_not the second.
y = "Those who know %s and those who %s." % (binary, do_not)

#this prints out the string that is assigned to the variable x
print x
#this prints out the string that is assigned to the variable y
print y

#This prints a string with a format variable of r (a string formatter). The variable x is assigned to it.
print "I said: %r." % x

#This prints a string with a format variable of s (a string formatter). The variable x is assigned to it.
print "I also said: '%s'." % y

#The boolean false is assigned to the variable hilarious
hilarious = False

#A string with a formatter variable r is assigned to the variable joke_evaluation.
joke_evaluation = "Isn't that joke so funny?! %r"

#The string in joke_evaluation is printed with the variable hilarious assigned to the formatter variable r.
print joke_evaluation % hilarious

#A string is assigned to the variable w
w = "This is the left side of..."
#A string is assigned to the variable e
e = "a string with a right side."

#The string assigned to the variable w is printed and concatenated to the string assigned to the variable e
print w + e
