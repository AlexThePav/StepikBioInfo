# Insert your Count(Motifs) function here from the last Code Challenge.
from decimal import Decimal

def Count(Motifs):
	count = {} # initializing the count dictionary

	#range over all nucleotides symbol and create a list of zeroes corresponding to count[symbol].
	k = len(Motifs[0])
	for symbol in "ACGT":
	    count[symbol] = []
	    for j in range(k):
	         count[symbol].append(0)

	#range over all elements symbol = Motifs[i][j] of the count matrix and add 1 to count[symbol][j].
	t = len(Motifs)
	for i in range(t):
	    for j in range(k):
	        symbol = Motifs[i][j]
	        count[symbol][j] += 1

	return count

# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
	profile = {}
	t = len(Motifs)
	k = len(Motifs[0])
	count = Count(Motifs)

	for symbol in count.keys():
		profile[symbol] = []
		for j in range(k):
			#x = Decimal(count[symbol][j]) / k
			#rounded = round(x,1)
			#roundedF = float(round(x,1))
			profile[symbol].append(float(round(Decimal(count[symbol][j])/t,1)))

	return profile


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
motifs = ["AACGTA","CCCGTT","CACCTT","GGATTA","TTCCGG"]
print(Profile(motifs))