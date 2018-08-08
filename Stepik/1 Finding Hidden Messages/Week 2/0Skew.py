def Skew(Genome):
    skew = {} #initializing the dictionary
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

skew = Skew("AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT")
print(' '.join([str(skew[i]) for i in skew.keys()]))