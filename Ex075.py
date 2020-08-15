lista = (int(input("Digite um número:")),int(input("Digite um número:")),int(input("Digite um número:")),int(input("Digite um número:")))
print(f"O valor nove apareceu {lista.count(9)}")
if 3 in lista:
    print(f"O valor 3 apareceu na posição {lista.index(3)}")
if 3 not in lista:
    print(f"O valor 3 não apareceu")
print("Os numeros parase foram:",end=" ")
for a, b in enumerate(lista):
    if b % 2 ==0:
        print(b ,end=" ")