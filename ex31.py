print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

indicator = "> "
door = raw_input(indicator)

if door == "1":
	print "There's agiant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scraem at the bear."

	bear = raw_input(indicator)

	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. The bear runs away" % bear

elif door == "2":
	print "You stare into the endless abyss of stereytpe's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input(indicator)

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else:
	print "You stumble around and fall on a knife and die. Good job!"