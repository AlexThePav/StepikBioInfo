# Input:  A set of kmers Motifs
# Output: Count(Motifs)
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
	        # print("symbol = " + symbol)
	        count[symbol][j] += 1

	return count


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
motifs = ["AACGTA","CCCGTT","CACCTT","GGATTA","TTCCGG"]
print(Count(motifs))