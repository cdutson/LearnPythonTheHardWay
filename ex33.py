numbers = []

def loop(loopto, step):
	i = 0
	while i < loopto:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + step
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

loop(6, 1)

print "The numbers: "

for num in numbers:
	print num