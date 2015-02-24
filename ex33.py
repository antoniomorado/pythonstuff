first = 0 
numbers =[]

# Using a while loop inside a function
#def lineup(i, cars, inc):
#	while i < cars:
#		print "At the top i is %d" % i
#		numbers.append(i)
#	
#		i = i + inc
#		print "Numbers now: ", numbers
#		print "At the bottom i is %d" % i
#	return cars
	

# Using a for-loop inside a function
def lineup(start, drivers, inc):
	for i in range(start, drivers, inc):
		print "At the top i is %d" % i
		numbers.append(i)
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		

motorists = 8
incremented = 3
lineup(first, motorists, incremented)
	
print "The numbers: "

for num in numbers:
	print num