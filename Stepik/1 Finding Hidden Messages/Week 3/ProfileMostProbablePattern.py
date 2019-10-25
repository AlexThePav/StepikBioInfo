# Insert your Pr(Text, Profile) function here from Motifs.py.
# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def ProfileProduct(Text, Profile):
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
		candidatePr = ProfileProduct(candidate,Profile)

		if candidatePr > maxCandidatePr:
			maxCandidatePr = candidatePr
			finalKmer = candidate

	return finalKmer

# fo = open("dataset_Profile.txt", "r+")
#
# fo.close()

with open("dataset_Profile.txt") as file_input:
	content = file_input.readlines()
content = [x.strip() for x in content]
Dna = content[0]
k = content[1]
ACGTs = {'A': [], 'C': [], 'G': [], 'T': []}
print(ACGTs.values())
print(ACGTs.keys())
contentCount = 2
for nucleotide in ACGTs.values():
	nucleotide.append(list(content[contentCount], " "))
	contentCount += 1
print(ACGTs)

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
# print(ProfileMostProbablePattern('TTACCATGGGACCGCTGACTGATTTCTGGCGTCAGCGTGATGCTGGTGTGGATGACATTCCGGTGCGCTTTGTAAGCAGAGTTTA',
# 	5,
# 	{'A': [0.2, 0.2, 0.3, 0.2, 0.3],
# 	'C': [0.4, 0.3, 0.1, 0.5, 0.1], 
# 	'G': [0.3, 0.3, 0.5, 0.2, 0.4], 
# 	'T': [0.1, 0.2, 0.1, 0.1, 0.2]}))