zbior = set()
for a in range(2,101):
    for b in range(2,101):
        x = a ** b
        zbior.add(x)
print(len(zbior))