# Input: A collection Patterns of k-mers.
# Output: The overlap graph Overlap(Patterns), in the form of an adjacency list. (You may return the nodes and their edges in any order.)
def overlap_graph(kmer_list):
    adjacents = {}

    for kmer in kmer_list:
        adjacents[kmer] = []
        kmer_suffix = kmer[1::]

        for candidate in kmer_list:
            candidate_prefix = candidate[0:len(candidate)-1]

            if kmer_suffix == candidate_prefix:
                adjacents[kmer].append(candidate)

        if len(adjacents[kmer]) == 0:
            del(adjacents[kmer])

    return adjacents


# ###INPUT###
# file_input = open("input.txt", "r+")
# kmers = [line.strip('\n') for line in file_input]
# file_input.close()
#
# print("Loading...")
# graph = overlap_graph(kmers)
#
#
# ###OUTPUT###
# f = open('output.txt', 'w')
#
# count = 0
# for i in graph:
#     if count < len(graph) - 1:
#         f.write("{} -> {}\n".format(kmers[count], ", ".join(graph[i][:])))
#         count += 1
#     else:
#         f.write("{} -> {}".format(kmers[count], ", ".join(graph[i][:])))
#         count += 1
# f.close()
#
# print("Done! See output.txt")
