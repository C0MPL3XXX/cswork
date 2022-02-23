grade = [20, 6, 38, 50, 40]
limit = 4

def store_class_mark():

    for counter1 in range(0, limit):
        min = counter1
        for counter2 in range(counter1 + 1, limit+1):
            if grade[counter2] < grade[counter1]:
                min = counter2
        if min != counter1:
            temporary = grade[min]
            grade[min] = grade[counter1]
            grade[counter1] = temporary

store_class_mark()
print(grade)



