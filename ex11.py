print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
            age, height, weight)
print "Formatted height %s" % height

# 1. raw_input() gets input from the prompt
# 2. Other ways to use it
name=raw_input("What is your name? ")
print "Hello, %s." % name
# 3. New form
quest=raw_input("What is your quest? ") # to seek the holy grail
favouritecolour=raw_input("What is your favourite colour? ")
print "Right then %s, off you go %s" % (name, quest)
#4. The apostrophe is escaped because the format character is %r and the
# example input (6'2") contains a mixture of single and double quotes.
# %r presents the string literally as it would have to be typed - either
# "6'2\"" or '6\'2"'
# Python's preference is for single quotes so it prints the former.
