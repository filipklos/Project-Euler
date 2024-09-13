import time

start = time.time()
final_num = 0
max_chain = 0
for i in range(2, 1_000_000):
    chain = 1
    num = i
    while i != 1:
        if i % 2 == 0:
            i = i / 2
            chain += 1
        else:
            i = (i * 3) + 1
            chain += 1
    if chain > max_chain:
        max_chain = chain
        final_num = num
print(final_num, " ", max_chain)
end = time.time()
print(end - start)
