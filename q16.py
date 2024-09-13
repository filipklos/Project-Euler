number = 2 ** 1000
digits_sum = 0

while number > 0:
    r = number % 10
    number = number // 10
    digits_sum += r

print(digits_sum)
