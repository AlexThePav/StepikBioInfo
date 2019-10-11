import pandas as pd
import numpy as np

# tested input motifs were in list form
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



Motifs1 = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]

print(motif_entropy(Motifs1))