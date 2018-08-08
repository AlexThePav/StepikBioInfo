def Skew(Genome):
    skew = {} #initializing the dictionary
    n = len(Genome)
    if Genome[0] == "C":
    	skew[0] = -1
    elif Genome[0] == "G":
    	skew[0] = 1
    else:
    	skew[0] = 0
    for i in range(1,n):
    	if Genome[i] == "C":
    		skew[i] = skew[i-1]-1
    	elif Genome[i] == "G":
    		skew[i] = skew[i-1]+1
    	else:
    		skew[i] = skew[i-1]
    return skew

skew = Skew("AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT")
print(' '.join([str(skew[i]) for i in skew.keys()]))