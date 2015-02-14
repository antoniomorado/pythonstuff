#The from is calling the sys module (or library)
# and import is importing the argv module
from sys import argv

#The argv variable is unpacking to script first then filename
#These arguments need the user to pass 2 command line arguments
script, filename = argv

#This opens a file that is assigned to the filename variable
#and is assigned to txt
txt = open(filename)

#This string is printed with a formatter variable for strings
#and the filename variable is assigned to %r
print "Here's your file %r:" % filename
#This prints the text of the file assigned to filename
#it is done by using a read method on the txt variable using
#the dot operator
print txt.read()
txt.close()

#This prints the string and then the next line uses raw_input
#to request a filename from the user and assigns it to file_again
print "Type the filename again:"
file_again = raw_input("> ")

#The file assigned to file_again is opened and assigned to 
#txt_again
txt_again = open(file_again)

#the read method is called again. This time for the txt_again variable.
#and printed
print txt_again.read()
txt_again.close()

#I think getting the file from the raw input method even after passing an argv argument
#is better because of the option to choose the file you open. This is after the program is
#running.
