from Replication import remove_duplicates, HammingDistance
from ReverseComplement import ReverseComplement
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
  for i in range(0,len(Text)-k+1):
    pattern = Text[i:k+i]
    j = PatternToNumber(pattern)
    frequencyArray[j] += 1
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
    if HammingDistance(Suffix(Pattern), text) < d:
      for x in nucleotides:
        x += text
        neighborhood.append(x)
    else:
      textWithNucleotide = FirstSymbol(Pattern) + text
      neighborhood.append(textWithNucleotide)
  return neighborhood

def ComputeFrequenciesWithMismatches(Text, k, d):
  frequencyArray = [0] * (4**k)
  allPatterns = []
  for i in range(0,len(Text)-k+1):
    pattern = Text[i:k+i]
    neighborhood = Neighbors(pattern, d)
    for approximatePattern in neighborhood:
      j = PatternToNumber(approximatePattern)
      frequencyArray[j] += 1
      jToPattern = NumberToPattern(j, k)
      allPatterns.append(jToPattern)
  return frequencyArray

def FrequentWordsWithMismatches(Text, k, d):
  frequentPatterns = []
  frequencyArray = ComputeFrequenciesWithMismatches(Text, k, d)
  maxCount = max(frequencyArray)
  pattern = ""
  for i in range(0, 4**k-1):
    if frequencyArray[i] == maxCount:
      pattern = NumberToPattern(i, k)
      frequentPatterns.append(pattern)
  return frequentPatterns

def FrequentWordsWMismRevComplements(Text, k, d):
  frequentPatterns = []
  TextRC = ReverseComplement(Text)
  frequencyArray = [0] * (4 ** k)
  frequencyArraySP = ComputeFrequenciesWithMismatches(Text, k, d)
  frequencyArrayRC = ComputeFrequenciesWithMismatches(TextRC, k, d)
  for i in range(0, 4**k-1):
    frequencyArray[i] = frequencyArrayRC[i] + frequencyArraySP[i]
  maxCount = max(frequencyArray)
  pattern = ""
  for i in range(0, 4**k-1):
    if frequencyArray[i] == maxCount:
      pattern = NumberToPattern(i, k)
      frequentPatterns.append(pattern)
  return frequentPatterns


if __name__ == "__main__":
  # print(" ".join(FasterFrequentWords("ATTTAATTCTAAT", 3)))
  # print(PatternToNumber("TTTGAAAACTCCGTA"))
  # print(NumberToPattern(5437,8))
  # print(ComputeFrequenciesWithMismatches("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1))
  # print(ComputeFrequencies("ACCACCGAGGAGGTGTGATGATATTGGTA", 3))
  # print((" ".join(FrequentWordsWithMismatches("GCGGATTATTGATTGATTATTGGCGGATTGGTCGCGGGCGGATTGCGGATTGATTGAGAGGTCGTCAGAGGTCATTGCGGATTAGAGAGAGAGAGGCGGGCGGATTGATTAGAGGCGGAGAGATTGAGAGATTATTGATTGGTCAGAGATTATTATTGCGGGTCATTGATTGCGGATTATTGATTGATTGCGGATTGCGGGCGGATTGATTATTATTAGAGATTGTCATTGGTCATTATTGCGGGTCATTGATTGTCAGAGATTGGTCAGAGATTGGTCGCGGATTGAGAGATTATTAGAGGCGGATTATTGATTGGTCGTCGCGGATTGATTGGTCGTCATTGATTGCGGGCGGAGAGATTAGAG", 6, 2))))

  print(" ".join(FrequentWordsWMismRevComplements("CAAGCCTAGCACAGAGAGCACAGAGGAGCAAATGAGCCTAATAGCAAATAATCCTAATCCTAATAATAGAATCCTGAGCACAAATAGAGCCTGAGCCTCAAGAGCCTAATAGAATGAGGAGGAGAGCAAATCCTGAGAATCCTCAGAGAATCCTAGAGAATGAGCCTAATGAGAATCCTGAGGAGAGAGAATAGAATCAAGAATGAGCAAGAATAGCACAAGGAGAGAATCAAG", 7, 3)))