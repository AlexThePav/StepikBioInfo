from Replication import HammingDistance
from FasterFrequentWords import NumberToPattern

def DistancePatternStrings(Pattern, Dna):
  k = len(Pattern)
  distance = 0
  for text in Dna:
    hammingDistance = float("inf")
    for i in range(0,len(text)-k+1):
      kmer = text[i:i+k]
      hammingDistanceKmerPattern = HammingDistance(kmer, Pattern)
      if hammingDistance > hammingDistanceKmerPattern:
        hammingDistance = hammingDistanceKmerPattern
    distance += hammingDistance
  return distance

def MedianString(k, Dna):
  distance = float("inf")
  median = ""
  for i in range(0,4**k-1):
    pattern = NumberToPattern(i, k)
    distancePatternDna = DistancePatternStrings(pattern, Dna)
    if distance > distancePatternDna:
      distance = distancePatternDna
      median = pattern
  return median

#Input for MedianString
fo = open("dataset_158_9.txt", "r+")
k = int(fo.readline())
Dna = []
for line in fo:
  Dna.append(line.strip())
fo.close()
print(k)
print(Dna)

#Input for DistancePatternStrings
# fDist = open("dataset_5164_1.txt", "r+")
# content = fDist.readlines()
# Pattern = content[0].strip()
# Dna = []
# word = ""
# for letter in content[1].strip():
#   if letter != " ":
#     word += letter
#   elif letter == " " or letter is None:
#     Dna.append(word)
#     word = ""
# Dna.append(word)
# fDist.close()

# print(DistancePatternStrings("AAA", ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]))
# print(DistancePatternStrings(Pattern, Dna))
# print(MedianString(k, Dna))
# print(k)
# print(Dna)
print(MedianString(k, Dna))