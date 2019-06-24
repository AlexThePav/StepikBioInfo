from PatternCount import PatternCount

def CountDict(Text, k):
  Count = {}
  for i in range(len(Text)-k+1):
    Pattern = Text[i:i+k]
    Count[i] = PatternCount(Pattern, Text)
    # print("i: {0}, Pattern: {1}, Count[i]: {2}".format(i, Pattern, Count[i]))
  return Count

if __name__ == "__main__":
  print(CountDict("ACGTACGTACGT", 3))