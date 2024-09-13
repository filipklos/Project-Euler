from math import sqrt

def pierwsza(a):
  for i in range(2,int(sqrt(a))+1):
    if a%i==0:
      return False
  return True

max_dl = 0

for a in range(-1_000, 1_001):
    for b in range(-1_000, 1_001):
        n = 0
        while n >= 0:
            num = (n ** 2) + (a * n) + b
            if num < 0:
                break
            if pierwsza(num):
                n += 1
                if max_dl < n:
                    max_dl = n
                    coefficients = (a, b)
                    ab = a * b

            else:
                n = -1
print(max_dl, coefficients, ab)