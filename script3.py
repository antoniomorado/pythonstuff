from sys import argv

script, var1, var2, var3 = argv

print "The script is called:", script
print "Variable one is:", var1
print "Variable 2 is:", var2
print "Variable 3 is:", var3

food = raw_input("What is your favorite food? ")
drink = raw_input("Favorite drink? ")

print "Your favorite food and drink are %s and %s." % (
	food, drink)