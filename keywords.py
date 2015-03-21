from sys import argv 
from os.path import exists
#script, file1 = argv

#matches = 10
#fights = []
#i = 0

#superheros =['spiderman', 'superman', 'batman', 'captain america']

#print "Please add a super vilain to our list of heros:"
#villain = raw_input("> ")

#if villain != 'doc oc':
#	raise AssertionError ("Poor villain!")
#else:
#	print "good coice!"

#superheros.append(villain)

#for heros in superheros:
#	print heros


#def my_generator(val):
#	mylist = range(val)
#	for i in mylist:
#		print "i is %d" % i
#		yield i * i

#the_generator = my_generator(17)
#print (the_generator)



#new_word = 'python'
#code_ver = 3

#if new_word == 'python' or new_word == 'ruby':
#	print "We have code"
#else:
#	print "strange word"

#if new_word == 'python' and (not (code_ver > 3 and new_word == 'ruby')):
#	print "outdated version"
#else:
#	print "ready to go"



# Can assign a quick short function to a variable or funcname
# same as:
# 	def g(n)
# 		return n**2
# 		
#g = lambda n: n**2
#print g(3)



#if dogs == pet_count:
#	print "Same amount"
# Testing if "is" is the same as equality test. (yes it is)
#if dogs is pet_count:
#	print "Same stuff"
#else:
#	print "Not the same stuff"



#events = ['ufc 1', 'ufc 38', 'ufc 85', 'ufc 116']

#print "testing out some new keywords"

#for shows in events:
#	print shows



#print "Enter file name:"
#file1 = raw_input()

# assert exists(file1) #Throws an assertion error if exists func returns false

# We can also use 

#try:
#	f = open(file1, 'r')
#	print f.read()
#except IOError:
#	print "No file by that name"
#finally:
#	print "python is tricky, huh?"



#while i <= matches:
#	print "i at top is %d" % i
#	fights.append("match #%d" % i)
#	i = i + 1
#	print fights
#	if i == 3:
#		break
#	else:
#		print "i at the bottom %d" % i

#print "User please pick a match to delete."
#value = int(raw_input("> "))

#del fights[value]
#print fights



#print "We are adding to the %r" % file1, " file."
#rint "please enter a sentence to add to this file."
#sentence = raw_input("> ")

#with open(file1, 'w') as f:
#	f.write(sentence)



#if value < 10 and value >= 4:
#	print "strong number"
#elif value < 4 and value > 0:
#	print "weak number"
#else:
#	print "follow directions"
