N = [2, 9, 5, 6, 7, 8]
X = 9
Found = False
Counter = 0

for Counter in range(0, 5):
    if N[Counter] == X:
        Found = True
        print(str(N[Counter]), "found at position", str(Counter))

    if Found == False:
        print(str(X), "not found")

