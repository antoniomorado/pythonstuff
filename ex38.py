ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

# The following split method is called on the ten_things string. It returns a list of
# words in the string, delimited by ' '. Supplying no sep parameter is given, consecutive
# white spaces are regarded as a single separator.
stuff = ten_things.split(' ') # Now we have a list named stuff
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# While length of stuff does not equal 10, pop off the last value in the list more_stuff
# and assign it to the variable next_one
while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one) # append name popped off end of more_stuff to end of list stuff
	print "There are %d items now." % len(stuff) # Counts number of items in stuff
	
print "There we go: ", stuff # Prints the stuff list

print "Let's do some things with stuff."

print stuff[1] # Prints the 2nd word stored in the stuff list
print stuff[-1] # whoa! fancy # Prints the last word stored in the stuff list
print stuff.pop() # Pops off the last word added to the list stuff and prints it
# The 10th word was popped off so now we have 9 words

# About the join method: Return a string which is the concatenation of the strings in the 
# iterable iterable. The separator between elements is the string providing this method.

# The following creates a string by joining the words in the list stuff, separated by ' '
print ' '.join(stuff) # what? cool!
# The following creates a string by joining the words in the list stuff from the 4th-6th
# word (not including the 6th) separated by # sign. Hint: Remember cardinality
print '#'.join(stuff[3:5]) # super stellar!