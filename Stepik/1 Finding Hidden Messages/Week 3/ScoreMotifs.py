# Copy your Consensus(Motifs) function here.
def Consensus(Motifs):
	k = len(Motifs[0])
	count = Count(Motifs)

	consensus = ""
	for j in range(k):
	    m = 0
	    frequentSymbol = ""
	    for symbol in "ACGT":
	        if count[symbol][j] > m:
	            m = count[symbol][j]
	            frequentSymbol = symbol
	    consensus += frequentSymbol

	return consensus

def HammingDistance(p, q):
	count = 0
	j = 0
	for i in range(len(p)):
		j = i
		if p[i] != q[j]:
			count += 1
	return count

# Copy your Count(Motifs) function here.
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

# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    score = 0
    count = Count(Motifs)
    consensus = Consensus(Motifs)
    t = len(Motifs)

    for i in range(t):
    	hDist = HammingDistance(Motifs[i],consensus)
    	score = score + hDist

    return score

if __name__ == "__main__":
	### DO NOT MODIFY THE CODE BELOW THIS LINE ###
	print(Score(["AACGTA","CCCGTT","CACCTT","GGATTA","TTCCGG"]))

