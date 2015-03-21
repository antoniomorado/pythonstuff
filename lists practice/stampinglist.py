# Stamping system for metal parts 

order = ["mustang", 8, ]

def product(o):
	print "Which car is the frame for?"
	car_choice = raw_input("> ")
	print "How many components?"
	num = raw_input("> ")
	order.append(car_choice)
	order.append(int(num))
	return order

print "Would you like to print product?" 
print "Type: y or n"
choice = raw_input("> ")

while choice == "y":
	product(order)
	print order
	print "\nWould you like to add more product?" 
	print "Type: y or n"
	choice = raw_input("> ")

