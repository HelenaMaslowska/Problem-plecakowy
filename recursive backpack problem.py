import time
n = [8, 10, 15, 20, 25, 30, 40, 50, 75, 100]

def recpack(capacity, elem_in_house, n):
    if n == 0 or capacity == 0:
        return 0
    if elem_in_house[n - 1][0] > capacity: #zabezpiecza przed elementami o większej wadze niż aktualna poj plecaka (z dodatkowymi elementami)
        return recpack(capacity, elem_in_house, n - 1)
    else:
        return max(
            recpack(capacity - elem_in_house[n - 1][0], elem_in_house, n - 1) + elem_in_house[n - 1][1],    # z tym elementem
            recpack(capacity, elem_in_house, n - 1) )   #bez elementu


for another_data in range(2):
    for file in range(len(n)):
        if not another_data:
            in_file = open("data" + str(file) + ".txt", "r")
        else:
            in_file = open("data4.txt", "r")
        elem_in_house = []
        for line in in_file:  # dane elementow wkladanych do plecaka - elementy są unikalne, nie powtarzają się
            a, b = line.split()
            elem_in_house.append([int(a), int(b)])
        start_time = time.time()
        print(another_data, "rec", n[file], recpack(n[file], elem_in_house, len(elem_in_house)), "%s " % (time.time() - start_time))
