def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# Study drills
# 1. Return returns a value to the calling function or script.
# 2. age=30+5, height=78*4, weight=90*2, iq=100/2
# 3. I think this means break the functions so multiply doesn't multiply (or something)? Unclear so skipping.
# 4. Formula:
# Result = (((23+5)/2)-4)*15
print "(((23+5)/2)-4)*15 = %d" % multiply(subtract(divide(add(23,5),2),4),15)
