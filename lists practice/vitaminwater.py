# Take a string that has vitamin water types, parse the list, and create a case.

print "welcome to drink depot."
print "please add your favorite flavors of vitamin water"
water_sent = raw_input("list your 5 favorites: ")

flavors = water_sent.split(", ")

print flavors

print "Your personal order includes: ",
print ' x4 '.join(flavors), " x4."



