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
  symbol = Pattern[l]
  prefix = Pattern[:l]
  return 4 * PatternToNumber(prefix) + SymbolToNumber(symbol)

def NumberToSymbol(index):
  symbol = "A"
  if index == 1:
    symbol = "C"
  elif index == 2:
    symbol = "G"
  elif index == 3:
    symbol = "T"
  return symbol

def NumberToPattern(index, k):
  if k == 1:
    return NumberToSymbol(index)
  prefixIndex = index // 4
  r = index % 4
  symbol = NumberToSymbol(r)
  PrefixPattern = NumberToPattern(prefixIndex, k-1)
  return PrefixPattern + symbol

def ComputeFrequencies(Text, k):
  frequencyArray = [0] * (4**k)
  frequenciesJoined = ""
  for i in range(0,len(Text)-k+1):
    pattern = Text[i:k+i]
    j = PatternToNumber(pattern)
    frequencyArray[j] += 1
  for frequency in frequencyArray:
    frequenciesJoined = frequenciesJoined + str(frequency)
  # return "".join(frequenciesJoined)
  return frequencyArray

def FasterFrequentWords(Text, k):
  frequentPatterns = []
  frequencyArray = ComputeFrequencies(Text, k)
  maxCount = max(frequencyArray)
  pattern = ""
  for i in range(0, 4**k-1):
    if frequencyArray[i] == maxCount:
      pattern = NumberToPattern(i, k)
      frequentPatterns.append(pattern)
  return frequentPatterns
if __name__ == "__main__":
  print(" ".join(FasterFrequentWords("ATTTAATTCTAAT", 3)))
# print(PatternToNumber("TTTGAAAACTCCGTA"))
# print(NumberToPattern(5437,8))