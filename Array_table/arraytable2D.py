Temp = [[10, 11, 12, 13, 10],
        [10, 13, 14, 12, 12]]
Month = 0
City = 0

def month_and_city():
    for Month in range(0, 2):
        print(str(Month + 1), " Month")
        for City in range(0, 5):
            print("City ", str(City + 1), str(Temp[Month][City]))

month_and_city()
