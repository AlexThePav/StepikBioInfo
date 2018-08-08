from decimal import Decimal

# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
# HINT:   You need to use CountWithPseudocounts as a subroutine of ProfileWithPseudocounts
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

# Input:  A set of kmers Motifs
# Output: ProfileWithPseudocounts(Motifs)
def ProfileWithPseudocounts(Motifs):
	profile = {}
	t = len(Motifs)
	k = len(Motifs[0])
	count = CountWithPseudocounts(Motifs)

	for symbol in count.keys():
		profile[symbol] = []
		for j in range(k):
			#x = Decimal(count[symbol][j]) / t
			#rounded = round(x,1)
			#roundedF = float(round(x,1))
			profile[symbol].append(float(Decimal(count[symbol][j])/(t+4)))

	return profile


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
motifs = ["AACGTA","CCCGTT","CACCTT","GGATTA","TTCCGG"]
print(ProfileWithPseudocounts(motifs))