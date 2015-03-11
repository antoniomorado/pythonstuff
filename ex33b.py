#i = 0 
#numbers = []


#def num_list(iter, val):
#	i = 0
#	numbers = []
#	while i < val:
#		print "At the top i is %d" % i
#		numbers.append(i)
	
#		i = i + iter
#		print "Numbers now: ", numbers
#		print "At the bottom i is %d" % i
	
	
#	return numbers

#When using for loop the iterator is already included in the range method.
#There is no need for "i = i + iterator" in the loop's code.
def num_list(iter, val):
	i = 0
	numbers = []
	for i in range(0, val, iter):
		print "i is %d" % i
		numbers.append(i)
		print"Numbers now: ",  numbers
		
	return numbers
		
#The "numbers" list is defined in the scope of the num_list function. 
#To do this following for loop we must assign our function call to a variable, in turn this
#takes the return value which is our list and makes it available out of the func def scope
	
numvals = num_list(4, 12)

print "The numbers: "

for num in numvals:
	print num



numvals2 = num_list(2, 5)

print "The numbers: "

for num in numvals2:
	print num