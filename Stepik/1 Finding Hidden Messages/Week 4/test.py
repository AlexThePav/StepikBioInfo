import random

probabilities = {
	"A" : 0,
	"B" : 0,
	"C" : 0
}

for i in range(100):
	y=random.randint(1,10)
	if y>=1 and y < 3:
	    print("A")
	    probabilities["A"] += 1
	elif y>=3 and y<=7:
	    print("B")
	    probabilities["B"] += 1
	else: 
		print("C")
		probabilities["C"] += 1

print(probabilities)

