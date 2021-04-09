def gpt(a, b):
    if (4*a + b) % 26 == 2 and (19*a + b) % 26 == 15:
        return True

for i in range (0, 26):
    for j in range (0,26):
        if gpt(i,j):
            print("a=" + str(i) + "; b=" + str(j))
