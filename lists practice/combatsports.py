# Combat sports event list
from sys import exit

print "UFC Events and dates:"

event_title = ['Fight Night: Maia vs LaFlare', 'Fight Night: Mendes vs Lamas',
				'Fight Night: Gonzaga vs CroCop 2', 'on Fox: Rockhold vs Machida',
				'186: Dillashaw vs Barao 2']
event_date = ['3-21-2015', '4-4-2015', '4-11-2015', '4-18-2015', '4-25-2015']

for  ttl, dt in zip(event_title, event_date):
	print "UFC " + ttl, dt

print ""

print 'Would you like to add an event?'
choice = raw_input("y or n ")
if choice == 'y':
	new_ttl = (raw_input("Event Title: "))
	event_title.append(new_ttl)
	new_dt = (raw_input("Event Date: "))
	event_date.append(new_dt)
	for ttl, dt in zip(event_title, event_date):
		print "UFC " + ttl, dt
elif choice == 'n':
	print "Enjoy the schedule."
	exit(1)
else:
	exit(1)
