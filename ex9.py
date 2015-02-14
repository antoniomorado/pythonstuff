# Here's some new strange stuff, remember type it exactly.

#The string containing the days of the week is assigned to the variable days.
days = "Mon Tue Wed Thu Fri Sat Sun"

#The string containing the months of the year is assigned to the variable months.
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#This string is printed followed by the string assigned to the variable days on the same line
print "Here are the days: ", days

#This string is printed followed by the string assigned to the variable months. Each month goes to
#a different line because \n creates a new line for the next part of the string
print "Here are the months: ", months


#it appears that using triple quotes allows you to start a new line of text just by hitting enter
#it may maintain the format that you type.
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

