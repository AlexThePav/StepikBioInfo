def PatternCount(Pattern, Text):
  count = 0
  for i in range(len(Text)-len(Pattern)+1):
      if Text[i:i+len(Pattern)] == Pattern:
          count = count+1
  return count 

if __name__ == "__main__":
  patternC = PatternCount("GCCTCCAGC", "ACGCCTCCACGCCTCCAGCCTCCATGCCTCCAGCCTCCAGCCTCCAAGCCTCCAGCCTCCAAGGAGCCTCCAGCCTCCAGCCTCCAGCCTCCAAGCCTCCAGCCTCCATATCGGCCTCCATGCCTCCAGTAATATCTAGGCCTCCAAAGCCTCCACTTGCCTCCAATAGCCTCCATGCCTCCATTGTAAAGCCTCCAGACGCCTCCAGCCTCCATGCCTCCAACGCCTCCATGCCTCCACCCGTGCCTCCAAATTATATACTCAGCGTTTGAAGCCTCCATAGGCCTCCAGCCTCCAAGCCTCCATAGCCTCCAGTTCGCGCCTCCATAGTTAGCAGCCTCCAAAGCCTCCAGCCTCCAGGCTGGCCTCCAGCCTCCAGCCTCCAATCTTGGCCTCCAGCCTCCATTGGCCTCCATTTCTGCCGCCTCCAGGGCCTCCATCTTAGCCTCCAAGCCGCCTCCACGCATAATAGAGTGCCTCCAAGTTCGCAAGCCTCCACGGCGCCTCCACGATACGCCTCCAGCCTCCAGTGAGCCTCCATCCGCCTCCATGGAGTGTAGGCCTCCAGGGCCTCCATGCCTCCAAGCCTCCAGCCTCCAGCCTCCATCGCCTCCAGTGCGAAAGTTGCCTCCATTACTAGCCTCCATGGGCTGGCCTCCAGAGCCTCCAGTCAGACCCTGCCTCCAGCCTCCAGGCCTCCAGCCTCCAGCCTCCAGTGAGGCCTCCATCGCCTCCACGCCTCCAGGCCTCCAGCCTCCAGGCCTCCAGCCTCCAAGCCTCCAGGCCTCCACGATCCCAGCCTCCAAGCCTCCACCCATGATTACACCGCCTCCAGGCCTCCACGCCTCCAGGCCTCCAGAAGCCTCCAAGCAGCCTCCATCCTAGACCAGCCTCCAGCCTCCACCCGCCTCCAAAGCCTCCAGCCTCCAGTGAAGCCTCCAGCCTCCAGCCTCCATTGCCTCCAGCCTCCAAGAGCCTCCATTGCCTCCAAACGCCTCCAGGCCTCCATCCGGCCTCCAACGCCTCCAAGCGCCTCCAGCCTCCAGCCTCCAGCCTCCAGCCTCCA")
  print(patternC)