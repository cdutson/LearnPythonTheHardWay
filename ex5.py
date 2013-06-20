name = "Corey A. Dutson"
age = 27 # not a lie
height = 71 # inches
calculated_height = height * 2.54 # in cm
weight = 171 # lbs
calculated_weight = weight * 0.453592 # in kg
eyes = 'Green'
teeth = 'Yellowish'
hair = 'Red'

print "Let's talk about %s." % name
print "He's %d inches tall, which is %f cm" % (height, calculated_height)
print "He's %d pounds heavy, which is %f kg." % (weight, calculated_weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s" % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)