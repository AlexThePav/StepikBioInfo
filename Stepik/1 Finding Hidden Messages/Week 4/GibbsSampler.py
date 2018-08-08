# first, import the random package
import random
from decimal import Decimal

# Input:  Integers k, t, and N, followed by a collection of strings Dna
# Output: GibbsSampler(Dna, k, t, N)
def GibbsSampler(Dna, k, t, N):
    BestMotifs = [] # output variable
    Motifs = RandomMotifs(Dna, k, t)
    BestMotifs = Motifs

    for j in range(0,N):
        i = random.randint(0,t-1)

        MotifsToProfile = Motifs
        removedMotif = Motifs[i]
        Motifs.remove(Motifs[i])

        Profile = ProfileWithPseudocounts(Motifs)
        Motifs.insert(i, removedMotif)
        Motifs[i] = ProfileGeneratedString(Dna[i], Profile, k)

        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs
    
    return BestMotifs

# place all subroutines needed for GibbsSampler below this line

# Copy your Consensus(Motifs) function here.
def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)

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

def HammingDistance(p, q):
    count = 0
    j = 0
    for i in range(len(p)):
        j = i
        if p[i] != q[j]:
            count += 1
    return count

# Copy your Count(Motifs) function here.
def Count(Motifs):
    count = {} # initializing the count dictionary

    #range over all nucleotides symbol and create a list of zeroes corresponding to count[symbol].
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
             count[symbol].append(0)

    #range over all elements symbol = Motifs[i][j] of the count matrix and add 1 to count[symbol][j].
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1

    return count

# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
    score = 0
    count = Count(Motifs)
    consensus = Consensus(Motifs)
    t = len(Motifs)

    for i in range(t):
        hDist = HammingDistance(Motifs[i],consensus)
        score = score + hDist

    return score

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

# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)
# HINT:   You might not actually need to use t since t = len(Dna), but you may find it convenient
def RandomMotifs(Dna, k, t):
    strings = []
    l = len(Dna[0])

    for i in range(t):
        randomIndex = random.randint(0,l-k)
        strings.append(Dna[i][randomIndex:randomIndex + k])

    return strings

def WeightedDie(Probabilities):
    kmer = '' # output variable
    p = random.uniform(0, 1)
    ranges = {}
    rangeStart = 0
    i = 0

    rangeKmers = {}
    ri = 0

    probIndex = 1

    for symbol in Probabilities:
        rangeKmers[ri] = symbol
        ri += 1

    for symbol in Probabilities.keys():
        ranges[i] = rangeStart + Probabilities[symbol]
        rangeStart = ranges[i]
        i += 1

    if p <= ranges[0]:
        kmer = rangeKmers[0]

    for symbol in Probabilities:
        if (p > ranges[probIndex-1]) and (p <= ranges[probIndex]):
            kmer = rangeKmers[probIndex]
        probIndex += 1

    return kmer

def Pr(Text, Profile):
    p = 1

    t = len(Text)
    for i in range(t):
        p = p * Profile[Text[i]][i]

    return p

def Normalize(Probabilities):
    newProbs = {}
    sum = 0.0

    for symbol in Probabilities.keys():
        sum = sum + Probabilities[symbol]   
    
    for symbol in Probabilities.keys():
        newProbs[symbol] = Probabilities[symbol] / sum

    return newProbs

# Input:  A string Text, a profile matrix Profile, and an integer k
# Output: ProfileGeneratedString(Text, profile, k)
def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}

    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)

    probabilities = Normalize(probabilities)
    return WeightedDie(probabilities)

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
def RepeatedGibbsSampler(Dna, k, t, N):
    BestScore = float('inf')
    BestMotifs = []
    for i in range(100):
        Motifs = GibbsSampler(Dna, k, t, N)
        CurrScore = Score(Motifs)
        if CurrScore < BestScore:
            BestScore = CurrScore
            BestMotifs = Motifs
    return BestMotifs
#import sys
#lines = sys.stdin.read().splitlines()
#k,t,N = lines[0].split()
k = 8
t = 5
N = 100
Dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
 "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
  "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
   "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
    "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
print('\n'.join(RepeatedGibbsSampler(Dna,k,t,N)))
#print('\n'.join(GibbsSampler(Dna,k,t,N)))