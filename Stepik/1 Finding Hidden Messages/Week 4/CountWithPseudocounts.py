# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
def CountWithPseudocounts(Motifs):
	count = {}

	t = len(Motifs)
	k = len(Motifs[0])
    
    #range over all nucleotides symbol and create a list of zeroes corresponding to count[symbol].
	for symbol in "ACGT":
		count[symbol] = []
		for j in range(k):
			count[symbol].append(1)

	#range over all elements symbol = Motifs[i][j] of the count matrix and add 1 to count[symbol][j].
	for i in range(t):
    for j in range(k):
      symbol = Motifs[i][j]
      count[symbol][j] += 1

	return count


if __name__ == '__main__':
		
	### DO NOT MODIFY THE CODE BELOW THIS LINE ###
	print(CountWithPseudocounts(["AACGTA",
	 "CCCGTT",
	  "CACCTT",
	   "GGATTA",
	    "TTCCGG"]))