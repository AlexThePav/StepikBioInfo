# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
	positions = [] # output variable
	skew = Skew(Genome)
	minSkew = 0
	for i in range(len(skew)):
		if skew[i] < minSkew:
			minSkew = skew[i]
	for i in range(len(skew)):
		if skew[i] == minSkew:
			positions.append(i)
	return positions

# Input:  A String Genome
# Output: Skew(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def Skew(Genome):
    skew = {} # output variable
    newGenome = " " + Genome
    n = len(newGenome)
    if newGenome[1] == "C":
    	skew[0] = -1
    elif newGenome[1] == "G":
    	skew[0] = 1
    else:
    	skew[0] = 0
    for i in range(1,n):
    	if newGenome[i] == "C":
    		skew[i] = skew[i-1]-1
    	elif newGenome[i] == "G":
    		skew[i] = skew[i-1]+1
    	else:
    		skew[i] = skew[i-1]
    return skew


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
print(' '.join([str(i) for i in MinimumSkew("CATTCCAGTACTTCGATGATGGCGTGAAGA")]))