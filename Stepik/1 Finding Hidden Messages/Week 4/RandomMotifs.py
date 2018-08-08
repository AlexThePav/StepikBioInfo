# import Python's 'random' module here
import random

# Input:  A list of strings Dna, and integers k and t
# Output: RandomMotifs(Dna, k, t)
# HINT:   You might not actually need to use t since t = len(Dna), but you may find it convenient
def RandomMotifs(Dna, k, t):
    strings = []
    l = len(Dna[0])

    for i in range(t):
    	randomIndex = random.randint(0,l-k)
    	strings.append(Dna[i][randomIndex:randomIndex + k])

    return strings


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
Dna = ["TTACCTTAAC",
 "GATGTCTGTC",
  "ACGGCGTTAG",
   "CCCTAACGAG",
    "CGTCAGAGGT"]
k = 3
t = 5
print(RandomMotifs(Dna,k,t))