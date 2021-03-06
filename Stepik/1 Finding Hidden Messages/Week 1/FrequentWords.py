from Replication import remove_duplicates

def CountDict(Text, k):
  Count = {} # output variable
  for i in range(len(Text)-k+1):
    Pattern = Text[i:i+k]
    Count[i] = PatternCount(Pattern, Text)
  return Count

def PatternCount(Pattern, Text):
  count = 0 # output variable
  for i in range(len(Text)-len(Pattern)+1):
    if Text[i:i+len(Pattern)] == Pattern:
      count = count+1
  return count 

def FrequentWords(Text, k):
  FrequentPatterns = []
  Count = CountDict(Text, k)
  m = max(Count.values())
  for i in Count:
    if Count[i] == m:
      FrequentPatterns.append(Text[i:i+k])
  FrequentPatternsNoDupes = remove_duplicates(FrequentPatterns)
  return FrequentPatternsNoDupes


if __name__ == "__main__":
  frequentW = FrequentWords("ATTTAATTCTAAT", 3)
  print(" ".join(frequentW))