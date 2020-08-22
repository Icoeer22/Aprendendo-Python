from random import  randint


def sorteio(lista):
    print("Sorteando :")
    for cont in range(0,5):
        n =randint(1, 10)
        lista.append(n)
        print(f"{n}",end=" ")
def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor %2 == 0:
            soma += valor
numeros =[]
sorteio(numeros)
somaPar(numeros)
