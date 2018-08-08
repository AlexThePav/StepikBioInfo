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


# Copy your reverse function from the previous step here.
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

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

reverseC = ReverseComplement("GATTACA")
print(reverseC)