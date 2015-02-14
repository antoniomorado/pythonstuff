# prints out the string of text.
print "I will now count my chickens:"

# Hens is first calculated 30 divided by 6 and then added to 25. Order of operation & LtoR 
print "Hens", 25.0 + 30.0 / 6.0
# Roosters first multiplies 25 by 3, then divides by 4 and results in 75/4 = 18 
# with remainder 3. That 3 is then subtracted from 100, giving us 97 Roosters.
print "Roosters", 100.0 - 25.0 * 3.0 % 4.0

print "Now I will count the eggs:"
# According to order of operations, 4%2 is evaluated first resulting in 0, then 1/4 which 
# is 0.25 but since we are only working with whole number calculation, we get 0.
# Then we add 3+2+1-5+0-0+6 = 7 
print 3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0

print "Is it true that 3 + 2 < 5 - 7?"
# The < operator evaluates if the left is less than the right. Since 5 is greater than -2
# the answer to the evaluation will be false
print 3.0 + 2.0 < 5.0 - 7.0
# we get the calculations to the evaluation above. the answers to 3 plus 2 is 5 and the 
# answer to 5 minus 7 is -2.
print "What is 3 + 2?", 3.0 + 2.0
print "What is 5 - 7?", 5.0 - 7.0

print "Oh, that's why it's False."

print "How about some more."
# the > operator is evaluating if the 5 on the left is greater than the -2 on the right. 
# The answer is True.
print "Is it greater?", 5.0 > -2.0
# the >= is evaluating if the 5 on the left is greater than or equal to the - 2 on the 
# right. The answer is true.
print "Is it greater or equal?", 5.0 >= -2.0
# The <= operator is evaluating if the 5 on the left is less than or equal to the -2 on the
# the right. The answer is false.
print "Is it less or equal?", 5.0 <= -2.0
