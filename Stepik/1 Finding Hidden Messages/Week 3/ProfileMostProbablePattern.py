# Insert your Pr(Text, Profile) function here from Motifs.py.
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
print(ProfileMostProbablePattern('TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA',
	5,
	{'A': [0.2, 0.2, 0.3, 0.2, 0.3],
	'C': [0.4, 0.3, 0.1, 0.5, 0.1], 
	'G': [0.3, 0.3, 0.5, 0.2, 0.4], 
	'T': [0.1, 0.2, 0.1, 0.1, 0.2]}))