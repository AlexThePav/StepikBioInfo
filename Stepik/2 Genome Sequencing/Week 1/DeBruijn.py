from Composition import composition


def pathGraph(k, text):
    kmer_list = composition(k, text)

    nodes = {}

    for kmer in kmer_list:
        kmer_prefix = kmer[0:k-1]
        nodes[kmer_prefix] = []

        for candidate in kmer_list:
            candidate_prefix = candidate[0:k-1]
            if kmer_prefix == candidate_prefix:
                nodes[kmer_prefix]\
                    .append(candidate[-k+1:])

    return nodes

###INPUT###


with open("dataset_199_6.txt", "r") as dataset_file:
    numk = int(dataset_file.readline())
    text = str(dataset_file.readline())

# file_input = open("dataset_199_6.txt", "r+")
# numk = int(file_input.readline())
# text = file_input.readlines()[0]
# file_input.close()

path_graph = pathGraph(numk, text)

###OUTPUT###

with open('output.txt', 'w') as output_file:
    count = 1
    for i in path_graph:
        print("{} -> {}".format(i, ", ".join(path_graph[i][:])), file=output_file)
#
# f = open('output.txt', 'w')
#
# count = 1
# for i in path_graph:
#     if count < len(path_graph):
#         f.write("{} -> {}\n".format(i, ", ".join(path_graph[i][:])))
#         count += 1
#     else:
#         f.write("{} -> {}".format(i, ", ".join(path_graph[i][:])))
#         count += 1
# f.close()

print("Done! See output.txt")
