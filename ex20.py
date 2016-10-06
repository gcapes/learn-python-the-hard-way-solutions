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
    print "line_count = %s" % line_count, f.readline(), # Add trailing comma 
    # to suppress new line after readline()

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
current_line += 1

# Print current line
print "current_line = %s" % current_line
print_a_line(current_line, current_file)

# Increment which line to print
current_line += 1
# Print current line
print "current_line = %s" % current_line
print_a_line(current_line, current_file)

# Study drills
# 1. Add comments for every line
# 2. Each time print_a_line is run, you are passing in a variable current_line. Write out what current_line is equal to on each function call, and trace how it becomes line_count in print_a_line.
# 3. Find each place a function is used, and check its def to make sure that you are giving it the right arguments.
# Looks fine to me.
# 4. Research online what the seek function for file does. Try pydoc file and see if you can figure it out from there. Then try pydoc file.seek to see what seek does.
# Seek rewinds the file
# 5. Research the shorthand notation += and rewrite the script to use += instead.
