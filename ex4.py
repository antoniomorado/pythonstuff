# 100 is being assigned to the variable name cars
cars = 100
# the float number 4.0 is being assigned to the variable name space_in_a_car
space_in_a_car = 4
# 30 is being assigned to the variable name drivers
drivers = 30
# 90 is being assigned to the variable passengers
passengers = 90
#cars is being subtracted by drivers and assigned to the variable cars_not_driven
cars_not_driven = cars - drivers
#the value stored in the variable drivers is also being assigned to a new variable cars_driven
cars_driven = drivers
#the variable carpool_capacity is being assigned the calculation of cars_driven and space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#average_passengers_per_car is calculated by dividing passengers by cars_driven
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."