#The string with 4 r formatter variables (used for string variables) is assigned to the
#the variable called formatter
formatter = "%r %r %r %r"

#the string in the variable formatter is printed. The integers 1,2,3, and 4 are assigned to
#the formatter variables r in the order that they are in in the parentheses
print formatter % (1, 2, 3, 4)

#the string in the variable formatter is printed. the strings in the parentheses are assigned
#to the formatter variables r in the order they are listed
print formatter % ("one", "two", "three", "four")

#the string in the variable formatter is printed. The booleans true and false are assigned to the
#formatter variables r in the formatter string.
print formatter % (True, False, False, True)

#The string in the formatter variable is printed. The formatter variable is assigned to itself as variables
#in parentheses. So the string of 4 r formatter variables are assigned 4 times. Once per r formatter.
print formatter % (formatter, formatter, formatter, formatter)

#The string in the formatter variable is printed. 4 strings are assigned to the r formatter variables in
#the order they are in in the parentheses
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)
	
	# the output of the second to last line has double quotes because the string has a
	#a single quote for the word didn't.
	