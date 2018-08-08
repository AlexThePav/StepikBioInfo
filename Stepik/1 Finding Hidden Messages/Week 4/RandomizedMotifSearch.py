# import the random package here
import random
from decimal import Decimal

# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch(Dna, k, t):
    #M = RandomMotifs(Dna, k, t)
    M = ["TGA", "GTT", "GAA", "TGT"]
    BestMotifs = M


    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna)
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 


# Insert necessary subroutines here, including RandomMotifs(), ProfileWithPseudocounts(), Motifs(), Score(),
# and any subroutines that these functions need.
def HammingDistance(p, q):
    count = 0
    j = 0
    for i in range(len(p)):
        j = i
        if p[i] != q[j]:
            count += 1
    return count

def RandomMotifs(Dna, k, t):
    strings = []
    l = len(Dna[0])

    for i in range(t):
        randomIndex = random.randint(0,l-k)
        strings.append(Dna[i][randomIndex:randomIndex + k])

    return strings

# Input:  A set of kmers Motifs
# Output: CountWithPseudocounts(Motifs)
# HINT:   You need to use CountWithPseudocounts as a subroutine of ProfileWithPseudocounts
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

# Input:  A profile matrix Profile and a list of strings Dna
# Output: Motifs(Profile, Dna)
def Motifs(Profile, Dna):
    pMotifs = []

    t = len(Dna)
    k = len(Profile['A'])

    for i in range(t):
        pMotifs.append(ProfileMostProbablePattern(Dna[i], k, Profile))

    return pMotifs

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

# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Pr(Text, Profile):
    p = 1
    t = len(Text)
    for i in range(t):
        p = p * Profile[Text[i]][i]

    return p

# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    score = 0
    count = CountWithPseudocounts(Motifs)
    consensus = Consensus(Motifs)

    t = len(Motifs)

    for i in range(t):
        hDist = HammingDistance(Motifs[i],consensus)
        score = score + hDist

    return score

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
    k = len(Motifs[0])
    count = CountWithPseudocounts(Motifs)

    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol

    return consensus
### DO NOT MODIFY THE CODE BELOW THIS LINE ###
# def RepeatedRandomizedMotifSearch(Dna, k, t):
#     BestScore = float('inf')
#     BestMotifs = []
#     for i in range(1000):
#         Motifs = RandomizedMotifSearch(Dna, k, t)
#         CurrScore = Score(Motifs)
#         if CurrScore < BestScore:
#             BestScore = CurrScore
#             BestMotifs = Motifs
#     return BestMotifs
# import sys
# lines = sys.stdin.read().splitlines()
# k,t = lines[0].split()
# k = int(k)
# t = int(t)

#print('\n'.join(RepeatedRandomizedMotifSearch(lines[1:],k,t)))

Dna = ["TGACGTTC",
 "TAAGAGTT",
  "GGACGAAA",
   "CTGTTCGC"]

print(RandomizedMotifSearch(Dna, 3, 4))