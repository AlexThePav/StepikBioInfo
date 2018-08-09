from Composition import composition
from Overlap_graph import overlapGraph

# Input: An integer k and a string Text.
# Output: DeBruijnk(Text), in the form of an adjacency list.


def pathGraph(k, text):
    kmer_list = composition(k, text)
    print(text)
    edges = overlapGraph(kmer_list)

    for edge in edges:
        print("{} -> {}".format(edge, ",".join(edges[edge][:])))


    nodes = {}

    edge_count = 0
    for edge in edges:
        edge_suffix_left = edge[-k+1:]
        edge_prefix_left = edge[0:k-1]
        nodes[edge_prefix_left] = []
        edge_values_list = list(edges.values())

        for edge_right_list in edge_values_list[edge_count:]:

            is_right_prefix = False
            is_right_suffix = False

            for edge_right_kmer in edge_right_list:
                edge_prefix_right = edge_right_kmer[0:k-1]
                edge_suffix_right = edge_right_kmer[-k+1:]

                if edge_suffix_left == edge_prefix_right:
                    is_right_prefix = True

                if edge_suffix_left == edge_suffix_right:
                    is_right_suffix = True

            if is_right_prefix == True and len(nodes[edge_prefix_left]) == 0:
                nodes[edge_prefix_left].append(edge_prefix_right)

            if is_right_suffix == True:
                nodes[edge_prefix_left].append(edge_suffix_right)

        edge_count += 1

    print("=" * 40)

    sorted_nodes = sorted(nodes)

    for node in sorted_nodes:
        print("{} -> {}".format(node, ",".join(nodes[node][:])))


    return edges


path_graph = pathGraph(3, "CTCTA")

# print("\nTAATGCCATGGGATGTT\n")

