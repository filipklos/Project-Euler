from math import sqrt

def dziel(a):
    dzielniki = 0
    pier = int(sqrt(a))
    for i in range(1, pier + 1):
        if a % i == 0:
            dzielniki += 1
    dzielniki = dzielniki * 2
    return dzielniki

liczba = 0
s = 0
while dziel(s) < 500:
    liczba += 1
    s += liczba
print(s)
