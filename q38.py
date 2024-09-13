def pan(a):
    for i in range(1, 10):
        if not str(i) in a:
            return False
    return True


ans = set()
for i in range(1, 1_000_000):
    a = 2
    word = str(i)
    while a > 1:
        if len(word) <= 9:
            if len(word) == 9:
                if pan(word):
                    ans.add(word)
                a = 1
            else:
                word = word + str(i * a)
                a += 1
        else:
            a = 1
print(max(ans))