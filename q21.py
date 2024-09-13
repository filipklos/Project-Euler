def dziel(a):
    suma = 0
    for i in range(1, int(a / 2) + 1):
        if a % i == 0:
            suma += i
    return suma


frends = set()
for i in range(1, 10_000):
    b = dziel(i)
    if dziel(b) == i and dziel(i) == b and b != i:
        frends.add(i)
        frends.add(b)
print(sum(frends))
