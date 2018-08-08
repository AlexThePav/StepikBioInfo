# Insert your Count(Motifs) function here.
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

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
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


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
print(Consensus(["AAGCTA","AAGTGA","AAGCCA","AGGTCA","TCGCGA", "AGGTGA"]))