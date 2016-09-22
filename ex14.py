from sys import argv

script, user_name, drink = argv #3. Add drink variable
prompt = '$ '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

#4. Understood multiline string containing % format activator
print """Fine whatever, this is a script so it doesn't like 
or dislike %s""" % drink 

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)

# Study drills
#1. Zork was a computer game. Adventure probably was too. Not going to play either.
#2. Replaced > with $ 
