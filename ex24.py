print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-----------------"
#Calling poem variable with multiline string assigned
print poem
print "-----------------"

five = 10 - 2 + 3 - 6
#event though variable five is an int, we are passing it to this string as a string 
#formatter
print "This should be five %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
start_point = 1000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
#Be carefule! To use the calling function method directly as used in the next line, we
#must have where our function is defined return its values in the correct order
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)
