'''
	Reverse Compliment Genome Generator
	By Ronald Randolph
	September 2019

	This program generates and returns the reverse compliment 
	of a given genome to an output file "p3_output.fasta"
'''

import sys

#argument check
if(len(sys.argv) != 2):
	print 'Usage: rev_comp.py [filename]'
	sys.exit(1)

#open file and split lines into a list
file = sys.argv[1]

with open(file) as f:
	data = f.read().splitlines()

#1. update/store header of data
h = data[0].split()
h[0] = ">reversed"
header = ' '.join(h)

#2. remove old header and reverse data
data.pop(0)
data.reverse()
data.pop(0)

with open("p3_output.fasta","w+") as f:

	f.write(header)
	f.write("\n")
	
	#3. reverse and compliment  each line
	for line in data:
		tmp = list(line)
		tmp.reverse()
	
		index = 0
		for char in tmp:
			if (char == 'A'):
				tmp[index] = 'T'
			elif (char == 'T'):
				tmp[index] = 'A'
			elif (char == 'C'):
				tmp[index] = 'G'
			else:
				tmp[index] = 'C'
			index += 1

		rev = ''.join(tmp)
		f.write(rev)
		f.write("\n")
