# Input: A dictionary Probabilities, where keys are k-mers and values are the probabilities of these k-mers (which do not necessarily sum up to 1)
# Output: A normalized dictionary where the probability of each k-mer was divided by the sum of all k-mers' probabilities
def Normalize(Probabilities):
	newProbs = {}
	sum = 0.0

	print(Probabilities.keys())

	for symbol in Probabilities.keys():
		sum = sum + Probabilities[symbol]	
	
	for symbol in Probabilities.keys():
		newProbs[symbol] = Probabilities[symbol] / sum

   	return newProbs


### DO NOT MODIFY THE CODE BELOW THIS LINE ###
probs = {'A': 0.15, 'C': 0.6, 'G': 0.225, 'T': 0.225, 'F': 0.3}
print(Normalize(probs))