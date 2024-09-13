import time
start=time.time()
c = 1
lista = [0]
lista_1 = [1]
while len(lista_1) < 1000:
    lista_2 = lista_1[::]
    lista_1.reverse()

    for j in range(0, len(lista_1)):
        if len(lista) > 0:
            lista_1[j] = lista[len(lista) - 1] + lista_1[j]
            lista.pop(len(lista) - 1)
            if lista_1[j] > 9:
                if len(lista_1) - 1 == j:
                    tmp = [lista_1[j]]
                    tmp = [tmp[0]//10, tmp[0]%10]
                    lista_tmp = [1]
                    lista_1[j] = int(tmp[1])
                    lista_1 = lista_1 + lista_tmp
                else:
                    tmp = [lista_1[j]]
                    tmp = [tmp[0] // 10, tmp[0] % 10]
                    lista_1[j] = int(tmp[1])
                    lista_1[j + 1] = lista_1[j + 1] + int(tmp[0])
    lista_1.reverse()
    lista = lista_2
    c+=1
print(len(lista_1))
print(c)
end=time.time()
print(end-start)