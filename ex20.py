#from is used to import module sys and creates references to argv
from sys import argv

#the first argument passed from argv is script, in this instance that is ex20.py
#the next argument passed by the user at terminal from argv is input_file, in this case test.txt
script, input_file = argv

#The first function designed is print_all() and it is passed the parameter f
#the next line uses the read method applied to f to reads the entire content of the file
#and prints it out to the user
def print_all(f):
	print f.read()

#the second function designed is rewind() and is also passed the parameter f
#The next line applies the seek method to the file f, and sets the file's current position to 0
def rewind(f):
	f.seek(0)
	
#The third function defined is print_a_line which is passed 2 values, line_count and f
#the print method is called to show the value assigned to variable line_count and
#read the next line by applying the readline() method to the file f. The file f keeps track of the
#position of the readhead from the last call of the readline method. Each call of the readline
#method returns \n to move the read-head to the next line. line_count is just counting along with
#each iteration/call of the print_a_line method. Remember that the read head begins with position
#0 because of the rewind method above.
def print_a_line(line_count, f):
	print line_count, f.readline()

#The open function is applied and passed a file called input_file (This was the second argument 
# passed from the user at terminal) and this object is assigned to the variable current_file
current_file = open(input_file)

#A string is printed out to console and the escape n is used to create a new line after
print "First let's print the whole file:\n"

#the print_all function is called and the current_file parameter or file (test.txt) is  
#passed to the functions f parameter
print_all(current_file)

#The string is printed to the user
print "Now let's rewind, kind of like a tape."

#The rewind function is called and passed current_file file. In this case test.txt
rewind(current_file)

#This string is printed to the user
print "Let's print three lines:"

#the integer 1 is assigned to the current_line variable
current_line = 1
#the print_a_line function is called and passed the value current_line or 1 and current_file
#in this case test.txt. These are called line_count and f in the original function. The result
#is a printing of 1 followed by the 1st line of text in the file until \n and returns \n to
#move to the next line.
print_a_line(current_line, current_file)

#The current_line variable is incremented by 1
current_line += 1
#The new current_line value or 2 is passed to the print_a_line function and current_file is
#passed again. The result is a printing of 2 followed by the 2nd line of text in the file until
#the end of the line and returns \n to move to the next line
print_a_line(current_line, current_file)

#the current_line variable is incremented again. This time the value is 3
current_line += 1
#the new current_line integer value 3 is passed to the print_a_line function again along
#with the current_file file. The result is a printing of 3 followed by the 3rd line of text
#in the file until the end of the line and returns \n to move to the next line
print_a_line(current_line, current_file)