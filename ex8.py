# String to contain formatting characters
formatter = "%r %r %r %r"

# Print integers using formatter string
print formatter % (1,2,3,4)
# Print strings using formatter string
print formatter % ("one","two","three","four")
# Print boolean values using formatter string
print formatter % (True,False,False,True)
# Print the formatter string four times
print formatter % (formatter,formatter,formatter,formatter)
# Print four strings
print formatter % (
        "I had this thing.",
        "That you could type up right.",
        "But it didn't sing.",
        "So I said goodnight."
        )

# You can just continue the command on a new line it seems, without a line continuation
# character. Just so long as you don't break the line in the middle of a string.
print formatter % ("I had this thing.","That you could type up right.", "But it didn't sing.", 
"So  I said goodnight."
        )

# Study drills
#1. Comment code
#2. Output of last line uses single and double quotes because it contains an apostrophe.
# repr() i.e. %r puts single quotes around the string, unless the string contains
# single quotes (i.e. an apostrophe) already.
