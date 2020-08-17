matriz = [[0,0,0],[0,0,0],[0,0,0]]
n=0
tot = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um número na posição [{l},{c}] da matriz:"))
        if c == 2:
            n += matriz[l][c]
        if matriz[l][c] % 2 == 0:
            tot +=matriz[l][c]
print(f"A soma de todos os números pares da matriz é {tot}")
print(f"A soma de todos os números da 3º coluna é {n}")
print(f"O maior número da segunda linha é {max(matriz[1])}")

matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Informe um valor para a matriz na posição [{l},{c}]:"))
print(30*"-=")
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]",end="")
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f"A soma dos pares foi {spar}")
for l in range(0,3):
    scol += matriz[l][2]
print(f"A soma dos valores da terceira coluna é {scol}")
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c]> mai:
        mai = matriz[1][c]
print(f"O maior valor da segunda linha é {mai}")
