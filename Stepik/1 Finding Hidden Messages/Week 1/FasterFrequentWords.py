from Replication import remove_duplicates
from itertools import product

def allPossibleKMers(k):
  words = []
  letters = ["A", "C", "G", "T"]
  for word in product("".join(letters), repeat=k):
    words.append("".join(list(word)))
  return words

def PatternToNumber(Pattern):
  pass

def NumberToPattern(index, k):
  pass

def FasterFrequentWords(Text, k):
  allKmers = []
  for i in range(len(Text)-k+1):
    allKmers.append(Text[i:i+k])
  sortedKmers = sorted(remove_duplicates(allKmers))
  return sortedKmers

# print(FasterFrequentWords("AAGCAAAGGTGGG", 2))