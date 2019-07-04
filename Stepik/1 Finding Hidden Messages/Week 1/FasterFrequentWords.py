from Replication import remove_duplicates
from itertools import product

def allPossibleKMers(k):
  #way too slow
  words = []
  letters = ["A", "C", "G", "T"]
  for word in product("".join(letters), repeat=k):
    words.append("".join(list(word)))
  return words

def PatternToNumber(Pattern):
  L = len(Pattern)
  print(len(Pattern))
  allKmers = allPossibleKMers(L)
  for kmer in allKmers:
    print(kmer)
    if kmer == Pattern:
      terms = []
      for letter in kmer:
        if letter == "A":
          x = 0
        elif letter == "C":
          x = 1
        elif letter == "G":
          x = 2
        elif letter == "T":
          x = 3
        y = len(kmer[letter::])
        terms.append(x*(4**y))
      index = sum(terms)

  return index
  


def NumberToPattern(index, k):
  pass

def FasterFrequentWords(Text, k):
  allKmers = []
  for i in range(len(Text)-k+1):
    allKmers.append(Text[i:i+k])
  sortedKmers = sorted(remove_duplicates(allKmers))
  return sortedKmers

print(allPossibleKMers(13))
print(PatternToNumber("AAGC"))