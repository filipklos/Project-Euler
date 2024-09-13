num = 2
max_sum = 0
while True:
    n = num
    suma = 0
    while n > 0:
        r = n % 10
        n = n // 10
        suma += r ** 5
    if suma == num:
        max_sum += num
        print(num, max_sum)
    num += 1