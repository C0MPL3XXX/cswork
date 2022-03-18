import random

#Challenge easy
list = []

duplicate = {}

for n in range(0, 10):
    n = random.randint(0,10)
    list.append(n)

def counting_dup():
    for u in list:
        duplicate[u] = list.count(u)

    print(duplicate)

#counting_dup()

#Challange Medium
