from Replication import remove_duplicates

def allPossibleKmers(k):
  firstWord = "A" * k
  words = [firstWord] * (4**k)
  wordsIndex = 0
  letters = ["A", "C", "G", "T"]
  lettersIndex = 1
  words[0] = firstWord
  i = k-1

  for word in words[1::]:
    wordsIndex += 1

    if words[wordsIndex] < words[wordsIndex-1]:
      wordToList = list(words[wordsIndex])
      wordToList[i] = letters[lettersIndex]
      words[wordsIndex] = "".join(wordToList)
    else:
      words[wordsIndex] = "ELSE"
    

    if lettersIndex < 3:
      lettersIndex += 1
    else:
      lettersIndex = 0

    if i > 0:
      i -= 1
    else:
      i = k-1

  return words

print(allPossibleKmers(4))

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