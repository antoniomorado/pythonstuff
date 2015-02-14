#we call the sys package and import the argv module (or feature)
from sys import argv

#The argv variable is unpacking to the script and filename variable. The argv arguments are
#passed to script and filename in the order the user enters them into the command line
script, filename = argv

#The file assigned to the filename variable is passed to the %r formatter variable.
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

#the raw_input function requests a user input. Return goes to the next command. CTRL-C is
#the standard cancel command for canceling any python program.
raw_input("?")

#The target variable is assigned a file named filename. filename is a variable that was 
#assigned a text file during the argv arguments before the program was run. w says to open
# the file in "write mode"
print "Opening the file..."
target = open(filename, 'w')

#the truncate method is called for the target variable. The truncate method clears the file
#contents
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

#These 3 lines request strings of text from the user. It uses the raw_input function with
#a prompt that requests strings.
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#The write method is applied to the target variable 3 times. Once for each variable line1,
#line2, line3. The escape n string is used to go to the next line.
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

input_string = "%r\n%r\n%r\n" % (line1, line2, line3)
target.write(input_string) 

print "And finally, we close it."
#The close method is applied to the target variable. This closes the file which is a good
#practice
target.close()


#Be careful when using "w" when opening a file in write mode. If it already exists it truncates it.