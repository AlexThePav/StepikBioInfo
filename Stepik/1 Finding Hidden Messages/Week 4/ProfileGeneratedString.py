# first, import the random package
import random

# then, copy Pr, Normalize, and WeightedDie below this line
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

	print(Probabilities.keys())

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
import sys
it,Text,profile,k = sys.stdin.read().splitlines()
it = int(it)
profile = eval(profile)
k = int(k)
print('\n'.join([ProfileGeneratedString(Text,profile,k) for i in range(it)]))