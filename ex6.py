# Initialise a string, including the number using the format character for integer (%d=%i)
x = "There are %d types of people." % 10 # Uses a string inside a string
# Set string variable
binary = "binary"
# Assign another string
do_not = "don't"
# Assign string using %s the string format character
y= "Those who know %s and those who %s." %(binary, do_not) # Uses a string inside a string

# Display strings
print x
print y

# Display strings using string format characters %r and %s (repr() and str() respectively)
# repr() i.e. %r shows quote marks
print "I said: %r." % x # Uses a string inside a string

# str() i.e. %s doesn't display quote marks
print "I also said: '%s'." %y # Uses a string inside a string

# Set logical variable
hilarious = False
# Create string including the format character which is used during the print statement
# on line 28. Alternative code to get same result is given on lines 31 & 32.
joke_evaluation = "Isn't that joke so funny?! %r"

# Display strings
print joke_evaluation % hilarious

# Refactored code to better illustrate the format character %r
joke_evaluation = "Isn't that joke so funny?! "
print joke_evaluation + "%r" % hilarious

# Create more strings
w = "This is the left side of..."
e = "a string with a right side."

# Display one string followed by the other
print w + e

# Study drills:
# 1. Comment the code
# 2. Find strings within strings
    # There are four or five lines where there are strings within strings.
    # Depends if you count putting a number within a string. I would and so there are five.
# 3. How can I be sure?
    # You can be sure, by looking for the '%' character, the format character.
# 4. Explain use of + to make a longer string
    # + is used to concatenate strings as well as do addition.
