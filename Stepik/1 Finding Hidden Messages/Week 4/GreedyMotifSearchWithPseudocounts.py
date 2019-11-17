from decimal import Decimal
from Motifs_module import ProfileWithPseudocounts, Score, Probability, ProfileMostProbablePattern

# Input:  A list of kmers Dna, and integers k and t (where t is the number of kmers in Dna)
# Output: GreedyMotifSearch(Dna, k, t)
def GreedyMotifSearchWithPseudocounts(Dna, k):
	t = len(Dna)
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

if __name__ == '__main__':
	with open("dataset_GreedyWithPseudocounts.txt") as file_input:
		content = file_input.readlines()

	firstLine = content[0].strip("\n").split(" ")
	k = int(firstLine[0])
	t = int(firstLine[1])
	Dna = []

	for DnaString in content[1::]:
		Dna.append(DnaString.strip("\n"))

	for motif in GreedyMotifSearchWithPseudocounts(Dna, k):
		print(motif)
