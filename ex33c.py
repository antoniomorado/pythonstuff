#i = 0
#numbers = []

#while i < 6:
#	print "At the top i is %d." % i
#	numbers.append(i)
	
#	i = i + 1
#	print "Numbers now: ", numbers
#	print "At the bottom i is %d." % i
	

#print "The numbers are:"

#for num in numbers:
#	print num
	


#print "\nStudy drill #1, #2, & #3"

#def list_creator(step, max_val):
#	i = 0
#	numbers = []
#	while i < max_val:
#		print "At the top i is %d" % i
#		numbers.append(i)
		
#		i = i + step
#		print "Numbers now: ", numbers
#		print "At the bottom i is %d" % i
		
#	return numbers

	
#numlist = list_creator(2, 8)

#print "The numbers are: "

#for nums in numlist:
#	print nums


print "\nStudy drill #4"

def list_creator():
	i = 0
	numbers = []
	
	for i in range(0, 9, 2):
		print "At the top i is %d" % i
		numbers.append(i)
		
		#i = i + 1
		print "numbers now: ", numbers
		print "At the bottom i is %d" % i
		
	return numbers
	
num_list = list_creator()

print "The numbers are: "

for nums in num_list:
	print nums
