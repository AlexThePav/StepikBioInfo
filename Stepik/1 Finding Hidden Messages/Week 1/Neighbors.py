from Replication import HammingDistance

def ImmediateNeighbors(Pattern):
  neighborhood = []
  nucleotides = list("ACGT")
  for i in range(0,len(Pattern)):
    symbol = Pattern[i]
    for x in nucleotides:
      if x != symbol:
        neighbor = Pattern
        neighborToList = list(neighbor)
        neighborToList[i] = x
        neighbor = "".join(neighborToList)
        neighborhood.append(neighbor)
  neighborhood.append(Pattern)
  return neighborhood

def FirstSymbol(Pattern):
  return Pattern[0]

def Suffix(Pattern):
  return Pattern[1::]

def Neighbors(Pattern, d):
  nucleotides = list("ACGT")
  if d == 0:
    return [Pattern]
  if len(Pattern) == 1:
    return nucleotides
  neighborhood = []
  suffixNeighbors = Neighbors(Suffix(Pattern), d)
  for text in suffixNeighbors:
    if HammingDistance(Suffix(Pattern), text) == d:
      for x in nucleotides:
        textWithNucleotide = text
        x += textWithNucleotide
        neighborhood.append(x)
    else:
      textWithNucleotide = FirstSymbol(Pattern) + text
      neighborhood.append(textWithNucleotide)
  return neighborhood

print(" ".join(Neighbors("CGGTGTAA", 3)))
# print(ImmediateNeighbors("CAA"))