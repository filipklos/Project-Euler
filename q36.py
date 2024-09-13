suma = 0
for i in range(1, 1_000_000):
    n = i
    b = ""
    while n > 0:
        r = n % 2
        n //= 2
        b = b + str(r)
    i = str(i)
    if i == i[::-1] and b == b[::-1]:
        suma += int(i)
print(suma)
