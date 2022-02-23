

def binary_search():
    Values = [11, 12, 15, 16, 112, 118, 123, 145]
    Target = 112
    Min = 0
    High = 7

    Answer = 0
    Mid = 0
    Found = False
    while Found == False and Min <= High:
        Mid = ((Min + High)/2)
        if Values[int(Mid)] == Target:
            Found = True
            Answer = int(Mid)
        elif Target > Values[int(Mid)]:
            Min = Mid + 1
        else:
            High = Mid - 1

    if Found == True:
        print(str(Target), "found at array index", str(Answer))
    else:
        print(str(Target), "was not found")

binary_search()

