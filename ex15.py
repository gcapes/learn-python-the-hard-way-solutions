# import argv from sys module
from sys import argv

# Create variables containing strings from arguments provided on the command line
script, filename = argv

# Open file and give it a local reference. This isn't a string but has a "file" type.
txt = open(filename)

# Print the file name
print "Here's your file %r:" % filename
# Print contents of file
print txt.read()
# 7. Close the file
txt.close()

#4.
# print "Type the filename again:"
# file_again = raw_input("> ")
# 
# txt_again = open(file_again)
# 
# print txt_again.read()

# 5.
# Getting the file name from the command line is better because
# you can use tab completion. This reduces error massively.
