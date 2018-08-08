# Input: An integer k and a string Text.
# Output: Compositionk(Text) (the k-mers can be provided in any order).
def composition(k, text):
    kmer_list = []
    t = len(text)

    for i in range(0, t-k):
        kmer_list.append(text[i:i+k])

    return kmer_list


Text = "TTTTAAGCGATGTTACATAGAGCATAAGTGACCGCTTTAACCTCACCTTTACACCCATGTTCGACCCTCCATACAGTTACTGAGGTAACTCTACCGAGTCGTATGTAACCACCTCCCTCCCAGAGGCCAACTGCACGGGTTATAAAGGGACCCATGTTCGTTCGTTCCGAGCAGCCCAGGAAGCTCCAACCTCTCCCGTTCAAGCAGGTATGTGCGCGTTGCTTATAGACAGTCGCAATATTGGATTCTTTCGTAGAGGCCGCTGGTAGATGATTATCTGCCTAAATAGAAAAACTGCGTTAACCTGATGAGCTCTCACATCCTTGACCGTCTGTAGTATCCGGCTGAGATGTTTTTTCAGCGGATAAGTGGGTCAGTAAGGAATGACAATACGCAAAGGCTCTCAGCCGAGAGCTATTCACGATCCCATTACTCTAATGGAGTTGGCATCTGTATTATTGATTAGGGCCTGTGGTAAAACCAAGGGTGCCAACCATGGAGGCTCATCTCGATTTTTATGTCTCTGTTTCTCGTGCCAAATGGGTCACATAGTGTAAAACAGGGTACCACGTAACTCGATACATTTACATCGGCCTTAAGCGACGTCCCTAAATATTATACCTACGTCTTGGCCCATCTGTTTTGATCGAAAAGCTTCGAGAGCTACCACGGGAGGTGACGACCGGTCCTACGGGGTTTTATTTGGTTAATATCGAAGACGCTTAAAGGACTGCCCCCCGCGATGGACGTACGCTTAGTCCTTTACGTGGTGACGGGGGCGCTATTAGCGAACTCGCAAGTCGGCGCAGATGCAATACAGAACGTACATGTAGGATGAGCTTACCTGACGCCACGCCGAGCCAGCTTGCGTGTTCCTTACTATGTATTATGAAGACTCTACCCTCTTTCGGTGTTGTAGCGCACCCCTAACTTCTATCGTCTTCGGCGGAAGTAACTATGACTCGTACGACCTCAAGCCTATTGGCACCCAAATGTGAGCTCTTGACCCCTCAACAACGTCCATCGCATCCTAGAGTTGTTACCGGTGTGTAGGCGGCATGCCGCGCTGCGGCCAGGATAGACGCCCGAGTATCCGGACGTTCCCTTCCGCTCCCACTCTATCTGCCTGTCAATGCTATGGAAGGGGGTCCACGCCTGAACTCCTACGAGCGATGAGAGTGTAATGCGTGAGTAGTGACCCTGTCTTAACTCCAGTCTCTGCAATATGAGGTAATAGGGCACGATATAACCAGGGGGTACGCAACTCTGTCTAGTGCAATGCGTCGGTGACGGTCTTGTTCCACAGGGGACCGGGAGTTGGTTTGCGATCCGCAGAAGTCTCGGCGGAGTGGAATCAACCAAGTACCTTTCACTAGTCCGTTCTCCCCTTCTGCATATGTATCTAAGGCAAGCCCTGAGTCGCCACGGGAAAGCAGCTTACAGCCGTTTGCGTCAGCTGCCATCAGCCTTCGGAATGGGAGGATTCAGTGGCATTTGTTAATAAGGAAGCCAGGGCGAATGATCGATGTTCCAGTGAAAGACCTCCGTGCCTCAAGTATTACACAATCGGAAAACAAGCGTCTCGCCGTCCGGCTTACGCCCGCTCAGACCGTTCTCCTTGTGTGAACTAGGACAAGTAGATGTTTTCCCTTAGGCGTGCCATTTAGGGGTATAGCGGGCTACCCTGACAATACAAGGTCACCTTCACTAGCGCTTAAATGCAGCAAAGGATTGCGAGGGGCTAAACATAGCACCTGAAGAGCTAGTTACGTCGGTGAGGGACGGTACGTTGCCGAGGGGAATATATGACAGACCTTGGGGGTGTGAATCGTCAGTCAAAACCAGCCTTGCTCAAGTGGGAGCTGGCTTGGCGCCATTATCTGGGGCGCTTCCAGGCGTGGTTTCTGCAATCCGAACCCTAAGGATCCATACTGATTAAACAAGGACCGGCCACCCAGGTTGAGTAAACACAGTCTCATGAGACGGGATATGCAATTAGCATTTCTACCCTGAAACTCCAGCGCGCTAGGTAAGTGGCGCATTCGAACTGCGTAGCGGAGCGGAGTACACCAGCCTAATTCTGGCTACCTAAATAACAAGTCTCTGTCAGTGCTCTACCTAACACTTTGAAAAACCCGCTCTAGAACAGGAAGCTCATAGGCTAGCATATGAAATTCGTTGCGTTCACAGGTTGCATCGGAAGCCGTCAGGCGTTTGGTGTCCGTCATCTAACGACATCTTCAAAAGTGGCTTGGAAGCTTTTTCTCGTCGGCAAGAGCCATACATCAACTTGCAGCTCCAAGGGTAACGGTTCTATGCAGATTCGAGCGTCGATCGTACACCGGAATCGGCGAAGAATGTGCATAAAGATTCATTCCGAGGTATGAGCCCTAACGACAACTCGAAACGCCGCACTAATACGTATTAGCTTGACCACCTCGCTACATATACTTGCGAACACGGTGGATTCTGGTAATCATGCTCGGCTAGTGGCCCCCTCTGCACGCGTCTCGAGTTTAAGAGATATCGGTGCTTGTTAAGATCCCTTAGCCTCCTAGCATTCTACCGCTGAAGTCTATCTCCTTCGACCAAAGGAGATACGGATTTGCGAAATTTATATCAAATGCCAGGAGGTCTCAGAATACAAAATGACGCTGGACCGCGTAAGGAAGATTATCGAGCGCGAGGATCTGCTATGTGAGGACCACAAAGGCGTGTCATGGGGCAGTCCAACAACGTATGATATATACTTTCAATGCGGGATGACAGGATAGCAGAGGGTCGGCGATACAACCATGCACGACTGTGAAGGAATTTACTCTTGGACCATAGCAACGACGACCCAATCCACTTGCATTTGCCCCGCGGGGACTGTCAATGGACAGTTGTCAGGTAACCGGTGTCTATTTGGGAGGTGCTCTGTTCTAATTGGTACATCTAAAACTACGAGGTATTCTCTAGGTAAAAACCACCAATGCTCAGTTTTCGCGCACGTCTAGAACGCATGTCCTGCTTAACCCCGCTAGAAAACAAAGGCTCTTGGGGGTAAGCGGATACGACCGGGGTTACGGTACTACCGCAGCTACCGCACTCCACAATATCCTATCGCGGGAGACACTTGGGGCATAGCACGCTCGCCCTGTTAATTCATAATGAGTAATTTAAACGCTAAAAGCCATTCCGATCGTGTGTATGATCAAGATGGAGCCATGCCAGCACGTTATCTGGACCCAAACGACTATAGAGTTCCCCCACTTTACTGTTAATTGTACCCCAGCCTATAAAGGATGAAAACACAAGATCACTACCAGTGGAAGCAAGGAGGCCGGGGCTCGCTCTTGGATGTCAATGAAGCTTATCGATTTCAGATCCTTAGTGCGCATGTAGGGTGCTTACTGAAATAACTGAAAGCTATTACACCAGGACACCCAGGATCAGGCGCTCTTAGACTGAGATCACACCCCCCAGATCCCCGCGGGGGATTACAGTCCGCGTAGCTCAAGAAGCGCACTATTCCTTTAGGGCGGGACACGGTTGTGGCAAATAGTTCCGAGCAGTGTTATATCTCCTGAGGACTCTCTGAACATGACCGAAAAGGGGCGGAGGGTCCGAATTGTATACCCTGCGCTCTAGGAAGGCTTCTGTACGACTTTGCGTAGGTATAATGCAGATGTTGCTTGGTGGCGATCCTAGGACGACATCACCCCGCAATAGTATAAGCTTTTCGGGTTTATGCTCTCATCAATTTCTCCCGTGGGCTGCCTTTCATATCACTTTGGAACGGACGGAGTGTGAGAAACCCTCGCCCATCTGAGTTATGATAGCTACGAGGGTGCTTAACAAAATGAGGACCGTTACTAGGTCTTCTAAGCGGGTAGTCGCCGGTGTTCCTAAAGTAATGAACGCGAGCCCCTGGAAGAGAAGGGTCTAAACGGCGCCATAATGCGAATATTCGGGATTAATAGTCTGAGTCAGGGTTACCGTACACATCTATAGACCGAACTCGATTTTTAAGCATTCTCGATATCCCTGAAGTAACGACGGATCCCACGATCCTGTTAAACAACCGATTGCATTAAAGTGGTTACACTCTTTACATCTACTGAGCGGCGAGTACGTCGTAATGTTGCGACAACTGGATGGTTGCGGGTCCGTGCCGTCCCACCGCCACCACAAGATATACAGCCTCCATCGCCGTCAGGGCCTTTGGATAGTCCGAATTCTATTAAGTCGCTTGTGGTGTTCTTTTGTTTACCCCTGGCAACTGATAGTCGCGGTGTTCCTGCCTCCGGCGGCTTTGGCTATCAGCGATCGCTCGGTGTCTATCTAGTGATTTATCGGGAGGATTTGGAGAAGCGTGCGTCGATTGATTGCGATTTCGATGTTCTTGTTGTCCCGGCCGATGGGGGAACGCGTATATCCACGACCAGCCTCAAGCTGCATTCCTCTTTGAAGCATGAAATTATGTCATTCACTGTCGATACCTGCTTTACGTGGAACGGTACAGGACGTCGGGCTCGTTATTGAGGCGCACCATGTCTAGGATGGATGGCCACGGGCTAAGACGTTCATATAAAGCTAATGTACAACTGATCCTCACGACGTCGAAACGGGCAAGCATCTTCAAAAAATGCCCTGATGATCATTTCAACCAGACTCGCCGCATCAGCGCAACGGCGGGAGATCCGGCAGAGACTAAATGGCTAAATGGGCCGGCATCGTATTCGCCCCATACTACTGGAGATAATATACGGAACTTCGAGCGAGGGTCGTCACAAATCAATCGACGTAACGACGCGCTCGTATTGCTCGAGCATTAGTACCGCAGTGCCTTACTTGATATGACTCTCTCTATGAGCTACTTCCGTCGAAGATTGCGTTCGCTAGGCTCGAGTCGTGTGTGTCGCCATCAACGTCTCAGTGTCTATCAGGTCCAGGTACCGCATTGTATCTCACCAGACCGCACTCTGGAGGTGGACGAAATTTGAGTCAGATAACAA "
K = 100

txt = '\n'.join(composition(K, Text))
f = open('output.txt', 'w')
f.write(txt)
f.close()
