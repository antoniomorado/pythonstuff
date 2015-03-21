
# Basic with-as example
with open('output.txt', 'w') as f:
    f.write('Hi there!')


# class example of with-as statement
class controlled_execution:
	def __enter__():
		#code
		return thing
	def __exit__():
		#code

with controlled_execution() as thing:
	#code

# Example of an assert statement
def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!" #Prints this string when assert error
   return ((Temperature-273)*1.8)+32

print KelvinToFahrenheit(273)
print int(KelvinToFahrenheit(505.78))
print KelvinToFahrenheit(-5) #will trigger the Assert Error


# Examples of break statements in loops or if-statements. Stops the loop
for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print 'Current Letter :', letter
  
var = 10                    # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 5:
      break

print "Good bye!"


# Examples of continue statements in loops or if-statements, similar to break but
# "...rejects all the remaining statements in the current iteration of the 
# loop and moves the control back to the top of the loop."
for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print 'Current variable value :', var
print "Good bye!"


# Example of del function
list1 = ['physics', 'chemistry', 1997, 2000];

print list1;
del list1[2];
print "After deleting value at index 2 : "
print list1;


# Example of except 
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
   fh.close()

# Example of exec in terminal. Lets your run strings as python code
#  >> exec('print("cats and dogs")\nprint("oh and fish")')
# cats and dogs
# oh and fish


# Example of finally clause. The finally is guaranteed to occur, even if an
# exception is raised during the try block.
try:
    file = open('frobnaz.txt', 'w')
    raise ValueError
finally:
    file.close()
    os.path.remove('frobnaz.txt')


# An example of is vs ==. 
# You can see that is compares two objects in memory, == compares their values
#a = 19998989890
#b = 19998989889 + 1
# >>> a is b
#False
#>>> a == b
#True


# Example of lambda functions in use for short anonymous function w/out using def
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print "Value of total : ", sum( 10, 20 )
print "Value of total : ", sum( 20, 20 )


# Example of using pass statement as placeholder for code that is not written yet
for letter in 'Python': 
   if letter == 'h':
      pass
      print 'This is pass block'
   print 'Current Letter :', letter

print "Good bye!"


# Example of using raise to handle exceptions
def functionName( level ):
   if level < 1:
      raise "Invalid level!", level
      # The code below to this would not be executed
      # if we raise the exception


# Example of using try to handle exceptions. (requires except and else)
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
   fh.close()


 # Example of yield. It is used like a return statement in generators.
 # The trick is that you must understand the difference in using generators 
 # and the itteration of lists. It all has to do with memory see:
 # https://freepythontips.wordpress.com/2013/09/29/the-python-yield-keyword-explained/
 >>> def createGenerator():
...    mylist = range(3)
...    for i in mylist:
...        yield i*i
...
>>> mygenerator = createGenerator() # create a generator
>>> print(mygenerator) # mygenerator is an object!
<generator object createGenerator at 0xb7555c34>
>>> for i in mygenerator:
...     print(i)
0
1
4
