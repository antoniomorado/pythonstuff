from sys import exit

print "IBD's 10 Secrets to Success:"
success = ['think', 'dreams and goals', 'action', 'learning', 'work hard', 
			'details', 'time', 'innovate', 'communicate', 'Be honest']

for rules in success:
	print rules

print "Would you like to add a personal rule for success?"
choice = raw_input("y or n? ")

if choice == 'y':
	new_rule = raw_input("type new rule: ")
	success.append(new_rule)
	print "\nNew List:"
	for rules in success:
		print rules
elif choice == 'n':
	exit(1)
else:
	print "read the rules next time!"
	exit(1)