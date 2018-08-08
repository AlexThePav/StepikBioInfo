def MinimumSkew(Genome):
    positions = [] # output variable
    skew = Skew(Genome)
    minSkew = 0
    for i in range(len(skew)):
        if skew[i] < minSkew:
            minSkew = skew[i]
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
    count = 0 # initialize count variable
    t = len(Text)
    p = len(Pattern)
    for i in range(t-1):
        comparingText = Text[i:i+p]
        if len(Pattern) == len(comparingText):
            hDistance = HammingDistance(Pattern, comparingText)
            if hDistance <= d:
                count += 1
    return count

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
    return positions

def HammingDistance(p, q):
    count = 0
    j = 0
    for i in range(len(p)):
        j = i
        if p[i] != q[j]:
            count += 1
    return count

# Then, call your FrequentWords function, passing in oriC for Vibrio Cholerae for Text and 10 for k,
# and store the result as a variable named words.
words = FrequentWords("ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC", 10)
print(words)

# Call PatternMatching with Pattern equal to "CTTGATCAT" and Genome equal to v_cholerae,
# and store the output as a variable called positions
positions = PatternMatching("CTTGATCAT", v_cholerae)
print(positions)