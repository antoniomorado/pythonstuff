# Podcast list manager 

podcast = ['jre', 'Bill Burr', 'Joey Diaz', 'Ari Shaffir', 'Duncan Trussell']

numbered =[]

i = 0
n = 0

def pod_loop(n, i, max_num):
	while i < max_num:
		i = i + 1
		title = podcast[n] + " " + str(i)
		numbered.append(title)
	return numbered


print "We'll list my favorite podcasts"


while n <= 4:
	if n == 0:
		max_num = 40
	elif n == 1:
		max_num = 25
	elif n == 2:
		max_num = 10
	elif n == 3:
		max_num = 10
	elif n == 4:
		max_num = 5
	pod_loop(n, i, max_num)
	n = n + 1

for nums in numbered:
	print nums

print "\nWhich episode would you like to pull?"
choice = raw_input("Enter Podcast #: ")

print numbered[int(choice) - 1]

print "\nChoose by name?"
full_choice = raw_input("Enter full title: ")

if full_choice in numbered:
	print full_choice
else:
	print "Not available"


