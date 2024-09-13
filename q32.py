import time
start = time.time()
def pan(a):
    for i in range(1, 10):
        if not str(i) in a:
            return False
    return True
zbior = set()
for i in range(1, 10_000):
    for j in range(1, 10_000):
        num = i * j
        nap = str(i) + str(j) + str(num)
        if len(nap) == 9 and pan(nap):
            zbior.add(num)
print(zbior)
suma = 0
for i in zbior:
    suma += i
print(suma)
end = time.time()
print(end - start)