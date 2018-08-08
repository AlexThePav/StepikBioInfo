# Input: A sequence of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols of Patterni are equal to the first k-1 symbols of Patterni+1 for 1 ≤ i ≤ n-1.
# Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni  (for 1 ≤ i ≤ n).
def reconstruction(kmer_list):

    reconstructed_genome = kmer_list[0]
    kmer_length = len(kmer_list[0])

    for kmer in kmer_list[1::]:
        reconstructed_genome += kmer[kmer_length-1]
    return reconstructed_genome

###INPUT###
file_input = open("input.txt", "r+")
kmers_from_file = [line.strip('\n') for line in file_input]
file_input.close()

txt = reconstruction(kmers_from_file)

###OUTPUT###
f = open('output.txt', 'w')
f.write(txt)
f.close()