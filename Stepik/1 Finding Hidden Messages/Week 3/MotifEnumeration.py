# Try if you really want, highly impractical however

# MotifEnumeration(Dna, k, d)
#         Patterns ← an empty set
#         for each k-mer Pattern in Dna
#             for each k-mer Pattern’ differing from Pattern by at most d mismatches
#                 if Pattern' appears in each string from Dna with at most d mismatches
#                     add Pattern' to Patterns
#         remove duplicates from Patterns
#         return Patterns

# Sample Input:

# 3 1
# ATTTGGC
# TGCCTTA
# CGGTATC
# GAAAATT
# Sample Output:

# ATA ATT GTT TTT
def HammingDistance(p, q):
	count = 0
	j = 0
	for i in range(len(p)):
		j = i
		if p[i] != q[j]:
			count += 1
	return count

def MotifEnumeration(Dna, k, d):
  Patterns = []
  i = 0
  for kmer in Dna[i:k]:
    