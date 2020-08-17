import random
from time import sleep
n = int(input("Quantos jogos você quer:"))
lista = []
li = []
for s in range (0,n):
    for num in range(0,6):
        while True:
            a = random.randint(1,60)
            if a not in lista:
                break
        li.append(a)
        if num == 5:
            li.sort()
            lista.append(li[:])
            li.clear()
print(13*"-",end="")
print("Sorteio Mega Sena",end="")
print(14*"-")
for a in range(0,n):
    print(f"O sorteio {a+1}º é {lista[a]}")
    sleep(1)
print(8*"-=", "BOA SORTE ",8*"-=")


