# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Pattern, Text, d):
    positions = [] # initializing list of positions
    t = len(Text)
    p = len(Pattern)
    for i in range(t-1):
    	comparingText = Text[i:i+p]
    	if len(Pattern) == len(comparingText):
	    	hDistance = HammingDistance(Pattern, comparingText)
	    	if hDistance <= d:
	    		positions.append(i)
    return positions


# Insert your Hamming distance function on the following line.
def HammingDistance(p, q):
	count = 0
	j = 0
	for i in range(len(p)):
		j = i
		if p[i] != q[j]:
			count += 1
	return count

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
print(' '.join([str(i) for i in ApproximatePatternMatching("CCA","CCACCT",0)]))