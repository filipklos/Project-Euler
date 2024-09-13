lista = []
sol = 1
for i in range(10, 100):
    for j in range(10, i):
        k0 = i % 10
        k1 = i // 10
        l0 = j % 10
        l1 = j // 10
        if (k0 == l1) and ((l0 / k1) == (j / i)):
                lista.append((l0, k1))
                sol *= l0 / k1
        if k0 != 0:
            if (k1 == l0) and ((l1 / k0) == (j / i)):
                lista.append((l1, k0))
                sol *= l1 / k0
print(lista)
print(sol)
#otżymane liczby pomnożone przez siebie dają 8/800 czyli 1/100 wiec wynik to 100 (bo 100 w mianowniku)