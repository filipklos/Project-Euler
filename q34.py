ost_suma = 0
for i in range(3, 100_000):
    n = i
    suma = 0
    while n > 0:
        l = 1
        r = n % 10
        n //= 10
        for j in range(1, r + 1):
            l *= j
        suma += l
    if suma == i:
        ost_suma += i
print(ost_suma)