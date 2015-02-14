name = 'Antonio C. Morado'
age = 35 #not a lie
height = 66 #inches
weight = 240 #lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

height_in_cm = height * 2.54
weight_in_kg = weight * 0.45

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "My height in centimeters is %f."  % height_in_cm
print "My weight in kilograms is %f." % weight_in_kg

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age +
 height + weight)