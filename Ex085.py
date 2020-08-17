lista = [[],[]]
b = 0
for a in range(0,7):
    b = (int(input(f"Digite o {a+1}º valor:")))
    if b % 2 == 0 or b == 0:
        lista[0].append(b)
    else:
        lista[1].append(b)
lista[0].sort()
lista[1].sort()
print(f"A lista de pares em ordem crescente é {lista[0]}")
print(f"A lista dos números ímpares na ordem crescente é {lista[1]}")

