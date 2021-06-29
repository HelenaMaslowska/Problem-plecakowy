import time
n = [8, 10, 15, 20, 25, 30, 40, 50]

for another_data in range(2):
    for file in range(len(n)):
        wmax = 0
        pmax = 0
        if not another_data:
            in_file = open("data" + str(file) + ".txt", "r")
        else:
            in_file = open("data4.txt", "r")
        elem_in_house = []  #elements in house
        for line in in_file:        #dane elementow
            a, b = line.split()
            elem_in_house.append([int(a), int(b)])

        start_time = time.time()
        for i in range(pow(2, len(elem_in_house))):
            binary = bin(i)
            binary = binary[2:]
            xw = xp = 0
            for k in range(len(binary)):
                if binary[k] != "0":
                    xw += elem_in_house[len(binary) - k-1][0]
                    xp += elem_in_house[len(binary) - k-1][1]
            if xw <= n[file] and pmax < xp:
                pmax = xp
                wmax = xw
        print(another_data, "brute", n[file], pmax, "%s " % (time.time() - start_time))
        in_file.close()
