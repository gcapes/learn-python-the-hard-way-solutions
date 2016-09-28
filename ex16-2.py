# This script reads in a file passed as an argument on the command line
# To run the script type "python test.txt"

from sys import argv

script, filename = argv

print "This script will open the file %r and display its contents" % filename

# Open file read-only
inputfile=open(filename,'r')
contents=inputfile.read()

print "Your file is printed below: %s%s" % ('\n',contents)

print "And finally, we close it."
inputfile.close()
