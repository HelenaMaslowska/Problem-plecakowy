
import random
n = [8, 10, 15, 20, 25, 30, 40, 50, 75, 100]  #poj plecaka
for i in range(len(n)):
    tab = []
    file = open("data" + str(i+1) + ".txt", "w")
    for j in range(n[i]//2):
        w = n[i]//2+1
        p = n[i] + 1
        line = str(random.randrange(1, w)) + " " + str(random.randrange(1, p)) + "\n"
        if line not in tab:
            tab.append(line.split())
        else:
            j = j-1
    for j in range(len(tab)):
        werso = str(tab[j][0]) + " " + str(tab[j][1]) + "\n"
        #print(werso)
        file.write(werso)
    file.close()
