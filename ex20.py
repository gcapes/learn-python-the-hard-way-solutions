# import command line argument function from sys module
from sys import argv

# Assign command line arguments to variables
script, input_file = argv

# Function to read file and print it
def print_all(f):
    print f.read()

# Rewind file to beginning
def rewind(f):
    f.seek(0)

# Print current line from the file
def print_a_line(line_count, f):
    # Modify output to explicitly display line_count for comparision against
    # value of current_line which is passed in when this function is called.
    print "line_count = %s" % line_count, f.readline() 

# Create local variable for input_file
current_file = open(input_file)

print "First let's print the whole file:\n"

# Call print all function
print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
# Print current line
print "current_line = %s" % current_line
print_a_line(current_line, current_file)

# Increment which line to print
current_line = current_line + 1
# Print current line
print "current_line = %s" % current_line
print_a_line(current_line, current_file)

# Increment which line to print
current_line = current_line + 1
# Print current line
print "current_line = %s" % current_line
print_a_line(current_line, current_file)
