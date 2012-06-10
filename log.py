#!/usr/bin/python

import random

def main():
	MATCH = 1
	LIMIT = 100 # number of samples
	lines = [] # collection of lines
	seen = 1 # keep track of how many we've seen

	# take a range for this example, but the actual size shouldn't be known
	for i in range(100000):
		if seen <= LIMIT:
			upper = 1
		else:
			upper = int(1/(float(LIMIT)/seen))
		
		# random number for first LIMIT lines will always be picked
		if random.randint(1, upper) == MATCH:
			if seen <= LIMIT:
				lines.append(i) # append to always guarantee LIMIT lines
			else:
				# replace random other line
				pos = random.randrange(0,LIMIT)
				#print "replace position %s with %s" % (pos, i)
				lines[pos] = i
		seen += 1

	print lines
	print len(lines)	

if __name__ == '__main__':
	main()
