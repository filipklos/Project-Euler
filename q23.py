def dziel(a):
    sums = 0
    for i in range(1, int(a / 2) + 1):
        if a % i == 0:
            sums += i
    return sums

abundant = set()
for i in range(1, 28124):
    if dziel(i) > i:
        abundant.add(i)

numbers = set()
for i in range(1, 28124):
    numbers.add(i)

for i in abundant:
    for j in abundant:
        if i + j in numbers:
            numbers.remove(i + j)
print(sum(numbers))