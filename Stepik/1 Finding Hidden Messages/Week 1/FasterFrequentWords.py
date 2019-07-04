from Replication import remove_duplicates
from itertools import product

def SymbolToNumber(symbol):
  x = 0
  if symbol == "C":
    x = 1
  elif symbol == "G":
    x = 2
  elif symbol == "T":
    x = 3
  return x

def PatternToNumber(Pattern):
  l = len(Pattern) - 1
  if len(Pattern) == 0:
    return 0
  patternToList = list(Pattern)
  symbol = Pattern[l]
  prefix = Pattern[:l]
  return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)
  


def NumberToPattern(index, k):
  pass

def FasterFrequentWords(Text, k):
  allKmers = []
  for i in range(len(Text)-k+1):
    allKmers.append(Text[i:i+k])
  sortedKmers = sorted(remove_duplicates(allKmers))
  return sortedKmers

print(PatternToNumber("TTTGAAAACTCCGTA"))