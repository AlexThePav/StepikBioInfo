# Useful link: https://study.com/academy/lesson/how-okazaki-fragments-of-the-lagging-strand-dna-are-replicated.html

def Skew(Genome):
    skew = {} #initializing the dictionary
    newGenome = Genome + " "
    n = len(newGenome)
    # if newGenome[1] == "C":
    # 	skew[0] = -1
    # elif newGenome[1] == "G":
    # 	skew[0] = 1
    # else:
    # 	skew[0] = 0
    skew[0] = 0
    for i in range(0,n-1):
    	if newGenome[i] == "C":
    		skew[i+1] = skew[i]-1
    	elif newGenome[i] == "G":
    		skew[i+1] = skew[i]+1
    	else:
    		skew[i+1] = skew[i]
    return skew

def MinimumSkew(Genome):
  positions = [] # output variable
  skew = Skew(Genome)
  minSkew = min(skew.values())
  for i in range(len(skew)):
    if skew[i] == minSkew:
      positions.append(i)
  return positions
    
def FasterSymbolArray(Genome, symbol):
  array = {}
  n = len(Genome)
  ExtendedGenome = Genome + Genome[0:n//2]
  array[0] = PatternCount(symbol, Genome[0:n//2])
  for i in range(1, n):
    array[i] = array[i-1]
    if ExtendedGenome[i-1] == symbol:
      array[i] = array[i]-1
    if ExtendedGenome[i+(n//2)-1] == symbol:
      array[i] = array[i]+1
  return array

def FrequentWords(Text, k):
  FrequentPatterns = []
  Count = CountDict(Text, k)
  m = max(Count.values())
  for i in Count:
    if Count[i] == m:
      FrequentPatterns.append(Text[i:i+k])
  FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
  return FrequentPatternsNoDuplicates

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

# almost same as PatternCount, but replaced Text with Genome
def PatternMatching(Pattern, Genome):
  positions = [] # output variable
  for i in range(len(Genome)-len(Pattern)+1):
    if Genome[i:i+len(Pattern)] == Pattern:
      positions.append(i)
  return positions

def remove_duplicates(Items):
  ItemsNoDuplicates = list(set(Items))
  return ItemsNoDuplicates

def ApproximatePatternCount(Pattern, Text, d):
  positions = ApproximatePatternMatching(Pattern, Text, d)
  return len(positions)

def ApproximatePatternMatching(Pattern, Text, d):
  positions = [] # initializing list of positions
  t = len(Text)
  p = len(Pattern)
  for i in range(t-1):
    comparingText = Text[i:i+p]
    if len(Pattern) == len(comparingText):
      hDistance = HammingDistance(Pattern, comparingText)
      if hDistance <= d:
        positions.append(i)
    else:
      break
  return positions

def HammingDistance(p, q):
  count = 0
  for i in range(len(p)):
    if p[i] != q[i]:
      count += 1
  return count

if __name__ == "__main__":
  # Then, call your FrequentWords function, passing in oriC for Vibrio Cholerae for Text and 10 for k,
  # and store the result as a variable named words.
  # words = FrequentWords("ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC", 10)
  # print(words)

  # skew = MinimumSkew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT")
  # print(*skew,sep=" ")

  # print(HammingDistance("GGGCCGTTGGT", "GGACCGTTGAC"))
  approxPositions = ApproximatePatternMatching("GAGG", "TTTAGAGCCTTCAGAGG", 2)
  print(*approxPositions,sep=" ")
  approxCount = ApproximatePatternCount("CGCCTTT", "CAAATATCTCATAGGTGAACGTAGGACCTAGATTCTGAGTATACATAATGCAGTTCACCCCGTGTAGAATCCCTTGTCGGGGCGATCTGTTTTGGAGCGTGGATGTTTTTGTTAATCTTGTGGATAGAGACCGGCCTTCCGCCTTTGTCGACCTTTACAGCTGCTCTGGGATCGCTCTCTCTGCGGTGACAGCAAAAGCCCCATTCATACCCACGTTAGTTGCATTACCGGTTAGCGAGCAGCGCTCTCATGGCGTCTCGAAACCGACAGGTACCGCACAAGTCTATTGTACCACTCCTTCGTATTGCTTCGCAAACTGTAATAGTGGCGTTAGGCCAAAT", 3)
  print(approxCount)
  # Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
  # and store the output as a variable called positions
  # positions = PatternMatching("CTTGATCAT", v_cholerae)
  # print(positions)