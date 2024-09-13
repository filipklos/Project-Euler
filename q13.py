numbers = []
file = open("num_13.txt", )
for i in file.readlines():
    i = i.replace("\n", "")
    numbers.append(int(i))
file.close()
print(numbers)

sum_1 = 0

for i in numbers:
    sum_1 += int(i)
sum_1 = str(sum_1)
print(sum_1[0:10])
