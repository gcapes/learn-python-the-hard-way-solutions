tabby_cat = "\tI'm \'tabbed\' in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

for j in range(1,1000):
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,

# Study drills
#1. I'm not going to memorise all of them. I've got some of them in my head.
#2. Use triple single quote instead. Why would you do that?
# Single quote is easier to type. Maybe if your string was to start with
# double quotes the triple single quotes would be useful.
#3. Combine escape sequences
print '\a',"this is a bel"
print "this is not a bel"
print "This is a backspace","\b","end"
print "This %s is a double quote character %s" % ("\"",'"')
#4. Combine %r with double and single quote escapes
# In order to escape the % character you have to use %% instead of \%.
print "Single quotes using '%%r' %r " % "\'"
print "Single quotes %r" % '\'' 
print "Single quotes using '%%s' %s " % "\'"
print "Single quotes %s" % '\'' 
