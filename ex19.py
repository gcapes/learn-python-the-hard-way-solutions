# Define function taking two arguments
# This function just prints out the arguments with some extra text
# for context.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
# Call the function using numbers
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# Call the function using numbers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
# Call the function using numbers and maths.
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
# Call function using combination of variables and literal numbers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Study drills
# Write function of your own and run 10 different ways:
def mine(a,b):
    print "The arguments supplied were: a = %s, b = %s" % (a,b)

mine("one","two")
mine(1,2)
a='A'
b='B'
mine(a,b)
mine(a+a,b+b)
mine(a+b,1+2)
mine(raw_input('Supply first argument: '),raw_input('Supply second argument :'))
mine(raw_input('Supply first argument: ')+'w',raw_input('Supply second argument :'))
mine(a+b,raw_input('Supply second argument:\n'))
# Ok I'd had enough by 8.
