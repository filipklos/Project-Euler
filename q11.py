file = open("grid_11.txt")
grid = []
for i in range(0, 20):
    tmp = []
    line = []
    for j in file.readline():
        if j != " " and j != "\n":
            tmp.append(j)
    for k in range(0, len(tmp) - 1, 2):
        line.append((int(tmp[k] + tmp[k + 1])))
    grid.append(line)
file.close()

max_multi = 0
for i in range(0, len(grid)):
    for j in range(0, len(grid[i]) - 3):
        multi = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
        if multi > max_multi:
            max_multi = multi

for i in range(0, len(grid)-3):
    for j in range(0, len(grid[i])):
        multi = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
        if multi > max_multi:
            max_multi = multi

for i in range(0, len(grid)-3):
    for j in range(0, len(grid[i])-3):
        multi = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
        if multi > max_multi:
            max_multi = multi

for i in range(0, len(grid)-3):
    for j in range(3, len(grid[i])):
        multi = grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3]
        if multi > max_multi:
            max_multi = multi

print(max_multi)
