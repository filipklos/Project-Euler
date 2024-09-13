suma = 0
for i in range(1, 1001):
    suma += i ** i
suma = str(suma)
print(suma[len(suma)-10:])