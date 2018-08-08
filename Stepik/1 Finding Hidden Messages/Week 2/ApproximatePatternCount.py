# Input:  Strings Pattern and Text, and an integer d
# Output: The number of times Pattern appears in Text with at most d mismatches
def ApproximatePatternCount(Pattern, Text, d):
    count = 0 # initialize count variable
    t = len(Text)
    p = len(Pattern)
    for i in range(t-1):
    	comparingText = Text[i:i+p]
    	if len(Pattern) == len(comparingText):
	    	hDistance = HammingDistance(Pattern, comparingText)
	    	if hDistance <= d:
	    		count += 1
    return count


# Insert your HammingDistance function on the following line.
def HammingDistance(p, q):
	count = 0
	j = 0
	for i in range(len(p)):
		j = i
		if p[i] != q[j]:
			count += 1
	return count

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
print(ApproximatePatternCount("GTGCCG","AGCGTGCCGAAATATGCCGCCAGACCTGCTGCGGTGGCCTCGCCGACTTCACGGATGCCAAGTGCATAGAGGAAGCGAGCAAAGGTGGTTTCTTTCGCTTTATCCAGCGCGTTAACCACGTTCTGTGCCGACTTT",3))