file = open("piramid_67.txt")
piramid = []
for i in range(0, 100):
    line = []
    tmp = []
    for j in file.readline():
        if j != " " and j != "\n":
            tmp.append(j)
    for k in range(0, len(tmp) - 1, 2):
        line.append(int(tmp[k] + tmp[k + 1]))
    piramid.append(line)
file.close()

piramid.reverse()
while len(piramid[0]) != 1:
    for i in range(0, 1):
        for j in range(0, len(piramid[i]) - 1):
            if piramid[i][j] + piramid[i + 1][j] > piramid[i][j + 1] + piramid[i + 1][j]:
                piramid[i + 1][j] = piramid[i][j] + piramid[i + 1][j]
            else:
                piramid[i + 1][j] = piramid[i][j + 1] + piramid[i + 1][j]
        del piramid[0]
print(piramid[0][0])
