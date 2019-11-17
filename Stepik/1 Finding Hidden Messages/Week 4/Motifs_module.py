from decimal import Decimal

# Insert your Count(Motifs) function here.
def Count(Motifs):
  count = {} # initializing the count dictionary
  k = len(Motifs[0])
  for symbol in "ACGT":
    count[symbol] = []
    for j in range(k):
    	count[symbol].append(0)
  t = len(Motifs)
  for i in range(t):
    for j in range(k):
      symbol = Motifs[i][j]
      count[symbol][j] += 1
  return count

def CountWithPseudocounts(Motifs):
  count = {}

  t = len(Motifs)
  k = len(Motifs[0])
  for symbol in "ACGT":
  	count[symbol] = []
  	for j in range(k):
  		count[symbol].append(1)
  for i in range(t):
    for j in range(k):
      symbol = Motifs[i][j]
      count[symbol][j] += 1
  return count

# Input:  A set of kmers Motifs
# Output: ProfileWithPseudocounts(Motifs)
def ProfileWithPseudocounts(Motifs):
  profile = {}
  t = len(Motifs)
  k = len(Motifs[0])
  count = CountWithPseudocounts(Motifs)

  for symbol in count.keys():
    profile[symbol] = []
    for j in range(k):
      profile[symbol].append(float(Decimal(count[symbol][j])/(t+4)))

  return profile

# Input:  A set of kmers Motifs
# Output: A consensus string of Motifs.
def Consensus(Motifs):
  k = len(Motifs[0])
  count = Count(Motifs)
  consensus = ""

  for j in range(k):
    m = 0
    frequentSymbol = ""
    for symbol in "ACGT":
      if count[symbol][j] > m:
        m = count[symbol][j]
        frequentSymbol = symbol
    consensus += frequentSymbol

  return consensus

# Input:  A list of kmers Motifs
# Output: the profile matrix of Motifs, as a dictionary of lists.
def Profile(Motifs):
	profile = {}
	t = len(Motifs)
	k = len(Motifs[0])
	count = Count(Motifs)

	for symbol in count.keys():
		profile[symbol] = []
		for j in range(k):
			profile[symbol].append(float(round(Decimal(count[symbol][j])/t,1)))

	return profile

# Input:  String Text and profile matrix Profile
# Output: Pr(Text, Profile)
def Probability(Text, Profile):
    p = 1
    t = len(Text)
    for i in range(0,t):
        p = p * Profile[Text[i]][i]

    return p

# Input:  String Text, an integer k, and profile matrix Profile
# Output: ProfileMostProbablePattern(Text, k, Profile)
def ProfileMostProbablePattern(Text, k, Profile):
	t = len(Text)
	maxCandidatePr = 0
	finalKmer = Text[0:k]

	for i in range(0,t-k):
		candidate = Text[i:i+k]
		candidatePr = Probability(candidate,Profile)

		if candidatePr > maxCandidatePr:
			maxCandidatePr = candidatePr
			finalKmer = candidate

	return finalKmer

def Skew(Genome):
  skew = {} #initializing the dictionary
  newGenome = Genome + " "
  n = len(newGenome)
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
  positions = ApproximatePatternPositions(Pattern, Text, d)
  return len(positions)

def ApproximatePatternPositions(Pattern, Text, d):
  positions = [] # initializing list of positions
  t = len(Text)
  p = len(Pattern)
  for i in range(t-p):
    comparingText = Text[i:i+p]
    hDistance = HammingDistance(Pattern, comparingText)
    if hDistance <= d:
      positions.append(i)
  # positionsNoDupes = remove_duplicates(positions)
  return positions

def HammingDistance(p, q):
  distance = 0
  for i in range(len(p)):
    if p[i] != q[i]:
      distance += 1
  return distance

def Score(Motifs):
  score = 0
  count = Count(Motifs)
  consensus = Consensus(Motifs)
  t = len(Motifs)
  for i in range(t):
  	hDist = HammingDistance(Motifs[i],consensus)
  	score = score + hDist
  return score

def ApproximateCountDict(Text, k, d):
  counts = {}
  for i in range(len(Text)-k+1):
    pattern = Text[i:i+k]
    counts[i] = ApproximatePatternCount(pattern, Text, d)
  return counts

def FrequentWordsWithMismatches(Text, k, d):
  frequentWords = []
  count = ApproximateCountDict(Text, k, d)
  print(count)
  m = max(count.values())
  for i in count:
    if count[i] == m:
      frequentWords.append(Text[i:i+k])
  frequentWordsNoDupes = remove_duplicates(frequentWords)
  return frequentWordsNoDupes

# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
  revComp = '' # output variable
  comp = ''
  compPattern = ''
  for nuc in Pattern:
    comp = complement(nuc)
    compPattern = compPattern + comp
  revComp = reverse(compPattern)
  return revComp

def reverse(text):
  return text[::-1]

# HINT:   Filling in the following function is optional, but it may come in handy when solving ReverseComplement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Nucleotide):
  comp = '' # output variable
  original = Nucleotide
  if original == 'T':
    comp = 'A'
  elif original == 'A':
    comp = 'T'
  elif original == 'C':
    comp = 'G'
  elif original == 'G':
    comp = 'C'
  return comp

def motif_entropy(motifs):
  df = pd.DataFrame(index=np.arange(len(motifs)), columns=np.arange(len(motifs[0])))
  for i, seg in enumerate(motifs):
    for j, n in enumerate(seg):
      df.iloc[i,j] = n
    
  entropy = 0
  for i in range(df.shape[1]):
    for p in df[i].value_counts(normalize=True).values:
      entropy -= p*np.log2(p)
    
  return entropy

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

def DistancePatternStrings(Pattern, Dna):
  k = len(Pattern)
  distance = 0
  for text in Dna:
    hammingDistance = float("inf")
    for i in range(0,len(text)-k+1):
      kmer = text[i:i+k]
      hammingDistanceKmerPattern = HammingDistance(kmer, Pattern)
      if hammingDistance > hammingDistanceKmerPattern:
        hammingDistance = hammingDistanceKmerPattern
    distance += hammingDistance
  return distance

def MedianString(k, Dna):
  distance = float("inf")
  median = ""
  for i in range(0,4**k-1):
    pattern = NumberToPattern(i, k)
    distancePatternDna = DistancePatternStrings(pattern, Dna)
    if distance > distancePatternDna:
      distance = distancePatternDna
      median = pattern
  return median