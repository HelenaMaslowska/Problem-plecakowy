import time
n = [8, 10, 15, 20, 25, 30, 40, 50, 75, 100] #poj plecaka

wmax = 0
pmax = 0

for another_data in range(2):
    for file in range(len(n)):
        if not another_data:
            in_file = open("data" + str(file) + ".txt", "r")
        else:
            in_file = open("data4.txt", "r")
        in_house = []
        for line in in_file:  # dane elementow wkladanych do plecaka - elementy są unikalne, nie powtarzają się
            a, b = line.split()
            in_house.append([int(a), int(b)])
        start_time = time.time()
        rows = len(in_house) + 1
        columns = n[file] + 1
        giant_tab = [[0 for _ in range(columns)] for _ in range(rows)]

        for i in range(1, rows):
            for j in range(1, columns):
                if in_house[i-1][0] >= 0 and j-in_house[i-1][0] >= 0:
                    giant_tab[i][j] = max(giant_tab[i-1][j], giant_tab[i-1][j-in_house[i-1][0]] + in_house[i-1][1])
                else:
                    giant_tab[i][j] = giant_tab[i-1][j]
        #for k in range(rows):
            #print(giant_tab[k])
        print(another_data, "dyn", n[file], giant_tab[rows-1][columns-1], "%s " % (time.time() - start_time))