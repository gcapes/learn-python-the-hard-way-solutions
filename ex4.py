# Assign number of cars
cars=100
# Assign variable for number of spaces per car
space_in_a_car=4.
# Assign number of drivers
drivers=30
# Assign number of passengers
passengers=90
# Assign result of cars-drivers to new variable
cars_not_driven=cars-drivers
# Create another variable for numbr of cars driven
# I don't see why this is required
cars_driven=drivers
# Calculate capacity and save result in new variable
carpool_capacity=cars_driven*space_in_a_car
# Calculate people/car and assign to new variable
average_passengers_per_car=passengers/cars_driven


print "There are", cars, "cars available."
print "There are only", drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."

# Study drills
# Error from mistyping the variable name, thus attepmting to use a variable
# which hasn't been defined yet.
# 1. If you use 4 instead of 4. you get integer division. Necessary depends on 
# application. Can only get integer number of people but it would better to round
# instead of using floor division.
