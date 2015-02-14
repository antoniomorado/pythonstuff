#This string is printed
print "Mary had a little lamb."
#This string has a formatter variable s (for strings). The string snow is assigned to that variable
print "Its fleece was white as %s." % 'snow'
#This string is printed
print "And everywhere that Mary went."
#The string . is multiplied 10 times and printed in a row
print "." * 10 #What'd that do

#C is assigned to the variable end1
end1 = "C"
#h is assigned to the variable end2
end2 = "h"
#e is assigned to the variable end3
end3 = "e"
#e is assigned to the variable end4
end4 = "e"
#s is assigned to the variable end5
end5 = "s"
#e is assigned to the variable end6
end6 = "e"
#B is assigned to the variable end7
end7 = "B"
#u is assigned to the variable end8
end8 = "u"
#r is assigned to the variable end9
end9 = "r"
#g is assigned to the variable end10
end10 = "g"
#e is assigned to the variable end11
end11 = "e"
#r is assigned to the variable end12
end12 = "r"

# watch that comma at the end. try removing it to see what happens
#Each variable from the list above is concatenated. The comma keeps the next set of 
#concatenated variables on the same line but with a space. This is done because more than
#80 characters is bad according to python
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
