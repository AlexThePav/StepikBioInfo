from Replication import HammingDistance

def ImmediateNeighbors(Pattern):
  neighborhood = []
  for i in range(0,len(Pattern)-1):
    symbol = Pattern[i]
    for x in Pattern:
      if x != symbol:
        neighbor = Pattern
        neighborToList = list(neighbor)
        neighborToList[i] = x
        neighbor = "".join(neighborToList)
        neighborhood.append(neighbor)
  return neighborhood

def FirstSymbol(Pattern):
  return Pattern[0]

def Suffix(Pattern):
  return Pattern[1::]

def Neighbors(Pattern, d):
  nucleotides = list("ACGT")
  neighborhood = []
  if d == 0:
    return Pattern
  if len(Pattern) == 1:
    return nucleotides
  suffixNeighbors = Neighbors(Suffix(Pattern), d)
  print(Pattern, Suffix(Pattern))
  print("suffixNeighbors", suffixNeighbors)
  for text in suffixNeighbors:
    if HammingDistance(Suffix(Pattern), text) < d:
      for x in nucleotides:
        text += x
        neighborhood.append(text)
    else:
      text += FirstSymbol(Pattern)
      neighborhood.append(text)
  return neighborhood

print(Neighbors("ACG", 1))
