from decimal import Decimal

# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearchWithPseudocounts(Dna, k, t):
	BestMotifs = []
	for i in range(0, t):
			BestMotifs.append(Dna[i][0:k])

	n = len(Dna[0])
	for i in range(0, n-k+1):
		Motifs = []
		Motifs.append(Dna[0][i:i+k])

		for j in range(1, t):
			P = ProfileWithPseudocounts(Motifs[0:j])
			Motifs.append(ProfileMostProbablePattern(Dna[j], k, P))

		if Score(Motifs) < Score(BestMotifs):
			BestMotifs = Motifs

return BestMotifs

# Copy all needed subroutines here.  These subroutines are the same used by GreedyMotifSearch(),
# except that you should replace Count(Motifs) and Profile(Motifs) with the new functions
# CountWithPseudocounts(Motifs) and ProfileWithPseudocounts(Motifs).


# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
	count = 0
	j = 0
	for i in range(len(p)):
		j = i
		if p[i] != q[j]:
			count += 1
	return count

# Copy your Score(Motifs), Count(Motifs), Profile(Motifs), and Consensus(Motifs) functions here.
# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    score = 0
    consensus = Consensus(Motifs)

    t = len(Motifs)

    for i in range(t):
    	hDist = HammingDistance(Motifs[i],consensus)
    	score = score + hDist

    return score

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

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
	k = len(Motifs[0])
	count = CountWithPseudocounts(Motifs)

	consensus = ""
	for j in range(k):
	    m = 0
	    frequentSymbol = ""
	    for symbol in count.keys():
	        if count[symbol][j] > m:
	            m = count[symbol][j]
	            frequentSymbol = symbol
	    consensus += frequentSymbol

	return consensus

# Then copy your ProfileMostProbablePattern(Text, k, Profile) and Pr(Text, Profile) functions here.
# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    p = 1
    t = len(Text)
    for i in range(t):
        p = p * Profile[Text[i]][i]

    return p

# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
def ProfileMostProbablePattern(Text, k, Profile):
	t = len(Text)
	maxCandidatePr = 0
	finalKmer = Text[0:k]

	for i in range(t-(k-1)):
		candidate = Text[i:i+k]
		candidatePr = Pr(candidate,Profile)

		if candidatePr > maxCandidatePr:
			maxCandidatePr = candidatePr
			finalKmer = candidate

	return finalKmer

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
# Copy the ten strings occurring in the hyperlinked DosR dataset below.
Dna = ["GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC",
 "CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG",
  "ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC",
   "GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC",
    "GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG",
     "CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA",
      "GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA",
       "GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG",
        "GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG",
         "TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"]

testDna = ["GGCGTTCAGGCA",
 "AAGAATCAGTCA",
  "CAAGGAGTTCGC",
   "CACGTCAATCAC",
    "CAATAATATTCG"]

# set t equal to the number of strings in Dna and k equal to 15
t = len(Dna)
k = 15

testT = len(testDna)
testK = 3

# Call GreedyMotifSearch(Dna, k, t) and store the output in a variable called Motifs
Motifs = GreedyMotifSearchWithPseudocounts(Dna, k, t)
#Motifs = GreedyMotifSearchWithPseudocounts(testDna, testK, testT)

# Print the Motifs variable
print(Motifs)

# Print Score(Motifs)
print(Score(Motifs))
