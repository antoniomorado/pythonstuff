def weight_equipment(light_kettlebell, heavy_kettlebell, dumbell):
	print "I have 3 weights total."
	print "I have a light kettlebell weighing %d lbs." % light_kettlebell
	print "I also have a heavy kettlebell that weighs %d lbs." % heavy_kettlebell
	print "And a %d lb dumbell." % dumbell
	print "Lets get to work! \n"

print "Just passing integers:"	
weight_equipment(30, 45, 35)

print "Passing new variables:"
lightbell = 20
heavybell = 40
dummy = 45

weight_equipment(lightbell, heavybell, dummy)

print "passing addition:"
weight_equipment(10+15, 20+25, 40+5)

print "passing variables plus addition:"
weight_equipment(lightbell + 5, heavybell + 10, dummy + 10)

print "Time to ask you for weights."
l_bell = int(raw_input("Please enter the Light kettlebell weight: "))
h_bell = int(raw_input("Heavy kettlebell weight: "))
d_bell = int(raw_input("Dumbell weight: "))

weight_equipment(l_bell, h_bell, d_bell)



print "We'll ask again with prompt symbols."
prompt = "--> "

print "What is the light kettlebell weigh?"
light_b = int(raw_input(prompt))

print "What is the weight of the heavy one?"
heavy_b = int(raw_input(prompt))

print "What does the dumbell weigh?"
dum = int(raw_input(prompt))

weight_equipment(light_b, heavy_b, dum)
