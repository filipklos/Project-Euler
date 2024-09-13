from math import sqrt
def sito(a):
    zbior = set()
    tmp = [True] * (a + 1)
    pier = int(sqrt(a))
    for i in range(2, pier):
        if tmp[i]:
            for j in range(i * i, a + 1, i):
                tmp[j] = False
    for i in range(2, a + 1):
        if tmp[i]:
            zbior.add(i)
    return zbior

zbior = sito(1_000_000)
wynik = set()

for i in zbior:
    n = i
    while n > 0:
        if n in zbior:
            n //= 10
        else:
            break
    m = i
    while m > 0:
        if m in zbior:
            m = str(m)
            m = m[1:len(m)]
            if m == "":
                m = 0
            else:
                m = int(m)
        else:
            break
    if n <= 0 and m <= 0:
        wynik.add(i)

#usuwanie 2,3,5,7
for i in range(2, 10):
    wynik.discard(i)
print(sum(wynik))