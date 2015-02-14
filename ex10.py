#The string is assigned to the variable tabby_cat. The \t will horizontally tab the string
tabby_cat = "\tI'm tabbed in."

#the string is  assigned to the variable persian_cat. The \n will cause the "on a line"
#piece of the string to begin on a new line.
persian_cat = "I'm split\non a line."

#the string is assigned to the variable backlash_cat. The \\ is  an escape backslash
# which allows the \ character to remain in the string.
backlash_cat = "I'm \\ a \\ cat."

#the triple quotes allows for multiple lines of strings. The \t will horizontal tab the line
#it is next to and the \n will begin a new line.
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

#prints the string assigned to each variable.
print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

#The reason the output does not show the new line from \n ASCII linefeed, is because
#the variable formatter %r is for debugging and shows what we typed for the variable
#persian_cat
print "Testing something: \n %r" % persian_cat

#Using %s gives us the proper output
print "Testing something again: \n %s" % persian_cat