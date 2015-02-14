from sys import argv

script, ID, user_name, = argv
entry = ':: - '

print "Hi %s ID number: %s, I'm the %s script." % (user_name, ID, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(entry)

print "Where do you live %s?" % user_name
lives = raw_input(entry)

print "Your ID # is %s. When did you start?" % ID
years = raw_input(entry)

print "What kind of computer do you have?"
computer = raw_input(entry)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
So you've worked here for %r.
And you have a %r computer. Nice.
""" % (likes, lives, years, computer)

