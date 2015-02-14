from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your document %r." % filename
print txt.read()


print "Type the file name."
file_again = raw_input("> ")

txt_again = open(filename)

print txt_again.read()

