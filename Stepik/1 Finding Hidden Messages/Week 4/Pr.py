def Pr(Text, Profile):
    p = 1

    t = len(Text)
    for i in range(t):
    	p = p * Profile[Text[i]][i]

    return p

Profile = {"A" : [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],
"C": [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],
"G": [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],
"T": [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}

Text = "AAGTTC"

print(Pr(Text, Profile))