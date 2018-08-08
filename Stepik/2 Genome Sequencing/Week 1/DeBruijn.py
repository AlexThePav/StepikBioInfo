from Composition import composition
from Overlap_graph import overlap_graph

# Input: An integer k and a string Text.
# Output: DeBruijnk(Text), in the form of an adjacency list.
def debruijn(k, text):
    kmer_list = composition(k-1, text)
    adjacents = overlap_graph(kmer_list)



    return adjacents


print(debruijn(4, "AAGATTCTCTAAGA"))