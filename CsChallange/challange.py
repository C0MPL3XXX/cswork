
#Easy challange
list = [3, 6, 8, 10, 16, 19, 25, 28]

def print_values():
    for n in list:
        print(n)

#print_values()

#Medium challange

list2 = [1, 36, 146, 293, 333, 481, 526, 666, 846, 999]

def print_odd():
    list_odd = []
    for n in list2:
        if n % 2 == 1:
            list_odd.append(n)
    print(list_odd)

#print_odd()

#Hard challange
import random

list3 = []
for n in range(0, 10):
    n = random.randint(0, 1000)
    list3.append(n)

def hard_challange():

    print(list3)

    div_2 = []

    div_3 = []

    div_5 = []

    div_7 = []

    div_11 = []


    for n in list3:

        if n % 2 == 0:
            div_2.append(n)
        if n % 3 == 0:
            div_3.append(n)
        if n % 5 == 0:
            div_5.append(n)
        if n % 7 == 0:
            div_7.append(n)
        if n % 11 == 0:
            div_11.append(n)

    print('Numbers divisible by 2: ',
          div_2)
    print('Numbers divisible by 3: ',
          div_3)
    print('Numbers divisible by 5: ',
          div_5)
    print('Numbers divisible by 7: ',
          div_7)
    print('Numbers divisible by 11: ',
          div_11)

hard_challange()

#Hard challange remodeled

#prime_number = [2, 3, 5, 7, 11]

#for n in prime_number:
    #for y in list3:'
        #if y % n == 0:
            #print(y, 'is divisible by: ', n)
