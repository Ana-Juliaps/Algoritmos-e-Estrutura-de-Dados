def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def bubble_sort_otimizado(lista):
    n = len(lista)
    passagens = 0
    trocas = 0
    for i in range(n - 1):
        houve_troca = False
        passagens += 1
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                houve_troca = True
        if not houve_troca:
            break
    print("passagens="+ str(passagens))
    print("trocas" + str(trocas))
    return lista